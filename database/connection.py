from mysql import connector

config = {
    "user" : "root",
    "password":"RammusWukong1.",
    "host": "localhost",
    "database": "barberiadb"
}

def create_connection():
    conn= None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Falló en la conexión a la base :(, create_connection function: {err.msg}")
    return conn