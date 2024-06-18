{"filter":false,"title":"db.py","tooltip":"/database/db.py","undoManager":{"mark":99,"position":99,"stack":[[{"start":{"row":0,"column":0},"end":{"row":0,"column":1},"action":"insert","lines":["i"],"id":1},{"start":{"row":0,"column":1},"end":{"row":0,"column":2},"action":"insert","lines":["m"]},{"start":{"row":0,"column":2},"end":{"row":0,"column":3},"action":"insert","lines":["p"]},{"start":{"row":0,"column":3},"end":{"row":0,"column":4},"action":"insert","lines":["o"]},{"start":{"row":0,"column":4},"end":{"row":0,"column":5},"action":"insert","lines":["r"]},{"start":{"row":0,"column":5},"end":{"row":0,"column":6},"action":"insert","lines":["t"]}],[{"start":{"row":0,"column":6},"end":{"row":0,"column":7},"action":"insert","lines":[" "],"id":2},{"start":{"row":0,"column":7},"end":{"row":0,"column":8},"action":"insert","lines":["p"]},{"start":{"row":0,"column":8},"end":{"row":0,"column":9},"action":"insert","lines":["y"]},{"start":{"row":0,"column":9},"end":{"row":0,"column":10},"action":"insert","lines":["m"]},{"start":{"row":0,"column":10},"end":{"row":0,"column":11},"action":"insert","lines":["y"]}],[{"start":{"row":0,"column":11},"end":{"row":0,"column":12},"action":"insert","lines":["s"],"id":3},{"start":{"row":0,"column":12},"end":{"row":0,"column":13},"action":"insert","lines":["q"]},{"start":{"row":0,"column":13},"end":{"row":0,"column":14},"action":"insert","lines":["l"]}],[{"start":{"row":0,"column":0},"end":{"row":0,"column":14},"action":"remove","lines":["import pymysql"],"id":4},{"start":{"row":0,"column":0},"end":{"row":26,"column":0},"action":"insert","lines":["import pymysql","","# Datos de la instancia de RDS","endpoint = 'your-rds-endpoint.amazonaws.com'","username = 'your-username'","password = 'your-password'","database_name = 'your-database-name'","port = 3306  # Puerto por defecto de MySQL","","# Conexión a la instancia de RDS","connection = pymysql.connect(","    host=endpoint,","    user=username,","    password=password,","    database=database_name,","    port=port",")","","try:","    with connection.cursor() as cursor:","        # Ejecutar una consulta de prueba","        cursor.execute(\"SELECT VERSION()\")","        result = cursor.fetchone()","        print(\"Versión de la base de datos:\", result[0])","finally:","    connection.close()",""]}],[{"start":{"row":0,"column":0},"end":{"row":26,"column":0},"action":"remove","lines":["import pymysql","","# Datos de la instancia de RDS","endpoint = 'your-rds-endpoint.amazonaws.com'","username = 'your-username'","password = 'your-password'","database_name = 'your-database-name'","port = 3306  # Puerto por defecto de MySQL","","# Conexión a la instancia de RDS","connection = pymysql.connect(","    host=endpoint,","    user=username,","    password=password,","    database=database_name,","    port=port",")","","try:","    with connection.cursor() as cursor:","        # Ejecutar una consulta de prueba","        cursor.execute(\"SELECT VERSION()\")","        result = cursor.fetchone()","        print(\"Versión de la base de datos:\", result[0])","finally:","    connection.close()",""],"id":5},{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"insert","lines":["import os","import pymysql","from dotenv import load_dotenv","","# Cargar las variables de entorno desde el archivo .env","load_dotenv()","","# Obtener los valores de las variables de entorno","RDS_HOST = os.getenv('RDS_HOST')","RDS_PORT = int(os.getenv('RDS_PORT', 3306))  # Convertir a entero","RDS_USER = os.getenv('RDS_USER')","RDS_PASSWORD = os.getenv('RDS_PASSWORD')","RDS_DB_NAME = os.getenv('RDS_DB_NAME')","","# Establecer la conexión a la base de datos","connection = pymysql.connect(","    host=RDS_HOST,","    port=RDS_PORT,","    user=RDS_USER,","    password=RDS_PASSWORD,","    database=RDS_DB_NAME",")","","try:","    with connection.cursor() as cursor:","        # Ejecutar una consulta de prueba","        cursor.execute(\"SELECT VERSION()\")","        version = cursor.fetchone()","        print(f\"Database version: {version[0]}\")","finally:","    connection.close()",""]}],[{"start":{"row":0,"column":0},"end":{"row":31,"column":0},"action":"remove","lines":["import os","import pymysql","from dotenv import load_dotenv","","# Cargar las variables de entorno desde el archivo .env","load_dotenv()","","# Obtener los valores de las variables de entorno","RDS_HOST = os.getenv('RDS_HOST')","RDS_PORT = int(os.getenv('RDS_PORT', 3306))  # Convertir a entero","RDS_USER = os.getenv('RDS_USER')","RDS_PASSWORD = os.getenv('RDS_PASSWORD')","RDS_DB_NAME = os.getenv('RDS_DB_NAME')","","# Establecer la conexión a la base de datos","connection = pymysql.connect(","    host=RDS_HOST,","    port=RDS_PORT,","    user=RDS_USER,","    password=RDS_PASSWORD,","    database=RDS_DB_NAME",")","","try:","    with connection.cursor() as cursor:","        # Ejecutar una consulta de prueba","        cursor.execute(\"SELECT VERSION()\")","        version = cursor.fetchone()","        print(f\"Database version: {version[0]}\")","finally:","    connection.close()",""],"id":6},{"start":{"row":0,"column":0},"end":{"row":43,"column":0},"action":"insert","lines":["import os","import pymysql","from dotenv import load_dotenv","","# Cargar las variables de entorno desde el archivo .env","load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))","","# Obtener los valores de las variables de entorno","RDS_HOST = os.getenv('RDS_HOST')","RDS_PORT = int(os.getenv('RDS_PORT', 3306))  # Convertir a entero","RDS_USER = os.getenv('RDS_USER')","RDS_PASSWORD = os.getenv('RDS_PASSWORD')","RDS_DB_NAME = os.getenv('RDS_DB_NAME')","","# Establecer la conexión a la base de datos","connection = pymysql.connect(","    host=RDS_HOST,","    port=RDS_PORT,","    user=RDS_USER,","    password=RDS_PASSWORD,","    database=RDS_DB_NAME",")","","def save_user(id, name, lastname, birthday):","    try:","        with connection.cursor() as cursor:","            sql = \"INSERT INTO users (id, name, lastname, birthday) VALUES (%s, %s, %s, %s)\"","            cursor.execute(sql, (id, name, lastname, birthday))","            connection.commit()","    except Exception as e:","        print(f\"Error saving user: {e}\")","        connection.rollback()","","def get_users():","    try:","        with connection.cursor() as cursor:","            sql = \"SELECT id, name, lastname, birthday FROM users\"","            cursor.execute(sql)","            result = cursor.fetchall()","            return result","    except Exception as e:","        print(f\"Error fetching users: {e}\")","        return []",""]}],[{"start":{"row":23,"column":0},"end":{"row":23,"column":44},"action":"remove","lines":["def save_user(id, name, lastname, birthday):"],"id":7},{"start":{"row":23,"column":0},"end":{"row":23,"column":78},"action":"insert","lines":["def save_user(dni, typeDocument, name, lastname, address, phoneNumber, email):"]}],[{"start":{"row":2,"column":30},"end":{"row":3,"column":0},"action":"insert","lines":["",""],"id":9}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":25},"action":"insert","lines":["from client import Client"],"id":10}],[{"start":{"row":24,"column":14},"end":{"row":24,"column":76},"action":"remove","lines":["dni, typeDocument, name, lastname, address, phoneNumber, email"],"id":11},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["c"]},{"start":{"row":24,"column":15},"end":{"row":24,"column":16},"action":"insert","lines":["l"]},{"start":{"row":24,"column":16},"end":{"row":24,"column":17},"action":"insert","lines":["i"]},{"start":{"row":24,"column":17},"end":{"row":24,"column":18},"action":"insert","lines":["e"]},{"start":{"row":24,"column":18},"end":{"row":24,"column":19},"action":"insert","lines":["n"]},{"start":{"row":24,"column":19},"end":{"row":24,"column":20},"action":"insert","lines":["t"]}],[{"start":{"row":27,"column":12},"end":{"row":27,"column":92},"action":"remove","lines":["sql = \"INSERT INTO users (id, name, lastname, birthday) VALUES (%s, %s, %s, %s)\""],"id":12},{"start":{"row":27,"column":12},"end":{"row":30,"column":7},"action":"insert","lines":["query = \"\"\"","    INSERT INTO Client (DNI, typeDocument, name, lastname, address, phoneNumber, email)","    VALUES (%s, %s, %s, %s, %s, %s, %s)","    \"\"\""]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":13},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":14},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":15},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"insert","lines":["    "],"id":16},{"start":{"row":29,"column":0},"end":{"row":29,"column":4},"action":"insert","lines":["    "]},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":31,"column":12},"end":{"row":32,"column":31},"action":"remove","lines":["cursor.execute(sql, (id, name, lastname, birthday))","            connection.commit()"],"id":17},{"start":{"row":31,"column":12},"end":{"row":34,"column":22},"action":"insert","lines":[" cursor.execute(query, (client.dni, client.typeDocument, client.name, client.lastname, client.address, client.phoneNumber, client.email))","    connection.commit()","    cursor.close()","    connection.close()"]}],[{"start":{"row":31,"column":12},"end":{"row":31,"column":13},"action":"remove","lines":[" "],"id":18}],[{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"insert","lines":["    "],"id":19},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"insert","lines":["    "]},{"start":{"row":34,"column":0},"end":{"row":34,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":12},"end":{"row":45,"column":25},"action":"remove","lines":["sql = \"SELECT id, name, lastname, birthday FROM users\"","            cursor.execute(sql)","            result = cursor.fetchall()","            return result"],"id":20},{"start":{"row":42,"column":12},"end":{"row":49,"column":18},"action":"insert","lines":["connection = create_connection()","    cursor = connection.cursor(dictionary=True)","    query = \"SELECT * FROM Client\"","    cursor.execute(query)","    clients = cursor.fetchall()","    cursor.close()","    connection.close()","    return clients"]}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "],"id":21},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":43,"column":0},"end":{"row":43,"column":4},"action":"insert","lines":["    "],"id":22},{"start":{"row":44,"column":0},"end":{"row":44,"column":4},"action":"insert","lines":["    "]},{"start":{"row":45,"column":0},"end":{"row":45,"column":4},"action":"insert","lines":["    "]},{"start":{"row":46,"column":0},"end":{"row":46,"column":4},"action":"insert","lines":["    "]},{"start":{"row":47,"column":0},"end":{"row":47,"column":4},"action":"insert","lines":["    "]},{"start":{"row":48,"column":0},"end":{"row":48,"column":4},"action":"insert","lines":["    "]},{"start":{"row":49,"column":0},"end":{"row":49,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":42,"column":12},"end":{"row":42,"column":44},"action":"remove","lines":["connection = create_connection()"],"id":23}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":12},"action":"remove","lines":["    "],"id":24},{"start":{"row":42,"column":4},"end":{"row":42,"column":8},"action":"remove","lines":["    "]},{"start":{"row":42,"column":0},"end":{"row":42,"column":4},"action":"remove","lines":["    "]},{"start":{"row":41,"column":43},"end":{"row":42,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":25},"action":"remove","lines":["from client import Client"],"id":25},{"start":{"row":3,"column":0},"end":{"row":3,"column":34},"action":"insert","lines":["from entities.client import Client"]}],[{"start":{"row":6,"column":53},"end":{"row":6,"column":54},"action":"insert","lines":["c"],"id":26},{"start":{"row":6,"column":54},"end":{"row":6,"column":55},"action":"insert","lines":["o"]},{"start":{"row":6,"column":55},"end":{"row":6,"column":56},"action":"insert","lines":["n"]}],[{"start":{"row":6,"column":53},"end":{"row":6,"column":56},"action":"remove","lines":["con"],"id":27},{"start":{"row":6,"column":53},"end":{"row":6,"column":68},"action":"insert","lines":["connection.env'"]}],[{"start":{"row":6,"column":69},"end":{"row":6,"column":72},"action":"remove","lines":["env"],"id":28},{"start":{"row":6,"column":68},"end":{"row":6,"column":69},"action":"remove","lines":["."]},{"start":{"row":6,"column":67},"end":{"row":6,"column":69},"action":"remove","lines":["''"]}],[{"start":{"row":6,"column":67},"end":{"row":6,"column":68},"action":"insert","lines":["'"],"id":29}],[{"start":{"row":24,"column":9},"end":{"row":24,"column":13},"action":"remove","lines":["user"],"id":30},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["c"]},{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":["l"]},{"start":{"row":24,"column":11},"end":{"row":24,"column":12},"action":"insert","lines":["i"]},{"start":{"row":24,"column":12},"end":{"row":24,"column":13},"action":"insert","lines":["e"]},{"start":{"row":24,"column":13},"end":{"row":24,"column":14},"action":"insert","lines":["n"]},{"start":{"row":24,"column":14},"end":{"row":24,"column":15},"action":"insert","lines":["t"]}],[{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"remove","lines":["s"],"id":31},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"remove","lines":["r"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"remove","lines":["e"]},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"remove","lines":["s"]},{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"remove","lines":["u"]}],[{"start":{"row":39,"column":8},"end":{"row":39,"column":9},"action":"insert","lines":["c"],"id":32},{"start":{"row":39,"column":9},"end":{"row":39,"column":10},"action":"insert","lines":["l"]},{"start":{"row":39,"column":10},"end":{"row":39,"column":11},"action":"insert","lines":["i"]},{"start":{"row":39,"column":11},"end":{"row":39,"column":12},"action":"insert","lines":["e"]},{"start":{"row":39,"column":12},"end":{"row":39,"column":13},"action":"insert","lines":["n"]},{"start":{"row":39,"column":13},"end":{"row":39,"column":14},"action":"insert","lines":["t"]},{"start":{"row":39,"column":14},"end":{"row":39,"column":15},"action":"insert","lines":["s"]}],[{"start":{"row":48,"column":8},"end":{"row":48,"column":12},"action":"remove","lines":["    "],"id":33}],[{"start":{"row":42,"column":39},"end":{"row":42,"column":54},"action":"remove","lines":["dictionary=True"],"id":34}],[{"start":{"row":46,"column":8},"end":{"row":46,"column":12},"action":"remove","lines":["    "],"id":35}],[{"start":{"row":47,"column":8},"end":{"row":47,"column":12},"action":"remove","lines":["    "],"id":36}],[{"start":{"row":51,"column":17},"end":{"row":52,"column":0},"action":"insert","lines":["",""],"id":37},{"start":{"row":52,"column":0},"end":{"row":52,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":52,"column":4},"end":{"row":52,"column":8},"action":"remove","lines":["    "],"id":38}],[{"start":{"row":52,"column":4},"end":{"row":55,"column":18},"action":"insert","lines":["finally:","        cursor.close()","        connection.close()","    return clients"],"id":39}],[{"start":{"row":39,"column":18},"end":{"row":40,"column":0},"action":"insert","lines":["",""],"id":40},{"start":{"row":40,"column":0},"end":{"row":40,"column":4},"action":"insert","lines":["    "]},{"start":{"row":40,"column":4},"end":{"row":40,"column":5},"action":"insert","lines":["c"]},{"start":{"row":40,"column":5},"end":{"row":40,"column":6},"action":"insert","lines":["l"]},{"start":{"row":40,"column":6},"end":{"row":40,"column":7},"action":"insert","lines":["i"]},{"start":{"row":40,"column":7},"end":{"row":40,"column":8},"action":"insert","lines":["e"]},{"start":{"row":40,"column":8},"end":{"row":40,"column":9},"action":"insert","lines":["n"]},{"start":{"row":40,"column":9},"end":{"row":40,"column":10},"action":"insert","lines":["t"]},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["e"]},{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":["s"]}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"remove","lines":["s"],"id":41},{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"remove","lines":["e"]}],[{"start":{"row":40,"column":10},"end":{"row":40,"column":11},"action":"insert","lines":["s"],"id":42}],[{"start":{"row":40,"column":11},"end":{"row":40,"column":12},"action":"insert","lines":[" "],"id":43},{"start":{"row":40,"column":12},"end":{"row":40,"column":13},"action":"insert","lines":["="]}],[{"start":{"row":40,"column":13},"end":{"row":40,"column":14},"action":"insert","lines":[" "],"id":44}],[{"start":{"row":40,"column":14},"end":{"row":40,"column":16},"action":"insert","lines":["[]"],"id":45}],[{"start":{"row":52,"column":2},"end":{"row":52,"column":17},"action":"remove","lines":["      return []"],"id":46},{"start":{"row":52,"column":1},"end":{"row":52,"column":2},"action":"remove","lines":[" "]},{"start":{"row":52,"column":0},"end":{"row":52,"column":1},"action":"remove","lines":[" "]},{"start":{"row":51,"column":43},"end":{"row":52,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":47,"column":0},"end":{"row":48,"column":26},"action":"remove","lines":["        cursor.close()","        connection.close()"],"id":47},{"start":{"row":46,"column":39},"end":{"row":47,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":47,"column":0},"end":{"row":47,"column":22},"action":"remove","lines":["        return clients"],"id":48},{"start":{"row":46,"column":39},"end":{"row":47,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":15,"column":43},"end":{"row":16,"column":0},"action":"insert","lines":["",""],"id":49},{"start":{"row":16,"column":0},"end":{"row":16,"column":1},"action":"insert","lines":["d"]},{"start":{"row":16,"column":1},"end":{"row":16,"column":2},"action":"insert","lines":["e"]},{"start":{"row":16,"column":2},"end":{"row":16,"column":3},"action":"insert","lines":["f"]}],[{"start":{"row":16,"column":3},"end":{"row":16,"column":4},"action":"insert","lines":[" "],"id":50},{"start":{"row":16,"column":4},"end":{"row":16,"column":5},"action":"insert","lines":["g"]},{"start":{"row":16,"column":5},"end":{"row":16,"column":6},"action":"insert","lines":["e"]},{"start":{"row":16,"column":6},"end":{"row":16,"column":7},"action":"insert","lines":["t"]},{"start":{"row":16,"column":7},"end":{"row":16,"column":8},"action":"insert","lines":["C"]},{"start":{"row":16,"column":8},"end":{"row":16,"column":9},"action":"insert","lines":["o"]},{"start":{"row":16,"column":9},"end":{"row":16,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":10},"end":{"row":16,"column":11},"action":"insert","lines":["n"],"id":51},{"start":{"row":16,"column":11},"end":{"row":16,"column":12},"action":"insert","lines":["e"]},{"start":{"row":16,"column":12},"end":{"row":16,"column":13},"action":"insert","lines":["c"]},{"start":{"row":16,"column":13},"end":{"row":16,"column":14},"action":"insert","lines":["t"]},{"start":{"row":16,"column":14},"end":{"row":16,"column":15},"action":"insert","lines":["i"]},{"start":{"row":16,"column":15},"end":{"row":16,"column":16},"action":"insert","lines":["o"]},{"start":{"row":16,"column":16},"end":{"row":16,"column":17},"action":"insert","lines":["n"]}],[{"start":{"row":16,"column":17},"end":{"row":16,"column":19},"action":"insert","lines":["()"],"id":52}],[{"start":{"row":16,"column":19},"end":{"row":16,"column":20},"action":"insert","lines":[":"],"id":53}],[{"start":{"row":16,"column":20},"end":{"row":17,"column":0},"action":"insert","lines":["",""],"id":54},{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":18,"column":0},"end":{"row":18,"column":4},"action":"insert","lines":["    "],"id":55},{"start":{"row":19,"column":0},"end":{"row":19,"column":4},"action":"insert","lines":["    "]},{"start":{"row":20,"column":0},"end":{"row":20,"column":4},"action":"insert","lines":["    "]},{"start":{"row":21,"column":0},"end":{"row":21,"column":4},"action":"insert","lines":["    "]},{"start":{"row":22,"column":0},"end":{"row":22,"column":4},"action":"insert","lines":["    "]},{"start":{"row":23,"column":0},"end":{"row":23,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":17,"column":0},"end":{"row":17,"column":4},"action":"remove","lines":["    "],"id":56},{"start":{"row":16,"column":20},"end":{"row":17,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":23,"column":5},"end":{"row":24,"column":0},"action":"insert","lines":["",""],"id":57},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"insert","lines":["    "]},{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"insert","lines":["r"]},{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"insert","lines":["e"]},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"insert","lines":["t"]},{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"insert","lines":["u"]},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"insert","lines":["r"]},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"insert","lines":[" "],"id":58}],[{"start":{"row":24,"column":10},"end":{"row":24,"column":11},"action":"remove","lines":[" "],"id":59},{"start":{"row":24,"column":9},"end":{"row":24,"column":10},"action":"remove","lines":["n"]},{"start":{"row":24,"column":8},"end":{"row":24,"column":9},"action":"remove","lines":["r"]},{"start":{"row":24,"column":7},"end":{"row":24,"column":8},"action":"remove","lines":["u"]},{"start":{"row":24,"column":6},"end":{"row":24,"column":7},"action":"remove","lines":["t"]},{"start":{"row":24,"column":5},"end":{"row":24,"column":6},"action":"remove","lines":["e"]},{"start":{"row":24,"column":4},"end":{"row":24,"column":5},"action":"remove","lines":["r"]},{"start":{"row":24,"column":0},"end":{"row":24,"column":4},"action":"remove","lines":["    "]},{"start":{"row":23,"column":5},"end":{"row":24,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":13,"column":38},"end":{"row":14,"column":0},"action":"insert","lines":["",""],"id":60},{"start":{"row":14,"column":0},"end":{"row":14,"column":1},"action":"insert","lines":["c"]},{"start":{"row":14,"column":1},"end":{"row":14,"column":2},"action":"insert","lines":["o"]},{"start":{"row":14,"column":2},"end":{"row":14,"column":3},"action":"insert","lines":["n"]},{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"insert","lines":["e"]}],[{"start":{"row":14,"column":3},"end":{"row":14,"column":4},"action":"remove","lines":["e"],"id":61}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":3},"action":"remove","lines":["con"],"id":62},{"start":{"row":14,"column":0},"end":{"row":14,"column":10},"action":"insert","lines":["connection"]}],[{"start":{"row":14,"column":10},"end":{"row":14,"column":11},"action":"insert","lines":[" "],"id":63},{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["="]}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":[" "],"id":64}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":15},"action":"insert","lines":["''"],"id":65}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["'"],"id":66},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["'"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["n"],"id":67},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["u"]},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"insert","lines":["l"]},{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"insert","lines":["l"]}],[{"start":{"row":14,"column":16},"end":{"row":14,"column":17},"action":"remove","lines":["l"],"id":68},{"start":{"row":14,"column":15},"end":{"row":14,"column":16},"action":"remove","lines":["l"]},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["u"]},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["n"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["¿"],"id":69},{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"insert","lines":["¿"]}],[{"start":{"row":14,"column":14},"end":{"row":14,"column":15},"action":"remove","lines":["¿"],"id":70},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["¿"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":15},"action":"insert","lines":["''"],"id":71}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"insert","lines":["s"],"id":72}],[{"start":{"row":14,"column":9},"end":{"row":14,"column":10},"action":"remove","lines":["s"],"id":73}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":15},"action":"remove","lines":["''"],"id":74},{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"insert","lines":["2"]}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":14},"action":"remove","lines":["2"],"id":75}],[{"start":{"row":14,"column":13},"end":{"row":14,"column":15},"action":"insert","lines":["\"\""],"id":76}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":15},"action":"remove","lines":["= \"\""],"id":77},{"start":{"row":14,"column":11},"end":{"row":14,"column":26},"action":"insert","lines":["getConnection()"]}],[{"start":{"row":14,"column":11},"end":{"row":15,"column":0},"action":"insert","lines":["",""],"id":78},{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"insert","lines":["0"]}],[{"start":{"row":15,"column":0},"end":{"row":15,"column":1},"action":"remove","lines":["0"],"id":79},{"start":{"row":14,"column":11},"end":{"row":15,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":14,"column":11},"end":{"row":14,"column":12},"action":"insert","lines":["="],"id":80}],[{"start":{"row":14,"column":12},"end":{"row":14,"column":13},"action":"insert","lines":[" "],"id":81}],[{"start":{"row":27,"column":8},"end":{"row":28,"column":0},"action":"insert","lines":["",""],"id":82},{"start":{"row":28,"column":0},"end":{"row":28,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":28,"column":8},"end":{"row":29,"column":0},"action":"insert","lines":["",""],"id":83},{"start":{"row":29,"column":0},"end":{"row":29,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":29,"column":8},"end":{"row":30,"column":0},"action":"insert","lines":["",""],"id":84},{"start":{"row":30,"column":0},"end":{"row":30,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":30,"column":8},"end":{"row":31,"column":0},"action":"insert","lines":["",""],"id":85},{"start":{"row":31,"column":0},"end":{"row":31,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":31,"column":8},"end":{"row":32,"column":0},"action":"insert","lines":["",""],"id":86},{"start":{"row":32,"column":0},"end":{"row":32,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":32,"column":8},"end":{"row":33,"column":0},"action":"insert","lines":["",""],"id":87},{"start":{"row":33,"column":0},"end":{"row":33,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":29,"column":8},"end":{"row":29,"column":36},"action":"insert","lines":["connection = getConnection()"],"id":88}],[{"start":{"row":33,"column":4},"end":{"row":33,"column":8},"action":"remove","lines":["    "],"id":89},{"start":{"row":33,"column":0},"end":{"row":33,"column":4},"action":"remove","lines":["    "]},{"start":{"row":32,"column":8},"end":{"row":33,"column":0},"action":"remove","lines":["",""]},{"start":{"row":32,"column":4},"end":{"row":32,"column":8},"action":"remove","lines":["    "]},{"start":{"row":32,"column":0},"end":{"row":32,"column":4},"action":"remove","lines":["    "]},{"start":{"row":31,"column":8},"end":{"row":32,"column":0},"action":"remove","lines":["",""]},{"start":{"row":31,"column":4},"end":{"row":31,"column":8},"action":"remove","lines":["    "]},{"start":{"row":31,"column":0},"end":{"row":31,"column":4},"action":"remove","lines":["    "]},{"start":{"row":30,"column":8},"end":{"row":31,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":30,"column":4},"end":{"row":30,"column":8},"action":"remove","lines":["    "],"id":90},{"start":{"row":30,"column":0},"end":{"row":30,"column":4},"action":"remove","lines":["    "]}],[{"start":{"row":28,"column":4},"end":{"row":28,"column":8},"action":"remove","lines":["    "],"id":91},{"start":{"row":28,"column":0},"end":{"row":28,"column":4},"action":"remove","lines":["    "]},{"start":{"row":27,"column":8},"end":{"row":28,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":28,"column":36},"end":{"row":29,"column":0},"action":"remove","lines":["",""],"id":92}],[{"start":{"row":24,"column":5},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":93},{"start":{"row":25,"column":0},"end":{"row":25,"column":4},"action":"insert","lines":["    "]},{"start":{"row":25,"column":4},"end":{"row":25,"column":5},"action":"insert","lines":["r"]},{"start":{"row":25,"column":5},"end":{"row":25,"column":6},"action":"insert","lines":["e"]},{"start":{"row":25,"column":6},"end":{"row":25,"column":7},"action":"insert","lines":["t"]},{"start":{"row":25,"column":7},"end":{"row":25,"column":8},"action":"insert","lines":["u"]},{"start":{"row":25,"column":8},"end":{"row":25,"column":9},"action":"insert","lines":["r"]},{"start":{"row":25,"column":9},"end":{"row":25,"column":10},"action":"insert","lines":["n"]}],[{"start":{"row":25,"column":10},"end":{"row":25,"column":11},"action":"insert","lines":[" "],"id":94},{"start":{"row":25,"column":11},"end":{"row":25,"column":12},"action":"insert","lines":["c"]},{"start":{"row":25,"column":12},"end":{"row":25,"column":13},"action":"insert","lines":["o"]},{"start":{"row":25,"column":13},"end":{"row":25,"column":14},"action":"insert","lines":["n"]},{"start":{"row":25,"column":14},"end":{"row":25,"column":15},"action":"insert","lines":["n"]},{"start":{"row":25,"column":15},"end":{"row":25,"column":16},"action":"insert","lines":["e"]},{"start":{"row":25,"column":16},"end":{"row":25,"column":17},"action":"insert","lines":["c"]},{"start":{"row":25,"column":17},"end":{"row":25,"column":18},"action":"insert","lines":["t"]},{"start":{"row":25,"column":18},"end":{"row":25,"column":19},"action":"insert","lines":["i"]},{"start":{"row":25,"column":19},"end":{"row":25,"column":20},"action":"insert","lines":["o"]}],[{"start":{"row":25,"column":20},"end":{"row":25,"column":21},"action":"insert","lines":["n"],"id":95}],[{"start":{"row":25,"column":11},"end":{"row":25,"column":21},"action":"remove","lines":["connection"],"id":96},{"start":{"row":25,"column":11},"end":{"row":25,"column":21},"action":"insert","lines":["connection"]}],[{"start":{"row":14,"column":0},"end":{"row":14,"column":28},"action":"remove","lines":["connection = getConnection()"],"id":97}],[{"start":{"row":26,"column":0},"end":{"row":27,"column":0},"action":"insert","lines":["",""],"id":98},{"start":{"row":27,"column":0},"end":{"row":28,"column":0},"action":"insert","lines":["",""]}],[{"start":{"row":27,"column":0},"end":{"row":27,"column":28},"action":"insert","lines":["connection = getConnection()"],"id":99}],[{"start":{"row":47,"column":8},"end":{"row":48,"column":0},"action":"insert","lines":["",""],"id":100},{"start":{"row":48,"column":0},"end":{"row":48,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":48,"column":8},"end":{"row":48,"column":36},"action":"insert","lines":["connection = getConnection()"],"id":101}]]},"ace":{"folds":[],"customSyntax":"python","scrolltop":533.3333474618421,"scrollleft":0,"selection":{"start":{"row":48,"column":36},"end":{"row":48,"column":36},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":true,"wrapToView":false},"firstLineState":0},"timestamp":1718676989352,"hash":"a4e56e724f623d7aeec4d7dcaa9fb86324c15801"}