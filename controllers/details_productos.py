from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

from views.detail_producto import DetailProducto
from views.general_custom_ui import GeneralCustomUi
from database import productos

class DetailWindowProductoForm(QWidget,DetailProducto):
    def __init__(self,parent= None, producto_id=None):
        super().__init__(parent)

        self.producto_id= producto_id
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fill_widgets()
        self.add_edit_button_2.clicked.connect(self.close)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)


    def fill_widgets(self):
        data = productos.select_by_id(self.producto_id)

        id =data[0]
        nombre =data[1]
        descripcion =data[2]
        precio =data[3]
        stock =data[4]
        codigo =data[5]
        codigo_barras =data[6]
        categoria =data[7]


        self.idproducto_label.setText(str(id))
        self.nombre_label.setText(str(nombre))
        self.descripcion_plainTextEdit.setPlainText(str(descripcion))
        self.numero_label.setText(str(precio))
        self.stock_label.setText(str(stock))
        self.codigo_label.setText(str(codigo))
        self.codigobarras_label.setText(str(codigo_barras))
        self.categoria_label.setText(str(categoria))
