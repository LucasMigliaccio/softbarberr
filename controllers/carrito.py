from PySide6.QtWidgets import QWidget, QFileDialog
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

        # Configura los modelos de tabla
        self.productos_model = ProductosTableModel(productos.select_all())
        self.carrito_model = CarritoTableModel([])  # Inicialmente vacío

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
        # Lógica para agregar productos al carrito
        selected_indexes = self.productos_tableView.selectionModel().selectedRows()
        for index in selected_indexes:
            producto = self.productos_model.data(index, Qt.DisplayRole)
            self.carrito_model.add_product(producto)

    def agregar_producto(self):
        # Lógica para agregar un nuevo producto
        pass

    def salir(self):
        self.close()
