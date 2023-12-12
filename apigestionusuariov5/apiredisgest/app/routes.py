from flask import Flask, request, jsonify, session
from dotenv import load_dotenv
import os
from flask_migrate import Migrate

from app.metrics import init_metrics

import json
import redis

from app.models import db, Usuario, Rol, SessionManager, redis_instance


from app import utils
from app.getsecret import get_secret
from app.rabbitmq_client import RabbitMQClient
from app.snsclient import create_sns_client, publish_to_sns
from app.utils import hash_password
from sqlalchemy.exc import IntegrityError

from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
# Antes de iniciar la aplicación (Flask), establece la clave secreta
app.secret_key = os.urandom(24) # es para generar claves secretas seguras flask lo necesita
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:upt.2023@db:3306/usuarios'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Conexión a Redis
redis_password = get_secret()
print("Redis password:", redis_password)
redis_db = redis.Redis(host='redis', port=6379, db=0, password=redis_password, decode_responses=True)

# Configuración de RabbitMQ
rabbitmq_config = {
    'host': '161.132.37.246',
    'port': 5672,
    'username': 'guest',
    'password': 'guest',
    'queue_name': 'cola1',
    'heartbeat': 600
}
rabbitmq_client = RabbitMQClient(rabbitmq_config)

sns_client = create_sns_client()

load_dotenv()
migrate = Migrate(app, db)
init_metrics(app)

SWAGGER_URL = '/swagger'  
API_URL = '/static/swagger.json'  

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  
    API_URL,
    config={  
        'app_name': "ApiGestionUsuariosSwagger"
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)




