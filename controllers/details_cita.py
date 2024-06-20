from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from views.detail_cita import DetailsCita
from views.general_custom_ui import GeneralCustomUi
from database import citas

class DetailWindowForm(QWidget,DetailsCita):
    def __init__(self,parent= None, cita_id=None):
        super().__init__(parent)

        self.cita_id= cita_id
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_widgets()

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    # DESPUES CAMBIAR CON EL INNER JOIN LAS CELDAS CORRESPONDIENTES     
    def fill_widgets(self):
        data = citas.select_by_id(self.cita_id)

        id =data[0]
        cliente =data[1]
        telefono_cliente = data[9]
        direccion_cliente = data[10]
        barbero =data[2]
        fechahora =data[3]
        monto =data[4]
        servicios_programados =data[5]
        metodo_pago =data[6]
        estado =data[7]
        img_path =data[8]

        self.cita_id_label.setText(str(id))
        self.cliente_label.setText(str(cliente))
        self.barbero_label.setText(str(barbero))
        self.fechahora_label.setText(str(fechahora))
        self.set_monto(str(monto))
        self.metodo_pago_label.setText(str(metodo_pago))
        self.estado_label.setText(str(estado))
        self.set_cita_image(img_path)
        self.telefono_label.setText(str(telefono_cliente))
        self.direccion_label.setText(str(direccion_cliente))
        
    def set_monto(self,widget):
        montos=f"${str(widget)}"
        self.monto_label.setText(montos)
    
    #funcion para poner la imagen
    def set_cita_image(self,img_path):
        pix_map =QPixmap(img_path)
        self.img_label.setPixmap(pix_map)
        self.img_label.setScaledContents(True)