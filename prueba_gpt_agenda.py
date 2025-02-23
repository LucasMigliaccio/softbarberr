import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QWidget
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtCore import QDate
from database import agenda

class CalendarTurnos(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Agenda de Turnos")
        self.setGeometry(100, 100, 400, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout(self.central_widget)

        # Widget del calendario
        self.calendar = QCalendarWidget()
        self.layout.addWidget(self.calendar)

        self.turnos_df = agenda.select_agenda()
        print("TURNOS DF DA; ", self.turnos_df)

        if self.turnos_df is not None and not self.turnos_df.empty:
            self.turnos_df['Fecha'] = pd.to_datetime(self.turnos_df['Fecha']).dt.date
            self.marcar_fechas()
        else:
            print("No hay turnos disponibles o hubo un error al cargar los datos.")


    def marcar_fechas(self):
        formato = QTextCharFormat()
        formato.setBackground(QColor("lightblue"))
        formato.setForeground(QColor("black"))

        for fecha in self.turnos_df['Fecha'].unique():
            fecha_qdate = QDate.fromString(str(fecha), "yyyy-MM-dd")
            self.calendar.setDateTextFormat(fecha_qdate, formato)

if __name__ == "__main__":
    app = QApplication([])
    ventana = CalendarTurnos()
    ventana.show()
    app.exec()