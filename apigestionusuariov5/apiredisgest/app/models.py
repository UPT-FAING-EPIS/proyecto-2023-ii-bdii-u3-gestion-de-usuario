from flask_sqlalchemy import SQLAlchemy
import os
import redis
import json


db = SQLAlchemy()

class Rol(db.Model):
    __tablename__ = 'rol'

    rol_id = db.Column(db.Integer, primary_key=True)
    rol_nombre = db.Column(db.String(50), unique=True, nullable=False)

class Usuario(db.Model):
    __tablename__ = 'usuario'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.rol_id'), nullable=False)
    rol = db.relationship('Rol', backref=db.backref('usuarios', lazy=True))

# Configuración de la conexión a Redis, usando variables de entorno
redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_db = int(os.getenv('REDIS_DB', 0))
redis_password = os.getenv('REDIS_PASSWORD')  # Asegúrate de configurar esta variable de entorno

# Crea una instancia de Redis para manejar las sesiones
redis_instance = redis.Redis(host=redis_host, port=redis_port, db=redis_db, password=redis_password, decode_responses=True)

class SessionManager:
    @staticmethod
    def save_session(session_id, data):
        serialized_data = json.dumps(data)
        redis_instance.set(session_id, serialized_data)

    @staticmethod
    def get_session(session_id):
        # Obtener la sesión de Redis
        session_data = redis_instance.get(session_id)
        if session_data:
            return json.loads(session_data)
        return None

    # @staticmethod
    # def get_session(session_id):
    #     # Obtener la sesión de Redis
    #     data = redis_instance.get(session_id)
    #     if data:
    #         return json.loads(data)
    #     return None

    @staticmethod
    def delete_session(session_id):
        # Eliminar la sesión de Redis
        redis_instance.delete(session_id)
