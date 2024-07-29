from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_producto import AddEditProducto
from views.general_custom_ui import GeneralCustomUi

from database import productos

import random

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
        codigo =self.filtrar_codigo()
        codigo_de_barra =self.codigobarra_lineEdit.text()

        data = (nombre, descripcion, precio, stock, codigo, codigo_de_barra)

        if productos.insert(data):
            print("PRODUCTO AÑADIDO")
            self.clear_inputs()
            self.parent.set_table_data()

    def filtrar_codigo(self):
            marca = self.codigo_lineEdit.text() # Extrae lo que pusimos en el sistema ej: "levi´s"
            print(marca)
            marca = marca.upper() # Pone el texto(string) en mayúscula ej: "LEVI´S"
            marca = marca[:3] # Extrae los primeros 3 cáracteres ej: "LEV"
            numero_unico = random.randint(1000, 9999) # Genera el id unico del producto ej: "8532"
            marca = str(marca) + str(numero_unico) # Transforma el numero decimal en cadena de texto (string)
                # zfill: Si el numero es menor, va a rellenar con 0 a la izquierda hasta tener 4 digitos ej:"0002"
            return marca

    def clear_inputs(self):
        self.nombre_lineEdit.clear()
        self.descripcion_plainTextEdit.clear()
        self.precio_lineEdit.clear()
        self.stock_lineEdit.clear()
        self.codigo_lineEdit.clear()
        self.codigobarra_lineEdit.clear()



