from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.recuento_calendario import RecuentoDetailWindow
from views.general_custom_ui import GeneralCustomUi

from database import recuento

import pandas as pd


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
        segna_efectivo = str(data_efectivo[1])
        if segna_efectivo == str(None):
            segna_efectivo= str("0")

        data_mp = recuento.filtro_mp_dia(self.selected_date_str)
        mp = str(data_mp[0])
        if mp == str(None):
            mp= str("0")
        segna_mp = str(data_mp[1])
        if segna_mp == str(None):
            segna_mp= str("0")

        data_transfer = recuento.filtro_transferencia_dia(self.selected_date_str)
        transfer = str(data_transfer[0])
        if transfer == str(None):
            transfer= str("0")
        segna_transfer = str(data_transfer[1])
        if segna_transfer == str(None):
            segna_transfer= str("0")

        self.efec_label.setText(efectivo)
        self.mp_label.setText(mp)
        self.transfe_label.setText(transfer)

        self.efec_segna_label_.setText()
        self.mp_segna_label.setText()
        self.transfe_segna_label.setText()
        
        transfer = int(transfer)
        efectivo = int(efectivo)
        mp = int(mp)

        segna_transfer= int(segna_transfer)
        segna_mp= int(segna_mp)
        segna_efectivo= int(segna_efectivo)

        total = (mp + efectivo + transfer + segna_efectivo + segna_mp + segna_transfer)
        self.total_label.setText(str(total))

        gastos = self.gastos_lineEdit.text()
        if gastos != "":
            gastos = int(gastos)
            total = (total - gastos)
            self.total_label.setText(str(total))
        
        self.obtener_cierre_segnas()

    def obtener_cierre_segnas(self):
        selected_date = self.calendarWidget.selectedDate()
        self.selected_date_str = selected_date.toString("yyyy-MM-dd")
        fecha = self.selected_date_str
        cierre = recuento.cierre_caja_dia_segnas(fecha)

        # Convertimos a DataFrame
        columns = ["Método de Pago", "Monto", "Total Señas", "Señas Abonadas", "Total Pendiente Cobro"]
        df = pd.DataFrame(cierre, columns=columns)

        # Extraer primera y segunda fila (si existen)
        if len(df) > 0:
            primera_fila = df.iloc[0].to_dict() 
        if len(df) > 1:
            segunda_fila = df.iloc[1].to_dict()


        # Extraer datos específicos en variables
        metodo_pago = primera_fila["Método de Pago"]
        total_monto = primera_fila["Monto"]
        total_segna = primera_fila["Total Señas"]
        segna_abonada = primera_fila["Señas Abonadas"]
        pendiente_cobro = primera_fila["Total Pendiente Cobro"]

        metodo_pago_mp = segunda_fila["Método de Pago"]
        total_monto_mp = segunda_fila["Monto"]
        total_segna_mp = segunda_fila["Total Señas"]
        segna_abonada_mp = segunda_fila["Señas Abonadas"]
        pendiente_cobro_mp = segunda_fila["Total Pendiente Cobro"]

    def put_efectivo(self):
        """Utiliza la fecha seleccionada almacenada."""
        if self.selected_date_str:
            print(f"Usando la fecha seleccionada: {self.selected_date_str}")
            fecha = self.selected_date_str
            efectivo = recuento.filtro_efectivo_dia(fecha)
            # Aquí puedes usar self.selected_date_str en lugar de format_date
        else:
            print("No se ha seleccionado ninguna fecha.")