from mysql import connector

from database.connection import create_connection

def insert(data):
    conn= create_connection()
    sql = """INSERT INTO empleados (Nombre , Telefono, CorreoElectronico, Direccion, Especialidades)
            VALUES(%s,%s,%s,%s,%s)
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at insert(empleados) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_id(_id):
    conn= create_connection()
    sql = f"""SELECT * FROM empleados WHERE EmpleadoID = {_id}"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchone()
        return citas
    except connector.Error as err:
        print(f"Error at select_by_id(empleados) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_all():
    conn= create_connection()
    sql= """SELECT EmpleadoID, Nombre, Telefono, CorreoElectronico, Direccion, Especialidades FROM empleados"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        clientes = cur.fetchall()
        return clientes
    except connector.Error as err:
        print(f"Error at select_all(empleados) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def update(_id,data):
    conn= create_connection()
    sql = f"""UPDATE empleados SET
            Nombre = %s,
            Telefono = %s, 
            CorreoElectronico = %s, 
            Direccion = %s,
            Especialidades= %s
        WHERE EmpleadoID = {_id}
            """
    try:
        cur= conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        return True
    except connector.Error as err:
        print(f"Error at update(empleado) function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_by_parameter(param):
    conn= create_connection()
    param= f"%{param}%"
    sql = """SELECT EmpleadoID, Nombre, Telefono, CorreoElectronico, Direccion, Especialidades 
        FROM empleados
        WHERE Nombre LIKE %s"""
    try:
        cur= conn.cursor()
        cur.execute(sql,(param))
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_by_parameter(empleado): {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def delete(_id):
    conn= create_connection()
    sql = f"""DELETE FROM empleados
        WHERE EmpleadoID = {_id}
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

def comboBox_empleados():
    conn= create_connection()
    sql ="""SELECT EmpleadoID, Nombre FROM empleados"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at comboBox_empleados function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()