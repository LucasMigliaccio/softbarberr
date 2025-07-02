from PySide6.QtWidgets import QWidget, QFileDialog,QVBoxLayout
from PySide6.QtCore import Qt

from views.ventas_x_producto import ViewProductos
from views.general_custom_ui import GeneralCustomUi

import json
import pandas as pd
from database import analytics
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from models.venta_x_productos import VentaProductosTableModel

class ViewVentaProductos(QWidget, ViewProductos):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        #self.obtener_montos_productos()
        self.init_table_model()


    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def extraer_monto(self, productos_json):
        try:
            productos = json.loads(productos_json.replace("\\", ""))
            productos_lista = []
            for item in productos:
                nombre = str(item.split("Nombre: ")[1].split(",")[0])
                cantidad = int(item.split("Cantidad: ")[1].split(",")[0])
                monto = int(item.split("Precio Total: ")[1].split(",")[0])
                productos_lista.append((nombre, cantidad, monto))
                print (productos_lista, "ESTE ES LA LISTA DE PRODUCTOS RECIBIDA, BORRAR LUEGO")
            return productos_lista
        except (json.JSONDecodeError, AttributeError, IndexError, ValueError):
            return []  # Si hay errores, retorna una lista vacía
    
    def obtener_montos_productos(self):
        # Obtener datos desde la base de datos
        analytics_data = analytics.select_all()
        df_data = pd.DataFrame(analytics_data, columns=[
            "CitaID", "ClienteID", "EmpleadoID", "FechaHora",
            "Monto", "ServiciosProgramados", "MetodoPago", "Estado", "Seña"
        ])

        # Extraer productos para cada fila
        productos_expandido = df_data["ServiciosProgramados"].apply(self.extraer_monto)
        print (productos_expandido)

        # Aplanar la lista de productos
        todos_los_productos = [item for sublist in productos_expandido for item in sublist]

        # Crear DataFrame de productos
        df_productos = pd.DataFrame(todos_los_productos, columns=["ServiciosProgramados", "Cantidad", "Monto"])

        # Agrupar por producto y sumar cantidades
        productos_con_monto = df_productos.groupby("ServiciosProgramados")[["Cantidad", "Monto"]].sum().sort_values(by = "Cantidad", ascending=False)

        return productos_con_monto.reset_index()

    def init_table_model(self):
        try:
            df_ventas = self.obtener_montos_productos()
            print(df_ventas)
            self.data_ventas_model = VentaProductosTableModel(df_ventas)
            self.mas_vendidos_tableView.setModel(self.data_ventas_model)
        except Exception as e:
            print(f"Error al cargar datos: {e}")
            empty_model = VentaProductosTableModel(pd.DataFrame(columns=["ServiciosProgramados", "Cantidad", "Monto"]))
            self.mas_vendidos_tableView.setModel(empty_model)

