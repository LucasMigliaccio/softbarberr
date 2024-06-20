from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_producto import AddEditProducto

from views.general_custom_ui import GeneralCustomUi

from database import productos


class AddProductoForm(QWidget, AddEditProducto):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        
        self.add_edit_button.clicked.connect(self.add_producto)
        self.cancel_button.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def add_producto(self):
        nombre = self.nombre_lineEdit.text()
        descripcion = self.descripcion_plainTextEdit.toPlainText()
        precio  =self.precio_lineEdit.text()
        stock = self.stock_lineEdit.text()

        data = (nombre, descripcion, precio, stock)

        if productos.insert(data):
            print("PRODUCTO AÑADIDO")
            self.clear_inputs()
            self.parent.set_table_data()

    def clear_inputs(self):
        self.nombre_lineEdit.clear()
        self.descripcion_plainTextEdit.clear()
        self.precio_lineEdit.clear()
        self.stock_lineEdit.clear()