from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, QDateTime


from views.add_edit_cliente import AddEditCliente
from views.general_custom_ui import GeneralCustomUi

from database import clientes

import os 
import shutil
import datetime

class EditWindowClienteForm(QWidget,AddEditCliente):
    def __init__(self, parent= None, cliente_id= None):
        self.cliente_id = cliente_id
        self.parent = parent

        super().__init__(parent)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_inputs()
        self.add_edit_button.setText("EDITAR")
        self.add_edit_button.clicked.connect(self.update_cliente)


    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def update_cliente(self):

        nombre = self.nombre_lineEdit.text()
        numero  =self.numero_lineEdit.text()
        correo = self.fechacum_lineEdit.text()
        direccion = self.direccion_lineEdit.text()

        data = (
        nombre,
        numero,
        correo,
        direccion)

        if clientes.update(self.cliente_id, data):
            print("CLIENTE EDITADO")
            self.parent.set_table_data()
            self.close()
        
    def fill_inputs(self):
        data = clientes.select_by_id(self.cliente_id)
        
        self.nombre_lineEdit.setText(str(data[1]))
        self.numero_lineEdit.setText(str(data[2]))
        self.fechacum_lineEdit.setText(str(data[3])) 
        self.direccion_lineEdit.setText(str(data[4]))