import pandas as pd
from mysql import connector
from database.connection import create_connection


def select_agenda():
    conn= create_connection()
    sql = """SELECT citas.CitaID,
    DATE(citas.FechaHora) AS Fecha,
    TIME(citas.FechaHora) AS Hora,
    clientes.Nombre AS ClienteNombre,
    citas.Monto,
    citas.Seña,
    citas.ServiciosProgramados,
    citas.MetodoPago,
    citas.Estado FROM barberiadb.citas 
    INNER JOIN barberiadb.clientes ON citas.ClienteID = clientes.ClienteID ORDER BY Fecha;"""
    try:
        cursor= conn.cursor()
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=columns)

    except connector.Error as err:
        print(f"Error at select_agenda function: {err.msg}")
        return False
    finally:
        cursor.close()
        conn.close()
        return df
    
def select_citas_pendientes():
    conn= create_connection()
    sql = """SELECT citas.CitaID,
            DATE(citas.FechaHora) AS Fecha,
            TIME(citas.FechaHora) AS Hora,
            clientes.Nombre AS ClienteNombre,
            citas.Monto,
            citas.Seña,
            citas.ServiciosProgramados,
            citas.MetodoPago,
            citas.Estado
        FROM barberiadb.citas
        INNER JOIN barberiadb.clientes ON citas.ClienteID = clientes.ClienteID
        WHERE citas.Estado = 'pendiente'
        ORDER BY Fecha;"""
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