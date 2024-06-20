from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_edit_cliente import AddEditCliente

from views.general_custom_ui import GeneralCustomUi

from database import clientes


class AddClienteForm(QWidget, AddEditCliente):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        
        self.add_edit_button.clicked.connect(self.add_cita)
        self.cancel_button.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def add_cita(self):
        nombre = self.nombre_lineEdit.text()
        numero  =self.numero_lineEdit.text()
        correo = self.fechacum_lineEdit.text()
        direccion = self.direccion_lineEdit.text()

        data = (nombre, numero, correo, direccion)

        if clientes.insert(data):
            print("CLIENTE AÑADIDA")
            self.clear_inputs()
            self.parent.set_table_data()

    def clear_inputs(self):
        self.nombre_lineEdit.clear()
        self.numero_lineEdit.clear()
        self.fechacum_lineEdit.clear()
        self.direccion_lineEdit.clear()