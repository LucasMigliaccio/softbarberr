from database.citas import prueba_json_servicios

import json
import re

print(prueba_json_servicios)

# JSON con los datos
json_data = '["Crema Hidratante - Cantidad: 1, Precio Total: 10", "Corte Clásico - Cantidad: 2, Precio Total: 30"]'

# Cargar los datos del JSON como lista
data = json.loads(json_data)

# Filtrar solo los nombres de los productos o servicios
nombres = [re.split(r'\s-\s', item)[0] for item in data]

print(nombres)
