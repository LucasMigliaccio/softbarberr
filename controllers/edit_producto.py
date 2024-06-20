from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, QDateTime


from views.add_producto import AddEditProducto
from views.general_custom_ui import GeneralCustomUi

from database import productos

import os 
import shutil
import datetime

class EditWindowProductoForm(QWidget,AddEditProducto):
    def __init__(self, parent= None, producto_id= None):
        self.producto_id = producto_id
        self.parent = parent

        super().__init__(parent)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_inputs()
        self.add_edit_button.setText("EDITAR")
        self.add_edit_button.clicked.connect(self.update_empleado)


    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def update_empleado(self):

        nombre = self.nombre_lineEdit.text()
        descripcion = self.descripcion_plainTextEdit.toPlainText()
        precio  =self.precio_lineEdit.text()
        stock = self.stock_lineEdit.text()

        data = (nombre, descripcion, precio, stock) 
        if productos.update(self.producto_id, data):
            print("PRODUCTO EDITADO")
            self.parent.set_table_data()
            self.close
        
    def fill_inputs(self):
        data = productos.select_by_id(self.producto_id)
        
        self.nombre_lineEdit.setText(str(data[1]))
        self.descripcion_plainTextEdit.setPlainText(str(data[2]))
        self.precio_lineEdit.setText(str(data[3]))
        self.stock_lineEdit.setText(str(data[4]))
