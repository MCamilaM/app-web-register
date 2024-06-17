import os
import pymysql
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener los valores de las variables de entorno
RDS_HOST = os.getenv('RDS_HOST')
RDS_PORT = int(os.getenv('RDS_PORT', 3306))  # Convertir a entero
RDS_USER = os.getenv('RDS_USER')
RDS_PASSWORD = os.getenv('RDS_PASSWORD')
RDS_DB_NAME = os.getenv('RDS_DB_NAME')

# Establecer la conexión a la base de datos
connection = pymysql.connect(
    host=RDS_HOST,
    port=RDS_PORT,
    user=RDS_USER,
    password=RDS_PASSWORD,
    database=RDS_DB_NAME
)

try:
    with connection.cursor() as cursor:
        # Ejecutar una consulta de prueba
        cursor.execute("SELECT VERSION()")
        version = cursor.fetchone()
        print(f"Database version: {version[0]}")
finally:
    connection.close()
