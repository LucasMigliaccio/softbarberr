import shutil
import datetime
import json

from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_edit_cita_automatizado import AddEditMenu

from views.general_custom_ui import GeneralCustomUi

from controllers.view_cliente import ViewClienteWindowForm
from controllers.view_empleado import ViewEmpleadoWindowForm
from controllers.carrito import CarritoForm

from database import citas

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
        seña = self.lineEdit.text()
        metodo_pago = self.pago_comboBox.currentText()
        servicios_programados= [self.producto_listWidget.item(i).text() for i in range(self.producto_listWidget.count())]
        servicios_programados_json = json.dumps(servicios_programados)
        estado = self.estado_comboBox.currentText()

        if not hasattr(self, 'img_path_to') or not self.img_path_to:
            self.img_path_to = "images/imagen_custom_product_service.png"

        img= self.img_path_to
        fechayhora_string = fechayhora.toString("yyyy-MM-dd HH:mm:ss")

        data = (cliente, barbero, fechayhora_string, monto, seña, metodo_pago,
                servicios_programados_json, estado, img)

        if citas.insert(data):
            if hasattr(self, 'img_path_from') and self.img_path_from:
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
        if hasattr(self, 'img_path_from') and self.img_path_from:
            shutil.copy(self.img_path_from, "images")

    def clear_inputs(self):
        self.fechahora_dateTimeEdit.clear()
        self.barbero_comboBox.clear()
        self.cliente_comboBox.clear()
        self.monto_lineEdit.clear()
        self.lineEdit.clear()
        self.pago_comboBox.clear()
        self.estado_comboBox.clear()

    def segna_none(self):
        segna = self.lineEdit
        if segna == None:
            self.lineEdit.setText("0")
    

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

    def recibir_productos(self, productos):
        """Recibe la lista de productos desde CarritoForm y los añade al ListWidget."""
        self.producto_listWidget.clear() # Limpiar lista antes de agregar nuevos productos
        total_precio = 0 
        
        for producto in productos:
            nombre = producto["Nombre"]
            cantidad = producto["Cantidad"]
            precio_total = producto["Precio Total"]
            total_precio += precio_total
            item_text = f"{nombre} - Cantidad: {cantidad}, Precio Total: {precio_total}"
            self.producto_listWidget.addItem(item_text)
        
        total_precio = int(total_precio)
        self.monto_lineEdit.setText(f"{total_precio:.2f}")

    def open_empleados_view(self):
        window = ViewEmpleadoWindowForm(self)
        window.show()

    def open_clientes_view(self):
        window = ViewClienteWindowForm(self)
        window.show()

    def open_carrito(self):
        window = CarritoForm(self)
        window.show()
