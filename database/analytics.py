import pandas as pd
from mysql import connector
from database.connection import create_connection


def select_all():
    conn= create_connection()
    sql = """SELECT CitaID, ClienteID, EmpleadoID, FechaHora, Monto, 
                                MetodoPago, ServiciosProgramados, Seña Estado FROM cita"""
    try:
        cursor= conn.cursor()
        cursor.execute(sql)
        columns = [col[0] for col in cursor.description]
        df = pd.DataFrame(cursor.fetchall(), columns=columns)

        print(df.head())
    except connector.Error as err:
        print(f"Error at select_all_cita function: {err.msg}")
        return False
    finally:
        cursor.close()
        conn.close()

print(select_all())