@app.route('/', methods=['GET'])
def home():
    return "Bienvenido a la API de Gestión de Usuarios", 200

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    user = Usuario.query.filter_by(username=username).first()
    if user and utils.check_password(user.password, password):
        session_id = str(user.user_id)
        session_data = {'user_id': user.user_id, 'username': user.username}
        SessionManager.save_session(session_id, session_data)
        session['user_id'] = user.user_id
        return jsonify({'message': 'Inicio de sesión exitoso', 'session_id': session_id}), 200
    else:
        return jsonify({'message': 'Nombre de usuario o contraseña incorrecta'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session_id = request.json.get('session_id')
    # Primero, verifica si la sesión existe
    if not SessionManager.get_session(session_id):
        # Si la sesión no existe, devuelve un mensaje de error
        return jsonify({'message': 'Este ID no se encuentra logueado o no existe.'}), 404

    # Si la sesión existe, procede con el cierre de sesión
    SessionManager.delete_session(session_id)
    session.pop('user_id', None)
    return jsonify({'message': 'Cierre de sesión exitoso'}), 200


@app.route('/user', methods=['POST'])
def create_user():
    user_data = request.json
    existing_user = Usuario.query.filter_by(username=user_data['username']).first()
    if existing_user is not None:
        return jsonify({'message': 'El nombre de usuario ya existe.'}), 400
    user = Usuario(
        username=user_data['username'],
        password=hash_password(user_data['password']),
        email=user_data['email'],
        full_name=user_data['full_name'],
        rol_id=user_data['rol_id']
    )
    db.session.add(user)
    try:
        db.session.commit()
        rabbitmq_client.publish_event('POST', f'Usuario creado: {user.user_id}')
        publish_to_sns(sns_client,'arn:aws:sns:us-east-2:825479644052:Notificacion', f'Hola, código de usuario {user.user_id} con el nombre de usuario {user.username} ha sido agregado')
        return jsonify(user_id=user.user_id), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({'message': 'Error al crear usuario.'}), 500


@app.route('/users', methods=['GET'])
def list_users():
    users = Usuario.query.all()
    users_list = [
        {
            "user_id": user.user_id,
            "username": user.username,
            "email": user.email,
            "full_name": user.full_name,
            "created_at": user.created_at.isoformat(),  
            "rol_id": user.rol_id
        } for user in users
    ]
    return jsonify(users_list), 200


@app.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = Usuario.query.get(user_id)
    if user:
        rabbitmq_client.publish_event('GET', f'Consulta de usuario con ID: {user_id}')
        return jsonify(
            username=user.username,
            email=user.email,
            full_name=user.full_name,
            created_at=user.created_at,
            rol_id=user.rol_id
        ), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_data = request.json
    user = Usuario.query.get(user_id)
    if user:
        # Actualizar cada campo si se proporciona en la solicitud
        if 'username' in user_data:
            user.username = user_data['username']
        if 'password' in user_data:
            user.password = hash_password(user_data['password'])
        if 'email' in user_data:
            user.email = user_data['email']
        if 'full_name' in user_data:
            user.full_name = user_data['full_name']
        if 'rol_id' in user_data:
            user.rol_id = user_data['rol_id']
        
        # Guardar los cambios en la base de datos
        try:
            db.session.commit()
            rabbitmq_client.publish_event('PUT', f'Usuario actualizado con ID: {user_id}')
            publish_to_sns(sns_client, 'arn:aws:sns:us-east-2:825479644052:Notificacion', f'Hola, se modificó el usuario con el nombre {user.username} con el código {user_id}')
            return jsonify({"success": "Usuario actualizado"}), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404


@app.route('/user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Usuario.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        rabbitmq_client.publish_event('DELETE', f'Usuario eliminado con ID: {user_id}')
        publish_to_sns(sns_client,'arn:aws:sns:us-east-2:825479644052:Notificacion', f'Hola, se eliminó el usuario que estaba registrado con el código {user_id}')
        return jsonify({"success": "Usuario eliminado"}), 200
    else:
        return jsonify({"error": "Usuario no encontrado"}), 404

@app.route('/rol', methods=['POST'])
def add_rol():
    data = request.json
    nuevo_rol = Rol(rol_nombre=data['rol_nombre'])
    db.session.add(nuevo_rol)
    db.session.commit()
    return jsonify({"message": "Rol creado exitosamente", "rol_id": nuevo_rol.rol_id}), 201

@app.route('/rol/<int:rol_id>', methods=['GET'])
def get_rol(rol_id):
    rol = Rol.query.get(rol_id)
    if rol:
        return jsonify({"rol_nombre": rol.rol_nombre}), 200
    else:
        return jsonify({"error": "Rol no encontrado"}), 404

@app.route('/rol/<int:rol_id>', methods=['PUT'])
def update_rol(rol_id):
    data = request.json
    rol = Rol.query.get(rol_id)
    if rol:
        rol.rol_nombre = data['rol_nombre']
        db.session.commit()
        return jsonify({"message": "Rol actualizado"}), 200
    else:
        return jsonify({"error": "Rol no encontrado"}), 404

@app.route('/rol/<int:rol_id>', methods=['DELETE'])
def delete_rol(rol_id):
    rol = Rol.query.get(rol_id)
    if rol:
        db.session.delete(rol)
        db.session.commit()
        return jsonify({"message": "Rol eliminado"}), 200
    else:
        return jsonify({"error": "Rol no encontrado"}), 404

@app.route('/roles', methods=['GET'])
def list_roles():
    roles = Rol.query.all()
    return jsonify([{"rol_id": rol.rol_id, "rol_nombre": rol.rol_nombre} for rol in roles]), 200


@app.route('/active_sessions', methods=['GET'])
def active_sessions():
    try:
        keys = redis_db.keys() 
        session_data = {}
        for key in keys:
            # Deserializar cada sesión
            session_data[key] = json.loads(redis_db.get(key))  
        return jsonify(session_data), 200
    except redis.exceptions.AuthenticationError:
        return jsonify({"error": "Autenticacion con redis erronea"}), 401
    except Exception as e:
        return jsonify({"error": str(e)}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
