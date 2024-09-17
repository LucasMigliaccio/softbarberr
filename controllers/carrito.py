from PySide6.QtWidgets import QWidget, QFileDialog, QAbstractItemView
from PySide6.QtCore import Qt
from views.carritocompras import CarritoCompras
from views.general_custom_ui import GeneralCustomUi
from database import productos

from models.carrito import CarritoTableModel
from models.productos import ProductosTableModel


class CarritoForm(QWidget, CarritoCompras):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        self.productos_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Configura los modelos de tabla
        self.productos_model = ProductosTableModel(productos.select_all())
        self.carrito_model = CarritoTableModel([])  # Inicialmente vacío

        #almacena las filas
        self.filas_seleccionadas = []

        # Asocia los modelos a los QTableView
        self.productos_tableView.setModel(self.productos_model)
        self.carrito_tableView.setModel(self.carrito_model)

        # Conecta los botones a sus respectivas funciones
        self.add_pushButton.clicked.connect(self.agregar_al_carrito)
        self.add_edit_button.clicked.connect(self.agregar_producto)
        self.add_edit_button_2.clicked.connect(self.salir)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def agregar_al_carrito(self):
        # Almacena varias filas seleccionadas 
        selected_indexes = self.productos_tableView.selectionModel().selectedRows()
        print ("++++++++++",selected_indexes)

        for index in selected_indexes:
            fila_completa = []
            for column in range(self.productos_model.columnCount()):
                cell_data = self.productos_model.data(self.productos_model.index(index.row(), column), Qt.DisplayRole)
                fila_completa.append(cell_data)

            cantidad = self.contador_spinBox.value()
            #if cantidad > 1: 
            self.carrito_model.add_to_cart(fila_completa, cantidad)
            self.filas_seleccionadas.append(fila_completa)


    def agregar_producto(self):
        if self.filas_seleccionadas:
            print("filas seleccionadas: ", self.filas_seleccionadas)
            return self.filas_seleccionadas
        else:
            print("No hay filas seleccionadas")
            return None

    def salir(self):
        self.close()
