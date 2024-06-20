from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from views.detail_empleado import DetailEmpleado
from views.general_custom_ui import GeneralCustomUi
from database import empleados

class DetailWindowEmpleadoForm(QWidget,DetailEmpleado):
    def __init__(self,parent= None, empleado_id=None):
        super().__init__(parent)

        self.empleado_id= empleado_id
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_widgets()
        self.add_edit_button_2.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)


    def fill_widgets(self):
        data = empleados.select_by_id(self.empleado_id)

        id =data[0]
        nombre =data[1]
        numero =data[2]
        correo =data[3]
        direccion =data[4]
        especialidad =data[5]


        self.idcliente_label.setText(str(id))
        self.nombre_label.setText(str(nombre))
        self.numero_label.setText(str(numero))
        self.correo_label.setText(str(correo))
        self.direccion_label.setText(str(direccion))
        self.especialidad_label.setText(str(especialidad))