import json
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()
def get_secret():
    # Configuración y obtención de la clave de AWS Secrets Manager
    secret_name = "clavebd"
    region_name = "us-east-2"

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        raise e
    else:
        if 'SecretString' in get_secret_value_response:
            secret = json.loads(get_secret_value_response['SecretString'])
            return secret.get('redispass')
        else:
            raise Exception("Secreto en formato binario no soportado.")

    return None
