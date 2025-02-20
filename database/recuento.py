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
    COALESCE(m.MetodoPago, 'Sin datos') AS MetodoPago,
    COALESCE(SUM(CASE WHEN c.Estado != 'cancelado' THEN c.Monto ELSE 0 END), 0) AS monto,
    COALESCE(SUM(CASE WHEN c.Estado = 'completado' THEN c.Monto ELSE 0 END), 0) AS monto_abonado,
    COALESCE(SUM(CASE WHEN c.Estado = 'completado' THEN c.Seña ELSE 0 END), 0) AS total_señas_abonadas,
    COALESCE(SUM(CASE WHEN c.Estado = 'pendiente' THEN c.Seña ELSE 0 END), 0) AS total_señas_,
    COALESCE(SUM(CASE WHEN c.Estado = 'pendiente' THEN (c.Monto - c.Seña) ELSE 0 END), 0) AS total_pendiente_cobro
FROM 
    (SELECT DISTINCT MetodoPago FROM barberiadb.citas) m
LEFT JOIN 
    barberiadb.citas c
ON 
    m.MetodoPago = c.MetodoPago
AND 
    DATE(c.FechaHora) = '{fecha}'
GROUP BY 
    m.MetodoPago;

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

