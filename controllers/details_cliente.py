from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from views.detail_cliente import DetailCliente
from views.general_custom_ui import GeneralCustomUi
from database import clientes

class DetailWindowClienteForm(QWidget,DetailCliente):
    def __init__(self,parent= None, cliente_id=None):
        super().__init__(parent)

        self.cliente_id= cliente_id
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_widgets()
        self.add_edit_button_2.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)


    def fill_widgets(self):
        data = clientes.select_by_id(self.cliente_id)

        id =data[0]
        nombre =data[1]
        numero =data[2]
        correo =data[3]
        direccion =data[4]



        self.idcliente_label.setText(str(id))
        self.nombre_label.setText(str(nombre))
        self.numero_label.setText(str(numero))
        self.correo_label.setText(str(correo))
        self.direccion_label.setText(str(direccion))