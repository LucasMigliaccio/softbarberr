from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_barbero import AddEditEmpleado

from views.general_custom_ui import GeneralCustomUi

from database import empleados


class AddEmpleadoForm(QWidget, AddEditEmpleado):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        
        self.add_edit_button.clicked.connect(self.add_empleado)
        self.cancel_button.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def add_empleado(self):
        nombre = self.nombre_lineEdit.text()
        numero  =self.numero_lineEdit.text()
        correo = self.correo_lineEdit.text()
        direccion = self.direccion_lineEdit.text()
        especialidad= self.especialidad_lineEdit.text()

        data = (nombre, numero, correo, direccion, especialidad)

        if empleados.insert(data):
            print("EMPLEADO AÑADIDO")
            self.clear_inputs()
            self.parent.set_table_data()

    def clear_inputs(self):
        self.nombre_lineEdit.clear()
        self.numero_lineEdit.clear()
        self.correo_lineEdit.clear()
        self.direccion_lineEdit.clear()
        self.especialidad_lineEdit.clear()