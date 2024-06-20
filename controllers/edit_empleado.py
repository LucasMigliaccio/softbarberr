from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, QDateTime


from views.add_barbero import AddEditEmpleado
from views.general_custom_ui import GeneralCustomUi

from database import empleados

import os 
import shutil
import datetime

class EditWindowEmpleadoForm(QWidget,AddEditEmpleado):
    def __init__(self, parent= None, empleado_id= None):
        self.empleado_id = empleado_id
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
        numero  =self.numero_lineEdit.text()
        correo = self.correo_lineEdit.text()
        direccion = self.direccion_lineEdit.text()
        especialidad= self.especialidad_lineEdit.text()

        data = (nombre, numero, correo, direccion, especialidad)

        if empleados.update(self.empleado_id, data):
            print("EMPLEADO EDITADO")
            self.parent.set_table_data()
            self.close
        
    def fill_inputs(self):
        data = empleados.select_by_id(self.empleado_id)
        
        self.nombre_lineEdit.setText(str(data[1]))
        self.numero_lineEdit.setText(str(data[2]))
        self.correo_lineEdit.setText(str(data[3])) 
        self.direccion_lineEdit.setText(str(data[4]))
        self.especialidad_lineEdit.setText(str(data[5]))