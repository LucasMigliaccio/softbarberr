from mysql import connector
from database.connection import create_connection


def select_all():
    conn= create_connection()
    sql= """SELECT TransaccionID, CitaID, ProductosID, Cantidad, PrecioUnitario, PrecioTotal, FechaHora FROM transacciones;"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        transacciones = cur.fetchall()
        return transacciones
    except connector.Error as err:
        print(f"Error at select_all(transacciones) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def insert(data):
    conn= create_connection()
    sql = """INSERT INTO transacciones (CitaID, ProductosID, 
                    Cantidad, PrecioUnitario, PrecioTotal, FechaHora)
            VALUES(%s,%s,%s,%s,%s,%s)
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert_cita function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()