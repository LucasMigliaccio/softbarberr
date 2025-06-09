from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.add_stock_product import AddStockWindow
from views.general_custom_ui import GeneralCustomUi

from database import productos

import random

class AddStockoForm(QWidget, AddStockWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        
        self.add_edit_button.clicked.connect(self.add_new_stock)
        self.add_edit_button.setText("ACTUALIZAR")
        self.cancel_button.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

# add_stock_producto(nuevo_stock,_id):

    def fill_inputs(self):
        data = productos.select_by_id(self.producto_id)
        
        pass

    def add_new_stock(self):
        pass