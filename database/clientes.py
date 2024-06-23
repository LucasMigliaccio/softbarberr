from mysql import connector

from database.connection import create_connection

def insert(data):
    conn= create_connection()
    sql = """INSERT INTO clientes (Nombre, Telefono, CorreoElectronico, Direccion)
            VALUES(%s,%s,%s,%s)
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert(cliente) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_id(_id):
    conn= create_connection()
    sql = f"""SELECT * FROM clientes WHERE ClienteID = {_id}"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchone()
        return citas
    except connector.Error as err:
        print(f"Error at select_by_id(cliente) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_all():
    conn= create_connection()
    sql= """SELECT ClienteID, Nombre, Telefono, CorreoElectronico, Direccion FROM clientes"""
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

def update(_id,data):
    conn= create_connection()
    sql = f"""UPDATE clientes SET
            Nombre = %s,
            Telefono = %s, 
            CorreoElectronico = %s, 
            Direccion = %s
        WHERE ClienteID = {_id}
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at update(cliente) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_parameter(param):
    conn= create_connection()
    param= f"%{param}%"
    sql = """SELECT ClienteID, Nombre, Telefono, CorreoElectronico, Direccion
        FROM clientes
        WHERE Nombre LIKE %s OR Telefono LIKE %s"""
    try:
        cur= conn.cursor()
        cur.execute(sql, (param,param))
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_by_parameter(cliente): {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def delete(_id):
    conn= create_connection()
    sql = f"""DELETE FROM clientes
        WHERE ClienteID = {_id}
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

def comboBox_clientes():
    conn= create_connection()
    sql ="""SELECT ClienteID, Nombre FROM clientes"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at comboBox_clientes function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
