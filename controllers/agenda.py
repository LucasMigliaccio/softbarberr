from PySide6.QtCore import Qt,QDate
from PySide6.QtGui import QPixmap,QTextCharFormat, QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QWidget

from views.agenda import Agenda
from views.general_custom_ui import GeneralCustomUi
from database import agenda
import pandas as pd

class AgendaWindowForm(QWidget,Agenda):
    def __init__(self,parent= None, cita_id=None):
        super().__init__(parent)

        self.cita_id= cita_id
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.turnos_df = agenda.select_agenda()
        print("TURNOS DF DA; ", self.turnos_df)

        if self.turnos_df is not None and not self.turnos_df.empty:
            self.turnos_df['Fecha'] = pd.to_datetime(self.turnos_df['Fecha']).dt.date
            self.marcar_fechas()
        else:
            print("No hay turnos disponibles o hubo un error al cargar los datos.")

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)


    def marcar_fechas(self):
        formato = QTextCharFormat()
        formato.setBackground(QColor("lightblue"))
        formato.setForeground(QColor("black"))

        for fecha in self.turnos_df['Fecha'].unique():
            fecha_qdate = QDate.fromString(str(fecha), "yyyy-MM-dd")
            self.calendarWidget.setDateTextFormat(fecha_qdate, formato)