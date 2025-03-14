import json
import pandas as pd
from database import analytics

# Obtener los datos de la base de datos
analytics_data = analytics.select_all()

# Convertir los datos a un DataFrame
df_data = pd.DataFrame(analytics_data, columns=[
    "CitaID", "ClienteID", "EmpleadoID", "FechaHora", 
    "Monto", "ServiciosProgramados", "MetodoPago", "Estado", "Seña"
])

print (df_data)
print (df_data["ServiciosProgramados"])
# Función para extraer productos del JSON
def extraer_productos(productos_json):
    try:
        productos = json.loads(productos_json.replace("\\", ""))
        productos_lista = []
        for item in productos:
            nombre = item.split(" - ")[0]
            cantidad = int(item.split("Cantidad: ")[1].split(",")[0])
            productos_lista.append((nombre, cantidad))
        return productos_lista
    except (json.JSONDecodeError, AttributeError, IndexError, ValueError):
        return []  # En caso de errores, retorna una lista vacía

# Aplicar la función a cada fila
productos_expandido = df_data["ServiciosProgramados"].apply(extraer_productos)

# Unir todos los productos en una lista plana
todos_los_productos = [item for sublist in productos_expandido for item in sublist]

# Crear un DataFrame con los productos
df_productos = pd.DataFrame(todos_los_productos, columns=["ServiciosProgramados", "Cantidad"])

# Agrupar y sumar las cantidades
productos_mas_vendidos = df_productos.groupby("ServiciosProgramados")["Cantidad"].sum().sort_values(ascending=False)

print(productos_mas_vendidos)
print(type(productos_mas_vendidos))
