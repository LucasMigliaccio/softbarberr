from mysql import connector

from database.connection import create_connection

def insert(data):
    conn= create_connection()
    sql = """INSERT INTO citas (ClienteID, EmpleadoID, FechaHora, Monto, Seña, 
                                MetodoPago, ServiciosProgramados, Estado, Img_path)
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
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

def select_by_id(_id):
    conn= create_connection()
    sql = f"""
    SELECT 
    citas.CitaID,
    clientes.Nombre AS ClienteNombre,
    empleados.Nombre AS EmpleadoNombre,
    citas.FechaHora,
    citas.Monto,
    citas.Seña,
    citas.ServiciosProgramados,
    citas.MetodoPago,
    citas.Estado,
    citas.Img_path,
    clientes.Telefono AS ClienteTelefono,
    clientes.Direccion AS ClienteDireccion
FROM 
    barberiadb.citas
INNER JOIN 
    clientes ON citas.ClienteID = clientes.ClienteID
INNER JOIN 
    empleados ON citas.EmpleadoID = empleados.EmpleadoID WHERE CitaID = {_id}"""
    try:
        cur = conn.cursor()
        cur.execute(sql)
        citas = cur.fetchone()
        return citas
    except connector.Error as err:
        print(f"Error en la función select_by_id: {err.msg}")
        return None  # Retornar None en lugar de False
    finally:
        cur.close()
        conn.close()

def select_all():
    conn= create_connection()
    sql = """SELECT citas.CitaID, citas.img_path, citas.FechaHora, citas.ClienteID, citas.Monto, citas.Seña, citas.EmpleadoID, citas.ServiciosProgramados, citas.MetodoPago, citas.Estado FROM citas ORDER BY FechaHora DESC"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_all_cita function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####
def select_all_join():
    conn= create_connection()
    sql = """SELECT 
    citas.CitaID,
    citas.Img_path,
    citas.FechaHora,
    clientes.Nombre AS ClienteNombre,
    citas.Monto,
    citas.Seña,
    empleados.Nombre AS EmpleadoNombre,
    citas.ServiciosProgramados,
    citas.MetodoPago,
    citas.Estado
FROM 
    citas
INNER JOIN 
    clientes ON citas.ClienteID = clientes.ClienteID
INNER JOIN 
    empleados ON citas.EmpleadoID = empleados.EmpleadoID ORDER BY FechaHora DESC LIMIT 25"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_all_cita function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def select_all_join_tableview_complete():
    conn= create_connection()
    sql = """SELECT 
    citas.CitaID,
    citas.Img_path,
    citas.FechaHora,
    clientes.Nombre AS ClienteNombre,
    citas.Monto,
    citas.Seña,
    empleados.Nombre AS EmpleadoNombre,
    citas.ServiciosProgramados,
    citas.MetodoPago,
    citas.Estado
FROM 
    citas
INNER JOIN 
    clientes ON citas.ClienteID = clientes.ClienteID
INNER JOIN 
    empleados ON citas.EmpleadoID = empleados.EmpleadoID ORDER BY FechaHora DESC"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_all_cita function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####~
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####~
####~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~####~

def update(_id,data):
    conn= create_connection()
    sql = f"""UPDATE citas SET 
            ClienteID = %s,
            EmpleadoID = %s,
            FechaHora = %s,
            Monto = %s,
            Seña = %s, 
            MetodoPago = %s, 
            ServiciosProgramados = %s, 
            Estado = %s,
            Img_path = %s
        WHERE CitaID = {_id}
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

def select_by_parameter(param):
    conn= create_connection()
    param= f"%{param}%"
    sql = """SELECT clientes.Nombre, clientes.Apellido, citas.*
        FROM clientes
        INNER JOIN citas ON clientes.ClienteID = citas.ClienteID
        WHERE clientes.Nombre LIKE %s OR clientes.Apellido LIKE %s"""
    try:
        cur= conn.cursor()
        cur.execute(sql, (param,param))
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_by_parameter: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def delete(_id):
    conn= create_connection()
    sql = f"""DELETE FROM citas
        WHERE CitaID = {_id}
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

def contrast_img(_image):
    conn= create_connection()
    sql = f"""SELECT Img_path FROM citas WHERE Img_path = '{_image}';"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_all_cita function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
    
def fix_foreingkeys():
    conn= create_connection()
    sql ="""SELECT
    citas.CitaID,
    citas.ClienteID,
    citas.EmpleadoID,
    clientes.Nombre AS NombreCliente,
    empleados.Nombre AS NombreEmpleado
    FROM
    barberiadb.citas
    INNER JOIN
    barberiadb.clientes ON citas.ClienteID = clientes.ClienteID
    INNER JOIN
    barberiadb.empleados ON citas.EmpleadoID = empleados.EmpleadoID;"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_all_cita function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

def prueba_json_servicios():
    conn= create_connection()
    sql ="""SELECT citas.ServiciosProgramados FROM citas;"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        citas=cur.fetchall()
        return citas
    except connector.Error as err:
        print(f"Error at select_all_cita function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()