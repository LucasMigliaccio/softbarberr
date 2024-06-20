from mysql import connector
from database.connection import create_connection

def insert(data):
    conn= create_connection()
    sql = """INSERT INTO productos (NombreDelProducto, Descripcion, Precio, CantidadEnStock )
            VALUES(%s,%s,%s,%s)
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert(productos) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_id(_id):
    conn= create_connection()
    sql = f"""SELECT * FROM productos WHERE ProductoID = {_id}"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        productos=cur.fetchone()
        return productos
    except connector.Error as err:
        print(f"Error at select_by_id(productos) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_all():
    conn= create_connection()
    sql= """SELECT ProductoID, NombreDelProducto, Descripcion, Precio, CantidadEnStock FROM productos"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        productos = cur.fetchall()
        return productos
    except connector.Error as err:
        print(f"Error at select_all(producto) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def update(_id,data):
    conn= create_connection()
    sql = f"""UPDATE productos SET
            NombreDelProducto = %s,
            Descripcion = %s,
            Precio = %s, 
            CantidadEnStock = %s
        WHERE ProductoID = {_id}
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at update(producto) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_parameter(param):
    conn= create_connection()
    param= f"%{param}%"
    sql = """SELECT ProductoID, NombreDelProducto, Descripcion, Precio, CantidadEnStock 
        FROM productos
        WHERE NombreDelProducto LIKE %s OR CantidadEnStock LIKE %s"""
    try:
        cur= conn.cursor()
        cur.execute(sql, (param,param))
        productos=cur.fetchall()
        return productos
    except connector.Error as err:
        print(f"Error at select_by_parameter(productos): {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def delete(_id):
    conn= create_connection()
    sql = f"""DELETE FROM productos
        WHERE ProductoID = {_id}
            """
    try:
        cur= conn.cursor()
        cur.execute(sql)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at delete function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()