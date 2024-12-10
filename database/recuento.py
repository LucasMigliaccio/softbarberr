from datetime import datetime
from mysql import connector
from database.connection import create_connection
 
def reformatear_fecha(fecha): # Convertir la cadena de fecha al formato datetime 
    fecha_obj = datetime.strptime(fecha, '%d-%m-%Y')
    fecha_reformateada = fecha_obj.strftime('%Y-%m-%d') 
    fecha_reformateada = str(fecha_reformateada)
    return fecha_reformateada

def filtro_efectivo_dia(fecha):
    print("fecha base:", fecha, type(fecha))
    fecha_final = reformatear_fecha(fecha)
    print("fecha final:", fecha_final, type(fecha))

    conn= create_connection()
    sql=  f"""SELECT SUM(citas.Monto)
            FROM barberiadb.citas
            WHERE citas.MetodoPago = 'EFECTIVO' AND citas.Estado = 'compleado' AND DATE(citas.FechaHora) = '{fecha_final}';"""
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


def filtro_mp_dia(fecha):
    conn= create_connection()
    sql=  f"""SELECT citas.CitaID, citas.FechaHora, citas.ClienteID, citas.Monto, citas.EmpleadoID, citas.ServiciosProgramados, citas.MetodoPago, citas.Estado, SUM(Monto) FROM barberiadb.citas WHERE MetodoPago = 'MERCADOPAGO' AND Estado =  'completado' AND DATE(FechaHora) = '{fecha}'"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        mp=cur.fetchone()
        return mp
    except connector.Error as err:
        print (f"Error at filtro_mp_dia function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()
