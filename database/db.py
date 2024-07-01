import os
import pymysql
from dotenv import load_dotenv
from entities.client import Client

# Cargar las variables de entorno desde el archivo .env
load_dotenv(os.path.join(os.path.dirname(__file__), 'connection.env'))

# Obtener los valores de las variables de entorno
RDS_HOST = os.getenv('RDS_HOST')
RDS_PORT = int(os.getenv('RDS_PORT', 3306))  # Convertir a entero
RDS_USER = os.getenv('RDS_USER')
RDS_PASSWORD = os.getenv('RDS_PASSWORD')
RDS_DB_NAME = os.getenv('RDS_DB_NAME')


# Establecer la conexión a la base de datos
def getConnection():
    connection = pymysql.connect(
        host=RDS_HOST,
        port=RDS_PORT,
        user=RDS_USER,
        password=RDS_PASSWORD,
        database=RDS_DB_NAME
    )
    return connection

connection = getConnection()

def save_client(client):
    isClientSaved = True
    try:
        isClientSaved = True
        connection = getConnection()
        with connection.cursor() as cursor:
            query = """
                    INSERT INTO Client (DNI, typeDocument, name, lastname, address, phoneNumber, email)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    """
            cursor.execute(query, (client.dni, client.typeDocument, client.name, client.lastname, client.address, client.phoneNumber, client.email))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        isClientSaved = False
        print(f"Error saving user: {e}")
        connection.rollback()
    finally:
        return isClientSaved

def get_clients():
    clients = []
    try:
        connection = getConnection()
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            query = "SELECT * FROM Client"
            cursor.execute(query)
            clients = cursor.fetchall()
    except Exception as e:
        print(f"Error fetching users: {e}")
    finally:
        cursor.close()
        connection.close()
    return clients
    
def get_client_id(client_id):
    client = None
    try:
        connection = getConnection()
        with connection.cursor() as cursor:
            cursor = connection.cursor()
            query = f"SELECT * FROM Client WHERE DNI = {client_id}"
            cursor.execute(query)
            client = cursor.fetchone()
    except Exception as e:
        print(f"Error fetching user with dni {client_id}: {e}")
    finally:
        cursor.close()
        connection.close()
    return client
    
