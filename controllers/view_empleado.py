import os
from PySide6.QtWidgets import QWidget, QTabWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from views.view_empleados import ViewEmpleado
from views.general_custom_ui import GeneralCustomUi
from views import components
from views.add_barbero import AddEditEmpleado

from controllers.add_empleado import AddEmpleadoForm
from controllers.edit_empleado import EditWindowEmpleadoForm
from controllers.details_empleado import DetailWindowEmpleadoForm

from database import empleados

class ViewEmpleadoWindowForm(QWidget,ViewEmpleado):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.config_table()
        self.set_table_data()

        self.new_request_button_cliente.clicked.connect(self.open_add_window_empleado)
        self.search_line_edit.returnPressed.connect(self.search)
        self.search_line_edit.textChanged.connect(self.restore_table_data)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def open_add_window_empleado(self):
        window= AddEmpleadoForm(self)
        window.show()

    def config_table(self):
        column_label= ("ID", "NOMBRE", "TELEFONO", "CORREO", "DIRECCIÓN", "ESPECIALIDAD", "")
        self.clientes_table.setColumnCount(len(column_label))
        self.clientes_table.setHorizontalHeaderLabels(column_label)
        self.clientes_table.setColumnWidth(1,100) #nombre
        self.clientes_table.setColumnWidth(2,100) #telefono
        self.clientes_table.setColumnWidth(3,100) #correo
        self.clientes_table.setColumnWidth(4,100) #direccion
        self.clientes_table.setColumnWidth(5,100) #especialidad
        self.clientes_table.verticalHeader().setDefaultSectionSize(150)
        self.clientes_table.setColumnHidden(0, True)
        self.clientes_table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def populate_table(self, data):
        

        self.clientes_table.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.clientes_table.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell))
                )
            #buttons en la tabla
            self.clientes_table.setCellWidget(
            index_row,6, self.build_action_button()
            )
    

    def set_table_data(self):
        data = empleados.select_all()
        self.populate_table(data)

    def restore_table_data(self):
        param = self.search_line_edit.text()
        if param == "":
            self.set_table_data()

    def search(self):
        param = self.search_line_edit.text()
        if param != "":
            data =empleados.select_by_parameter(param)
            self.populate_table(data)
    
    def build_action_button(self):
        view_button=components.Butonn("view","#17A288")
        edit_button=components.Butonn("edit","#007BFF")
        delete_button=components.Butonn("delete","#DC3545")

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame =QFrame()
        buttons_frame.setLayout(buttons_layout)

        view_button.clicked.connect(self.view_empleado)
        edit_button.clicked.connect(self.edit_empleado)
        delete_button.clicked.connect(self.delete_empleado)

        return buttons_frame
    
    def open_detail_window_empleado(self, empleado_id):
        window = DetailWindowEmpleadoForm(self, empleado_id)
        window.show()
    
    def open_edit_window_empleado(self, cita_id):
        window= EditWindowEmpleadoForm(self, cita_id)
        window.show()

    def get_empleado_id_from_table(self,table,button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index= table.model().index(row_index,0)
        empleado_id= table.model().data(cell_id_index)
        return empleado_id

    def view_empleado(self):
        button = self.sender()
        table = self.clientes_table

        if button:
            empleado_id = self.get_empleado_id_from_table(table, button)
            self.open_detail_window_empleado(empleado_id)

    def edit_empleado(self):
        button = self.sender()
        table = self.clientes_table

        if button:
            empleado_id = self.get_empleado_id_from_table(table, button)
            self.open_edit_window_empleado(empleado_id)

    def delete_empleado(self):
        button = self.sender()
        table = self.clientes_table

        if button:
            empleado_id = self.get_empleado_id_from_table(table, button)
            data = empleados.select_by_id(empleado_id)

            if empleados.delete(empleado_id):
                print("+++++++++++++ PREELIMINADO +++++++++++++")
                self.set_table_data()
                print("+++++++++++++ ELIMINADO +++++++++++++")