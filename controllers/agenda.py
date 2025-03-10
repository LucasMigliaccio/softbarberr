from PySide6.QtCore import Qt,QDate
from PySide6.QtGui import QPixmap,QTextCharFormat, QColor,  QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow, QCalendarWidget, QVBoxLayout, QWidget,QHeaderView 

from views.agenda import Agenda
from views.general_custom_ui import GeneralCustomUi

from models.agenda import CitasTableModel
from database import agenda
import pandas as pd

class AgendaWindowForm(QWidget, Agenda):
    def __init__(self, parent=None, cita_id=None):
        super().__init__(parent)

        self.cita_id = cita_id
        
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.turnos_df = agenda.select_agenda()
        #rint("TURNOS DF DA; ", self.turnos_df)

        if isinstance(self.turnos_df, pd.DataFrame) and not self.turnos_df.empty:
            self.turnos_df['Fecha'] = pd.to_datetime(self.turnos_df['Fecha'], errors='coerce').dt.date
            self.marcar_fechas()
        else:
            print("No hay turnos disponibles o hubo un error al cargar los datos.")

        
        self.pendientes_model = None  # Inicializar vacío
        self.init_table_model()

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def marcar_fechas(self):
        formato_completado = QTextCharFormat()
        formato_completado.setBackground(QColor("lightblue"))
        formato_completado.setForeground(QColor("black"))

        formato_pendiente = QTextCharFormat()
        formato_pendiente.setBackground(QColor("lightcoral"))
        formato_pendiente.setForeground(QColor("white"))

        for _, fila in self.turnos_df.iterrows():
            fecha_qdate = QDate.fromString(str(fila['Fecha']), "yyyy-MM-dd")
            if fila['Estado'] == 'pendiente':
                self.calendarWidget.setDateTextFormat(fecha_qdate, formato_pendiente)
            else:
                self.calendarWidget.setDateTextFormat(fecha_qdate, formato_completado)

    def total_pendientes(self):
        try:
            pendiente = agenda.select_citas_pendientes()

            if isinstance(pendiente, pd.DataFrame) and not pendiente.empty:
                pendiente['Fecha'] = pd.to_datetime(pendiente['Fecha'], errors='coerce').dt.date
                model = CitasTableModel(pendiente)
                self.pendientes_tableView.setModel(model)
            else:
                print("No hay citas pendientes.")
        except Exception as e:
            print(f"Error al cargar citas pendientes: {e}")


    def init_table_model(self):
        """Inicializa el modelo de datos y lo configura en la tabla."""
        try:
            # Obtener los datos pendientes
            data_pendientes = agenda.select_citas_pendientes()
            df_pendientes = pd.DataFrame(data_pendientes, columns=["CitaID", "Fecha", "Hora", "ClienteNombre", "Monto", "Seña", "ServiciosProgramados", "MetodoPago", "Estado"])

            # Asegúrate de que las columnas numéricas sean tratadas correctamente
            numeric_columns = ["Monto", "Seña"]
            for col in numeric_columns:
                if col in df_pendientes.columns:
                    df_pendientes[col] = pd.to_numeric(df_pendientes[col], errors='coerce').abs()

            self.pendientes_model = CitasTableModel(df_pendientes)
            self.pendientes_tableView.setModel(self.pendientes_model)

        except Exception as e:
            print(f"Error al cargar datos: {e}")
            empty_model = CitasTableModel(pd.DataFrame())
            self.pendientes_tableView.setModel(empty_model)
