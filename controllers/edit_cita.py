from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, QDateTime


from views.add_edit_cita_fecha import AddEditMenu
from views.general_custom_ui import GeneralCustomUi

from database import citas

import os 
import shutil
import datetime

class EditWindowForm(QWidget,AddEditMenu):
    def __init__(self, parent= None, cita_id= None):
        self.cita_id = cita_id
        self.parent = parent

        super().__init__(parent)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.ui.fill_estado_cb()
        self.fill_inputs()
        self.add_edit_button.setText("EDITAR")
        self.add_edit_button.clicked.connect(self.update_cita)
        self.pushButton_img.clicked.connect(self.select_img)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def update_cita(self):
        cliente = self.cliente_lineEdit.text()
        barbero = self.barbero_lineEdit.text()
        fechayhora =self.fechahora_dateTimeEdit.dateTime()
        monto = self.monto_lineEdit.text()
        metodo_pago = self.pago_comboBox.currentText()
        servicios_programados= self.servicio_lineEdit.text()
        estado = self.estado_comboBox.currentText()
        img= f"images\{self.imagen_lineEdit.text()}" ############
        fechayhora_string = fechayhora.toString("yyyy-MM-dd HH:mm:ss")
        #borrar despues

        data = (cliente, barbero, fechayhora_string, monto, metodo_pago,
                servicios_programados, estado, img)

        if citas.update(self.cita_id, data):
            self.replace_img()
            print("CITA EDITADA")
            self.parent.set_table_data()
            self.close
    ############################COMBOBOX SETTERS###################################
            
    def set_current_pago_cb(self, text):
        text_index= self.pago_comboBox.findText(text)
        self.pago_comboBox.setCurrentIndex(text_index)

    def set_current_estado_cb(self, text):
        text_index= self.estado_comboBox.findText(text)
        self.estado_comboBox.setCurrentIndex(text_index)

    ##############################################################################
        
    def fill_inputs(self):
        data = citas.select_by_id(self.cita_id)

        
        self.cliente_lineEdit.setText(str(data[1]))
        self.barbero_lineEdit.setText (str(data[2]))
        #self.fechahora_dateTimeEdit.setTime(data[3])
        fecha_hora_db = data[3]

        if isinstance(fecha_hora_db, datetime.datetime):
            fecha_hora_db = fecha_hora_db.strftime("%Y-%m-%d %H:%M:%S")
        fecha_hora_qdatetime = QDateTime.fromString(fecha_hora_db, "yyyy-MM-dd HH:mm:ss")

        self.fechahora_dateTimeEdit.setDateTime(fecha_hora_qdatetime)
        self.monto_lineEdit.setText(str(data[4]))
        self.servicio_lineEdit.setText(str(data[5]))
        self.set_current_pago_cb(data[6])
        self.set_current_estado_cb(data[7])

        img_name = data[8].split("\\")[-1]

        self.old_image = img_name
        self.new_img = img_name

        self.imagen_lineEdit.setText(img_name)

    def select_img(self):
        self.img_path_from = QFileDialog.getOpenFileName()[0]

        if self.img_path_from:
            self.new_img = self.img_path_from.split("/")[-1]
            self.imagen_lineEdit.setText(self.new_img)


    def replace_img(self):
        if self.old_image != self.new_img:
            images = citas.contrast_img(self.old_image)
            os.remove ("images\\" + self.old_image)
            shutil.copy(self.img_path_from, "images")