from PySide6.QtWidgets import QWidget, QTableWidgetItem
import os
from PySide6.QtWidgets import QWidget, QTabWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QAbstractItemView
from PySide6.QtCore import QDate, Qt
import calendar

from views.horarios import ViewHorarios
from views.general_custom_ui import GeneralCustomUi
from views import components

from database import horarios

class ViewHorariosForm(QWidget,ViewHorarios):
    
    def __init__(self, parent= None):
        super().__init__(parent)

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.config_tables()

    
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def config_table(self):
        column_label= ("","LUNES", "MARTES", "MIÉRCOLES", "JUEVES", "VIERNES", "SÁBADO", "DOMINGO", "")
        self.horarios_table.setColumnCount(len(column_label))
        self.horarios_table.setHorizontalHeaderLabels(column_label)
        self.horarios_table.setColumnWidth(0,100) 
        self.horarios_table.setColumnWidth(1,100) 
        self.horarios_table.setColumnWidth(2,100) 
        self.horarios_table.setColumnWidth(3,100) 
        self.horarios_table.setColumnWidth(4,100)
        self.horarios_table.setColumnWidth(5,100)
        self.horarios_table.setColumnWidth(6,100)
        self.horarios_table.verticalHeader().setDefaultSectionSize(150)
        self.horarios_table.setSelectionBehavior(QAbstractItemView.SelectRows)


    def config_tables(self):
        # Obtener el día actual
        current_date = QDate.currentDate()
        
        # Obtener el primer día de la semana actual LUNESS
        first_day_of_week = current_date.addDays(-current_date.dayOfWeek() + 1)
        
        # Crear la lista de nombres de columnas
        column_labels = [""]
        for i in range(7):
            # Nombre del día de la semana
            day_name = calendar.day_name[(first_day_of_week.addDays(i)).dayOfWeek() - 1].upper()
            # Fecha en formato "DIA DD"
            date_str = (first_day_of_week.addDays(i)).toString("ddd dd")
            # Agrega el nombre del día y la fecha a la lista de columnas
            column_labels.append(f" {day_name} {date_str}")
        
        column_labels.append("")
        
        # Configura las columnas en la tabla
        self.horarios_table.setColumnCount(len(column_labels))
        self.horarios_table.setHorizontalHeaderLabels(column_labels)
        for i in range(len(column_labels)):
            self.horarios_table.setColumnWidth(i, 100)
        self.horarios_table.verticalHeader().setDefaultSectionSize(150)
        self.horarios_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        
        # Posiciona en la columna correspondiente al día actual
        day_index = current_date.dayOfWeek()
        self.horarios_table.setCurrentCell(0, day_index)

    def set_table_data(self):
        data = horarios.select_all()
        self.populate_table(data)

    def populate_table(self, data):
        

        self.horarios_table.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.horarios_table.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell))
                )
            #buttons en la tabla
            self.horarios_table.setCellWidget(
            index_row,6, self.build_action_button()
            )
    
    def build_action_button(self):
        edit_button=components.Butonn("edit","#007BFF")
        delete_button=components.Butonn("delete","#DC3545")

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame =QFrame()
        buttons_frame.setLayout(buttons_layout)

        #edit_button.clicked.connect(self.edit_cliente)
        #delete_button.clicked.connect(self.delete_cliente)

        return buttons_frame