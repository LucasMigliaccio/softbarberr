from mysql import connector

from database.connection import create_connection



def select_all():
    conn= create_connection()
    sql= """SELECT * FROM horarios"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        clientes = cur.fetchall()
        return clientes
    except connector.Error as err:
        print(f"Error at select_all(cliente) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()