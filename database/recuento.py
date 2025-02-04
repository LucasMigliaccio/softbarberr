from datetime import datetime
from mysql import connector
from database.connection import create_connection
 
def reformatear_fecha(fecha): # Convertir la cadena de fecha al formato datetime 
    fecha_obj = datetime.strptime(fecha, '%d-%m-%Y')
    fecha_reformateada = fecha_obj.strftime('%Y-%m-%d') 
    fecha_reformateada = str(fecha_reformateada)
    return fecha_reformateada

def filtro_efectivo_dia(fecha):

    conn= create_connection()
    sql=  f"""SELECT SUM(citas.Monto), SUM(citas.seña)
            FROM barberiadb.citas
            WHERE citas.MetodoPago = 'EFECTIVO' AND citas.Estado = 'completado' AND DATE(citas.FechaHora) = '{fecha}';"""
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

def filtro_transferencia_dia(fecha):

    conn= create_connection()
    sql=  f"""SELECT SUM(citas.Monto), SUM(citas.seña)
            FROM barberiadb.citas
            WHERE citas.MetodoPago = 'transferencia bancaria' AND citas.Estado = 'completado' AND DATE(citas.FechaHora) = '{fecha}';"""
    try:
        cur= conn.cursor()
        cur.execute(sql)
        transfe=cur.fetchone()
        return transfe
    except connector.Error as err:
        print (f"Error at filtro_transferencia_dia function: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()


def filtro_mp_dia(fecha):
    conn= create_connection()
    sql=  f"""SELECT SUM(citas.Monto), SUM(citas.seña)
            FROM barberiadb.citas
            WHERE citas.MetodoPago = 'Mercado Pago' AND citas.Estado = 'completado' AND DATE(citas.FechaHora) = '{fecha}';"""
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


def cierre_caja_dia_segnas(fecha):
    conn = create_connection()
    sql = f"""
        SELECT 
        MetodoPago,
        SUM(CASE WHEN Estado != 'cancelado' THEN Monto ELSE 0 END) AS monto,
        SUM(CASE WHEN Estado = 'completado' THEN Monto ELSE 0 END) AS monto_abonado,
        SUM(CASE WHEN Estado = 'completado' THEN Seña ELSE 0 END) AS total_señas_abonadas,
        SUM(CASE WHEN Estado = 'pendiente' THEN Seña ELSE 0 END) AS total_señas_,
        SUM(CASE WHEN Estado = 'pendiente' THEN (monto - seña) ELSE 0 END) AS total_pendiente_cobro
    FROM barberiadb.citas
    WHERE DATE(FechaHora) =  '{fecha}'
    GROUP BY MetodoPago;
    """
    try:
        cur = conn.cursor()
        cur.execute(sql)
        resultados = cur.fetchall()
        return resultados
    except connector.Error as err:
        print(f"Error en cierre_caja_dia: {err.msg}")
        return False
    finally:
        cur.close()
        conn.close()

