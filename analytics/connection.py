from mysql import connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la conexión
config = {
    "user": "root",
    "password": "RammusWukong10.",
    "host": "localhost",
    "database": "barberiadb"
}

def create_connection():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print(f"Falló en la conexión a la base :(, create_connection function: {err.msg}")
    return conn

def dataframe_citas():
    conn = create_connection()
    sql = "SELECT CitaID, ClienteID, EmpleadoID, FechaHora, Monto, MetodoPago, ServiciosProgramados, Estado FROM citas"
    try:
        cur = conn.cursor()
        cur.execute(sql)
        citas = cur.fetchall()
        columns = [col[0] for col in cur.description]  # Obtener nombres de columnas
        return pd.DataFrame(citas, columns=columns)   # Convertir a DataFrame de Pandas
    except connector.Error as err:
        print(f"Error at select_all_citas function: {err.msg}")
        return None
    finally:
        cur.close()
        conn.close()

df = dataframe_citas()

# Ver las primeras filas del DataFrame
if df is not None:
    # Análisis básico de datos
    print(df.describe())

    # Análisis de la distribución de los estados de las citas
    estado_counts = df['Estado'].value_counts()
    print(estado_counts)

    # Visualizar la distribución de estados de citas

    plt.figure(figsize=(10, 6))
    sns.countplot(x='Estado', data=df)
    plt.title('Distribución de Estados de Citas')
    plt.xlabel('Estado')
    plt.ylabel('Cantidad')
    plt.show()

    # Análisis de los métodos de pago
    metodo_pago_counts = df['MetodoPago'].value_counts()
    print(metodo_pago_counts)

    # Visualizar la distribución de métodos de pago
    plt.figure(figsize=(10, 6))
    sns.countplot(x='MetodoPago', data=df)
    plt.title('Distribución de Métodos de Pago')
    plt.xlabel('Método de Pago')
    plt.ylabel('Cantidad')
    plt.show()

    # Análisis de la tendencia temporal de las citas
    df['FechaHora'] = pd.to_datetime(df['FechaHora'])
    df.set_index('FechaHora', inplace=True)
    citas_mensuales = df.resample('M').size()

    # Visualizar la tendencia de citas mensuales
    plt.figure(figsize=(10, 6))
    citas_mensuales.plot()
    plt.title('Tendencia de Citas Mensuales')
    plt.xlabel('Fecha')
    plt.ylabel('Cantidad de Citas')
    plt.show()

    # Análisis del monto de las citas completadas
    monto_completado = df[df['Estado'] == 'completado']['Monto']
    print(monto_completado.describe())

    # Visualizar la distribución del monto de citas completadas
    plt.figure(figsize=(10, 6))
    sns.histplot(monto_completado, kde=True)
    plt.title('Distribución del Monto de Citas Completadas')
    plt.xlabel('Monto')
    plt.ylabel('Frecuencia')
    plt.show()
else:
    print("No se pudieron cargar los datos de la tabla 'cita'.")
