import os 
import shutil
import datetime
import json

from PySide6.QtWidgets import QWidget, QFileDialog, QTableView
from PySide6.QtCore import Qt, QDateTime,Signal


from views.add_edit_cita_automatizado import AddEditMenu
from views.general_custom_ui import GeneralCustomUi

from controllers.view_empleado import ViewEmpleadoWindowForm
from controllers.view_cliente import ViewClienteWindowForm
from controllers.carrito import CarritoForm

from database import citas
from models.citas import CitasTableModel


class EditWindowForm(QWidget,AddEditMenu):
    edit_finished = Signal()
    def __init__(self, parent= None, cita_id= None, source_view=None):
        self.cita_id = cita_id
        self.parent = parent
        self.source_view = source_view 

        super().__init__(parent)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        

        self.ui.fill_estado_cb()
        self.fill_inputs()
        self.add_edit_button.setText("EDITAR")
        self.add_edit_button.clicked.connect(self.update_cita)
        self.cancel_button.clicked.connect(self.close)


        self.pushButton_img_3.clicked.connect(self.open_empleados_view)
        self.pushButton_img_2.clicked.connect(self.open_clientes_view)
        self.add_producto_pushButton.clicked.connect(self.open_carrito)


        self.pushButton_img.clicked.connect(self.select_img)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def update_cita(self):
        cliente = self.leave_id_alone_cliente()
        barbero = self.leave_id_alone_barbero()
        fechayhora = self.fechahora_dateTimeEdit.dateTime()
        monto = self.monto_lineEdit.text()
        seña = self.lineEdit.text()
        metodo_pago = self.pago_comboBox.currentText()

        # NUEVOS SERVICIOS
        servicios_programados = []
        nuevos_map = {}

        for i in range(self.producto_listWidget.count()):
            texto = self.producto_listWidget.item(i).text()
            partes = dict(
                campo.strip().split(": ", 1)
                for campo in texto.split(", ")
                if ": " in campo
            )
            try:
                partes["ID"] = int(partes["ID"])
                partes["Cantidad"] = int(partes["Cantidad"])
                partes["Precio Total"] = float(partes["Precio Total"])
            except Exception as e:
                print("Error al convertir datos del producto:", partes)
                continue
            servicios_programados.append(partes)
            nuevos_map[partes["ID"]] = partes["Cantidad"]

        servicios_programados_json = json.dumps(servicios_programados, ensure_ascii=False)
        estado = self.estado_comboBox.currentText()

        if not hasattr(self, 'img_path_to') or not self.img_path_to:
            self.img_path_to = "images/imagen_custom_product_service.png"

        img = f"images\\{self.imagen_lineEdit.text()}"
        fechayhora_string = fechayhora.toString("yyyy-MM-dd HH:mm:ss")

        data = (cliente, barbero, fechayhora_string, monto, seña, metodo_pago,
                servicios_programados_json, estado, img)

        #### AJUSTE DE STOCK ####
        anteriores_ids = set(self.anteriores_map.keys())
        print("este es el ANTERIORES IDS SET MAP : ",anteriores_ids) #BORRAR DESPUES
        nuevos_ids = set(nuevos_map.keys())
        print("este es el NUEVOS IDS SET MAP : ",nuevos_ids) #BORRAR DESPUES
        todos_los_ids = anteriores_ids | nuevos_ids 

        for producto_id in todos_los_ids:
            cantidad_ant = self.anteriores_map.get(producto_id, 0)
            print("este es el ANTERIOR GET MAP : ",cantidad_ant) #BORRAR DESPUES
            cantidad_new = nuevos_map.get(producto_id, 0)
            print("este es el NUEVOS GET MAP : ",cantidad_new) #BORRAR DESPUES
            delta = cantidad_new - cantidad_ant

            if delta == 0:
                continue  # sin cambios

            # Si delta > 0 => se están agregando unidades => restar stock
            # Si delta < 0 => se están quitando unidades => devolver stock
            éxito = citas.update_product_stock_by_id(producto_id, delta)
            if not éxito:
                print(f"No pude ajustar stock del producto {producto_id}")

        #### ACTUALIZAR LA CITA ####
        if citas.update(self.cita_id, data):
            if hasattr(self, 'img_path_from') and self.img_path_from:
                self.replace_img()
            print("CITA EDITADA")

            if isinstance(self.source_view, QTableView):
                model = self.source_view.model()
                if isinstance(model, CitasTableModel):
                    model.refresh_data()
                self.edit_finished.emit()
            else:
                self.parent.set_table_data()

            self.close()


    ############################COMBOBOX SETTERS###################################
            
    def set_current_pago_cb(self, text):
        text_index= self.pago_comboBox.findText(text)
        self.pago_comboBox.setCurrentIndex(text_index)

    def set_current_estado_cb(self, text):
        text_index= self.estado_comboBox.findText(text)
        self.estado_comboBox.setCurrentIndex(text_index)

    def set_current_empleado_cb(self, text):
        text_index= self.barbero_comboBox.findText(text)
        self.barbero_comboBox.setCurrentIndex(text_index)
    
    def set_current_cliente_cb(self, text):
        text_index= self.cliente_comboBox.findText(text)
        self.cliente_comboBox.setCurrentIndex(text_index)

    ##############################################################################
        
    def fill_inputs(self):
        data = citas.select_by_id(self.cita_id)

        
        self.set_current_cliente_cb(str(data[1]))
        self.set_current_empleado_cb(str(data[2]))
        fecha_hora_db = data[3]

        if isinstance(fecha_hora_db, datetime.datetime):
            fecha_hora_db = fecha_hora_db.strftime("%Y-%m-%d %H:%M:%S")
        fecha_hora_qdatetime = QDateTime.fromString(fecha_hora_db, "yyyy-MM-dd HH:mm:ss")

        self.fechahora_dateTimeEdit.setDateTime(fecha_hora_qdatetime)
        self.monto_lineEdit.setText(str(data[4]))
        self.lineEdit.setText(str(data[5]))
        servicios = json.loads(data[6])  # Suponiendo que data[6] contiene un JSON de servicios
        # en fill_inputs, justo después de json.loads(...)

        raw_anteriores = json.loads(data[6])
        self.anteriores_map = {
            servicio['ID']: servicio['Cantidad']
            for servicio in raw_anteriores
            if isinstance(servicio, dict)
        }

        
        print("este es el json.loads de fill_inputs \n",servicios)
        #EJEMPLO
        #
        for servicio in servicios:
            if isinstance(servicio, dict):
                servicio_id = servicio.get("ID")
                nombre = servicio.get("Nombre")
                cantidad = servicio.get("Cantidad")
                print(servicio_id, nombre, cantidad)
            else:
                print("Formato inválido:", servicio)

        
        self.set_current_pago_cb(data[7])
        self.set_current_estado_cb(data[8])

        img_name = data[9].split("\\")[-1]

        self.old_image = img_name
        self.new_img = img_name

        self.imagen_lineEdit.setText(img_name)
        
        self.productos_anteriores = json.loads(data[6])  # Guardamos para revertir stock


    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]

        if self.img_path_from:
            self.new_img = self.img_path_from.split("/")[-1]
            self.imagen_lineEdit.setText(self.new_img)


    def replace_img(self):
        if self.old_image != self.new_img:
            images = citas.contrast_img(self.old_image)
            
            # Ruta de la imagen anterior
            old_image_path = os.path.join("images", self.old_image)
            
            # Verifica si la imagen anterior existe antes de intentar eliminarla
            if os.path.exists(old_image_path):
                try:
                    os.remove(old_image_path)
                    print(f"Imagen '{self.old_image}' eliminada correctamente.")
                except Exception as e:
                    print(f"No se pudo eliminar la imagen '{self.old_image}': {e}")
            else:
                print(f"Imagen '{self.old_image}' no encontrada, se omitió la eliminación.")
            
            # Copia la nueva imagen al directorio "images"
            try:
                shutil.copy(self.img_path_from, "images")
                print(f"Imagen '{self.new_img}' copiada exitosamente.")
            except Exception as e:
                print(f"No se pudo copiar la imagen '{self.new_img}': {e}")

    def leave_id_alone_cliente(self):        
        cliente_id = str(self.cliente_comboBox.currentText())
        print (cliente_id)
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
            id = producto["ID"]
            nombre = producto["Nombre"]
            cantidad = producto["Cantidad"]
            precio_total = producto["Precio Total"]
            total_precio += precio_total
            item_text = f"ID: {id}, Nombre: {nombre}, Cantidad: {cantidad}, Precio Total: {precio_total}"
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


