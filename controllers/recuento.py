from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt

from views.recuento_calendario import RecuentoDetailWindow
from views.general_custom_ui import GeneralCustomUi

from database import recuento

import pandas as pd
from decimal import Decimal


class RecuentoForm(QWidget, RecuentoDetailWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent=parent

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.selected_date_str = None

        self.calendarWidget.clicked.connect(self.obtener_cierre_segnas)

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

        self.efec_segna_label_.setText(segna_efectivo)
        self.mp_segna_label.setText(segna_mp)
        self.transfe_segna_label.setText(segna_transfer)
        
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
        #data = recuento.filtro_efectivo_dia(self.selected_date_str)
        #total_pagado_efectivo =str(data[0])
        #print (total_pagado_efectivo)
        fecha = self.selected_date_str
        cierre = recuento.cierre_caja_dia_segnas(fecha)

        # Conversion a dataFrame
        columns = ["Método de Pago", "Monto", "Monto Abonado", "Total Señas", "Señas Abonadas", "Total Pendiente Cobro"]
        df = pd.DataFrame(cierre, columns=columns)
        # Valores por defecto

        primera_fila = {
            "Método de Pago": "Efectivo",
            "Monto": 0,
            "Monto Abonado": 0,
            "Total Señas": 0,
            "Señas Abonadas": 0,
            "Total Pendiente Cobro": 0
        }
        segunda_fila = {
            "Método de Pago": "Transferencia",
            "Monto": 0,
            "Monto Abonado": 0,
            "Total Señas": 0,
            "Señas Abonadas": 0,
            "Total Pendiente Cobro": 0
        }
        tercer_fila = {
            "Método de Pago": "Mercado Pago",
            "Monto": 0,
            "Monto Abonado": 0,
            "Total Señas": 0,
            "Señas Abonadas": 0,
            "Total Pendiente Cobro": 0
        }

        
        # Extraer primera y segunda fila
        if len(df) > 0:
            primera_fila = df.iloc[0].to_dict() 
        if len(df) > 1:
            segunda_fila = df.iloc[1].to_dict()
        if len(df) > 2:
            tercer_fila = df.iloc[2].to_dict()


        # Extraer datos específicos en variables
        metodo_pago_efectivo = primera_fila["Método de Pago"]
        total_monto_efectivo = primera_fila["Monto"]
        total_monto_abonado_efectivo = primera_fila["Monto Abonado"]
        total_segna_efectivo = primera_fila["Total Señas"]
        segna_abonada_efectivo = primera_fila["Señas Abonadas"]
        pendiente_cobro_efectivo = primera_fila["Total Pendiente Cobro"]

        metodo_pago_transfe = segunda_fila["Método de Pago"]
        total_monto_transfe = segunda_fila["Monto"]
        total_monto_abonado_transfe = segunda_fila["Monto Abonado"]
        total_segna_transfe = segunda_fila["Total Señas"]
        segna_abonada_transfe = segunda_fila["Señas Abonadas"]
        pendiente_cobro_transfe = segunda_fila["Total Pendiente Cobro"]

        metodo_pago_mp = tercer_fila["Método de Pago"]
        total_monto_mp = tercer_fila["Monto"]
        total_monto_abonado_mp = tercer_fila["Monto Abonado"]
        total_segna_mp = tercer_fila["Total Señas"]
        segna_abonada_mp = tercer_fila["Señas Abonadas"]
        pendiente_cobro_mp = tercer_fila["Total Pendiente Cobro"]

        # monto  general sin distinguir seña
        total_monto_efectivo = int(total_monto_efectivo)
        
        total_monto_mp = int(total_monto_mp)
        total_monto_transfe = int(total_monto_transfe)
        total_monto_todos_medios = (total_monto_efectivo + total_monto_mp + total_monto_transfe)

        # total de señas  en estado pendiente
        segna_abonada_mp = int(segna_abonada_mp)
        segna_abonada_efectivo = int(segna_abonada_efectivo)
        segna_abonada_transfe = int(segna_abonada_transfe)
        total_segnas_en_estado_pendiente = (segna_abonada_mp + segna_abonada_efectivo + segna_abonada_transfe)

        # señas pendientes
        total_monto_abonado_efectivo = int(total_monto_abonado_efectivo)
        total_monto_abonado_mp = int(total_monto_abonado_mp)
        total_monto_abonado_transfe = int(total_monto_abonado_transfe)
        total_monto_abonado_completado = (total_monto_abonado_efectivo + total_monto_abonado_mp + total_monto_abonado_transfe)

        # pendiente de cobro       
        pendiente_cobro_efectivo = int(pendiente_cobro_efectivo)
        pendiente_cobro_mp = int(pendiente_cobro_mp)
        pendiente_cobro_transfe = int(pendiente_cobro_transfe)
        total_pendientes_todos_medios = (pendiente_cobro_efectivo + pendiente_cobro_mp + pendiente_cobro_transfe)


        #fill inputs 
        self.efec_label.setText(str(total_monto_abonado_efectivo))
        self.mp_label.setText(str(total_monto_abonado_mp))
        self.transfe_label.setText(str(total_monto_abonado_transfe))

        self.efec_segna_label_.setText(str(segna_abonada_efectivo))
        self.mp_segna_label.setText(str(segna_abonada_mp))
        self.transfe_segna_label.setText(str(segna_abonada_transfe))

        self.total_pendiente_cobro_edit.setText(str(total_pendientes_todos_medios))       
        self.total_label.setText(str(total_monto_abonado_completado))
        
        gastos = self.gastos_lineEdit.text()
        if gastos != "":
            gastos = int(gastos)
            total_monto_abonado_completado = (total_monto_abonado_completado - gastos)
            self.total_label.setText(str(total_monto_abonado_completado))

        self.total_monto_edit.setText(str(total_monto_todos_medios))
        self.total_monto_pendiente_edit.setText(str(total_monto_todos_medios))


    def put_efectivo(self):
        """Utiliza la fecha seleccionada almacenada."""
        if self.selected_date_str:
            print(f"Usando la fecha seleccionada: {self.selected_date_str}")
            fecha = self.selected_date_str
            efectivo = recuento.filtro_efectivo_dia(fecha)
            # Aquí puedes usar self.selected_date_str en lugar de format_date
        else:
            print("No se ha seleccionado ninguna fecha.")