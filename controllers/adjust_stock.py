from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, QDateTime


from views.adjust_stock import AdjustStockProducto
from views.general_custom_ui import GeneralCustomUi

from database import stock

import os 
import shutil
import datetime

class AdjustStockProductoForm(QWidget,AdjustStockProducto):
    def __init__(self, parent= None, producto_id= None):
        self.producto_id = producto_id
        self.parent = parent

        super().__init__(parent)
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_inputs()
        self.add_edit_button.setText("EDITAR")
        self.add_edit_button.clicked.connect(self.update_stock_product)
        self.spinBox.setMinimum(1)  # Valor mínimo
        self.spinBox.setMaximum(10000)


    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)
    
    def update_stock_product(self):
        producto_id = self.producto_id
        stock_actual = self.spinBox.value()
        stock_actual = int(stock_actual)

        if stock.update_stock_del_producto(stock_actual, producto_id):
            print("STOCK DE PRODUCTO EDITADO")
            self.parent.set_table_data()
            self.close()

        
    def fill_inputs(self):
        data = stock.select_by_id(self.producto_id)
        
        self.product_name_label.setText(str(data[1]))
        self.stock_actual_label.setText(str(data[4]))
        self.spinBox.setValue(int(data[4]))
