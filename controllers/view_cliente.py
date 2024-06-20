import os
from PySide6.QtWidgets import QWidget, QTabWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from views.view_clientes import ViewCliente
from views.general_custom_ui import GeneralCustomUi
from views import components
from views.add_edit_cliente import AddEditCliente

from controllers.add_cliente import AddClienteForm
from controllers.edit_cliente import EditWindowClienteForm
from controllers.details_cliente import DetailWindowClienteForm
from database import clientes

class ViewClienteWindowForm(QWidget,ViewCliente):

    def __init__(self, parent = None):
        super().__init__(parent)

        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.config_table()
        self.set_table_data()

        self.new_request_button_cliente.clicked.connect(self.open_add_window_cliente)
        self.search_line_edit.returnPressed.connect(self.search)
        self.search_line_edit.textChanged.connect(self.restore_table_data)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def open_add_window_cliente(self):
        window= AddClienteForm(self)
        window.show()

    def config_table(self):
        column_label= ("ID", "NOMBRE", "TELEFONO", "CORREO", "DIRECCIÓN", "")
        self.clientes_table.setColumnCount(len(column_label))
        self.clientes_table.setHorizontalHeaderLabels(column_label)
        self.clientes_table.setColumnWidth(1,100) #nombre
        self.clientes_table.setColumnWidth(2,100) #telefono
        self.clientes_table.setColumnWidth(3,100) #correo
        self.clientes_table.setColumnWidth(4,100) #direccion
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
            index_row,5, self.build_action_button()
            )
    

    def set_table_data(self):
        data = clientes.select_all()
        self.populate_table(data)

    def restore_table_data(self):
        param = self.search_line_edit.text()
        if param == "":
            self.set_table_data()

    def search(self):
        param = self.search_line_edit.text()
        if param != "":
            data =clientes.select_by_parameter(param)
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

        view_button.clicked.connect(self.view_cliente)
        edit_button.clicked.connect(self.edit_cliente)
        delete_button.clicked.connect(self.delete_cliente)

        return buttons_frame
    
    def open_detail_window_cliente(self, cliente_id):
        window = DetailWindowClienteForm(self, cliente_id)
        window.show()
    
    def open_edit_window_cliente(self, cita_id):
        window= EditWindowClienteForm(self, cita_id)
        window.show()

    def get_cliente_id_from_table(self,table,button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index= table.model().index(row_index,0)
        cliente_id= table.model().data(cell_id_index)
        return cliente_id

    def view_cliente(self):
        button = self.sender()
        table = self.clientes_table

        if button:
            cliente_id = self.get_cliente_id_from_table(table, button)
            self.open_detail_window_cliente(cliente_id)

    def edit_cliente(self):
        button = self.sender()
        table = self.clientes_table

        if button:
            cliente_id = self.get_cliente_id_from_table(table, button)
            self.open_edit_window_cliente(cliente_id)

    def delete_cliente(self):
        button = self.sender()
        table = self.clientes_table

        if button:
            cliente_id = self.get_cliente_id_from_table(table, button)
            #data = clientes.select_by_id(cliente_id)

            if clientes.delete(cliente_id):
                print("+++++++++++++ PREELIMINADO +++++++++++++")
                self.set_table_data()
                print("+++++++++++++ ELIMINADO +++++++++++++")