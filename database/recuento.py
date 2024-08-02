from mysql import connector
from database.connection import create_connection


def filtro_efectivo_dia(fecha):
    conn= create_connection()
    sql=  f"""SELECT citas.CitaID, citas.FechaHora, citas.ClienteID, citas.Monto, citas.EmpleadoID, citas.ServiciosProgramados, citas.MetodoPago, citas.Estado, SUM(Monto) FROM barberiadb.citas WHERE MetodoPago = 'EFECTIVO' AND Estado =  'completado' AND DATE(FechaHora) = '{fecha}'"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        efectivo=cur.fetchone()
        return efectivo
    except connector.Error as err:
        print (f"Error at filtro_efectivo_dia function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
