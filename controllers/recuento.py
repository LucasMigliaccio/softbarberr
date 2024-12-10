from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.recuento import RecuentoDetailWindow
from views.general_custom_ui import GeneralCustomUi

from database import recuento


class RecuentoForm(QWidget, RecuentoDetailWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.fecha_lineEdit.returnPressed.connect(self.search_linedits)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)


    def search_linedits(self):
        fecha= self.fecha_lineEdit.text()
        if fecha != "":
            print("resultado aparecio")


        data_recuento_efec=recuento.filtro_efectivo_dia(fecha)
        efectivo= str(data_recuento_efec[0])
        if efectivo == str(None):
            efectivo= str("0")

        self.efec_label.setText(efectivo)
