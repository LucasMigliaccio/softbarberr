import pandas as pd
from mysql import connector
from database.connection import create_connection


def select_by_id(_id):
    conn= create_connection()
    sql = f"""SELECT * FROM productos WHERE ProductoID = {_id}"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        productos=cur.fetchone()
        return productos
    except connector.Error as err:
        print(f"Error at select_by_id(adjust_stock) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def update_stock_del_producto(nuevo_stock,_id):
    conn = create_connection() 
    sql_update = f"UPDATE productos SET CantidadEnStock = {nuevo_stock} WHERE ProductoID = {_id} "

    try:
        cur= conn.cursor()
        cur.execute(sql_update)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error al actualizar stock para '{nuevo_stock}': {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()