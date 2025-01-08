from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.recuento_calendario import RecuentoDetailWindow
from views.general_custom_ui import GeneralCustomUi

from database import recuento


class RecuentoForm(QWidget, RecuentoDetailWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.selected_date_str = None

        self.calendarWidget.clicked.connect(self.obtener_fecha_seleccionada)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def obtener_fecha_seleccionada(self):
        """Obtiene la fecha seleccionada y la guarda como un atributo."""
        selected_date = self.calendarWidget.selectedDate()
        self.selected_date_str = selected_date.toString("yyyy-MM-dd")
        print("Fecha seleccionada:", self.selected_date_str)
        data_efectivo = recuento.filtro_efectivo_dia(self.selected_date_str)
        efectivo = str(data_efectivo[0])
        if efectivo == str(None):
            efectivo= str("0")
        data_mp = recuento.filtro_mp_dia(self.selected_date_str)
        mp = str(data_mp[0])
        if mp == str(None):
            mp= str("0")

        self.efec_label.setText(efectivo)
        self.mp_label.setText(mp)
        
        efectivo = int(efectivo)
        mp = int(mp)
        total = (mp + efectivo)
        self.total_label.setText(str(total))

        gastos = self.gastos_lineEdit.text()
        if gastos != "":
            gastos = int(gastos)
            total = (total - gastos)
            self.total_label.setText(str(total))

    def put_efectivo(self):
        """Utiliza la fecha seleccionada almacenada."""
        if self.selected_date_str:
            print(f"Usando la fecha seleccionada: {self.selected_date_str}")
            fecha = self.selected_date_str
            efectivo = recuento.filtro_efectivo_dia(fecha)
            # Aquí puedes usar self.selected_date_str en lugar de format_date
        else:
            print("No se ha seleccionado ninguna fecha.")