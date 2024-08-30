from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_edit_cita_automatizado import AddEditMenu

from views.general_custom_ui import GeneralCustomUi

from controllers.view_cliente import ViewClienteWindowForm
from controllers.view_empleado import ViewEmpleadoWindowForm
from controllers.carrito import CarritoForm

from database import citas
import shutil
import datetime

class AddWindowForm(QWidget, AddEditMenu):
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.ui.fill_estado_cb()
        self.setWindowFlag(Qt.Window)

        self.add_edit_button.setText("AGREGAR")
        self.cancel_button.clicked.connect(self.close)
        self.pushButton_img_3.clicked.connect(self.open_empleados_view)
        self.pushButton_img_2.clicked.connect(self.open_clientes_view)
        self.add_producto_pushButton.clicked.connect(self.open_carrito)


        self.add_edit_button.clicked.connect(self.add_cita)
        self.pushButton_img.clicked.connect(self.select_img)
        self.fechahora_dateTimeEdit.setDateTime(datetime.datetime.now())
        


    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def add_cita(self):
        cliente = self.leave_id_alone_cliente()
        barbero = self.leave_id_alone_barbero()
        fechayhora =self.fechahora_dateTimeEdit.dateTime()
        monto = self.monto_lineEdit.text()
        metodo_pago = self.pago_comboBox.currentText()
        servicios_programados= self.servicio_lineEdit.text()
        estado = self.estado_comboBox.currentText()
        img= self.img_path_to
        fechayhora_string = fechayhora.toString("yyyy-MM-dd HH:mm:ss")

        data = (cliente, barbero, fechayhora_string, monto, metodo_pago,
                servicios_programados, estado, img)

        if citas.insert(data):
            self.save_img()
            print("CITA AÑADIDA")
            self.clear_inputs()
            self.parent.set_table_data()

    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]
        img_name= self.img_path_from.split("/")[-1]
        self.img_path_to = f"images\{img_name}"
        self.imagen_lineEdit.setText(img_name)

    def save_img(self):
        shutil.copy(self.img_path_from, "images")

    def clear_inputs(self):
        self.fechahora_dateTimeEdit.clear()
        self.barbero_comboBox.clear()
        self.cliente_comboBox.clear()
        self.monto_lineEdit.clear()
        self.pago_comboBox.clear()
        self.estado_comboBox.clear()

    def leave_id_alone_cliente(self):        
        cliente_id = str(self.cliente_comboBox.currentText())
        id = int(cliente_id.split(' ')[0])
        print(type(id))
        return id

    def leave_id_alone_barbero(self):        
        barbero_id = str(self.barbero_comboBox.currentText())
        id = int(barbero_id.split(' ')[0])
        print(type(id))
        return id

    def open_empleados_view(self):
        window = ViewEmpleadoWindowForm(self)
        window.show()

    def open_clientes_view(self):
        window = ViewClienteWindowForm(self)
        window.show()

    def open_carrito(self):
        window = CarritoForm(self)
        window.show()