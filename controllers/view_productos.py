import os
from PySide6.QtWidgets import QWidget, QTabWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame
from PySide6.QtCore import Qt

from views.view_productos import ViewProducto
from views.general_custom_ui import GeneralCustomUi
from views import components
from views.add_producto import AddEditProducto

from controllers.add_productos import AddProductoForm
from controllers.edit_producto import EditWindowProductoForm
from controllers.details_productos import DetailWindowProductoForm
from controllers.adjust_stock import AdjustStockProductoForm

from database import productos

class ViewProductoWindowForm(QWidget,ViewProducto):

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
        window= AddProductoForm(self)
        window.show()

    def config_table(self):
        column_label= ("ID", "NOMBRE", "DESCRIPCION", "PRECIO", "STOCK", "CODIGO", "CODEBAR","CATEGORIA", "")
        self.productos_table.setColumnCount(len(column_label))
        self.productos_table.setHorizontalHeaderLabels(column_label)
        self.productos_table.setColumnWidth(1,100) #nombre
        self.productos_table.setColumnWidth(2,100) #descripcion
        self.productos_table.setColumnWidth(3,100) #precio
        self.productos_table.setColumnWidth(4,100) #stock
        self.productos_table.setColumnWidth(5,100) #codigo
        self.productos_table.setColumnWidth(6,100) #codigo_barra
        self.productos_table.setColumnWidth(7,100) #categoria
        self.productos_table.setColumnWidth(8,200) #buttons
        self.productos_table.verticalHeader().setDefaultSectionSize(150)
        self.productos_table.setColumnHidden(0, True)
        self.productos_table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def populate_table(self, data):
        

        self.productos_table.setRowCount(len(data))

        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.productos_table.setItem(
                    index_row, index_cell, QTableWidgetItem(str(cell))
                )
            #buttons en la tabla
            self.productos_table.setCellWidget(
            index_row,8, self.build_action_button()
            )
    

    def set_table_data(self):
        data = productos.select_all()
        self.populate_table(data)

    def restore_table_data(self):
        param = self.search_line_edit.text()
        if param == "":
            self.set_table_data()

    def search(self):
        param = self.search_line_edit.text()
        if param != "":
            data =productos.select_by_parameter(param)
            self.populate_table(data)
    
    def build_action_button(self):
        stock_button=components.Butonn("stock","#FEE43D")
        view_button=components.Butonn("view","#17A288")
        edit_button=components.Butonn("edit","#007BFF")
        delete_button=components.Butonn("delete","#DC3545")

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(stock_button)
        buttons_layout.addWidget(view_button)
        buttons_layout.addWidget(edit_button)
        buttons_layout.addWidget(delete_button)

        buttons_frame =QFrame()
        buttons_frame.setLayout(buttons_layout)

        stock_button.clicked.connect(self.adjust_stock_producto)
        view_button.clicked.connect(self.view_producto)
        edit_button.clicked.connect(self.edit_producto)
        delete_button.clicked.connect(self.delete_producto)

        return buttons_frame
    
    def open_detail_window_producto(self, producto_id):
        window = DetailWindowProductoForm(self, producto_id)
        window.show()
    
    def open_edit_window_producto(self, producto_id):
        window= EditWindowProductoForm(self, producto_id)
        window.show()

    def open_addjust_stock_window_producto(self, producto_id):
        window= AdjustStockProductoForm(self, producto_id)
        window.show()

    def get_producto_id_from_table(self,table,button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index= table.model().index(row_index,0)
        producto_id= table.model().data(cell_id_index)
        return producto_id

    def view_producto(self):
        button = self.sender()
        table = self.productos_table

        if button:
            producto_id = self.get_producto_id_from_table(table, button)
            self.open_detail_window_producto(producto_id)

    def edit_producto(self):
        button = self.sender()
        table = self.productos_table

        if button:
            producto_id = self.get_producto_id_from_table(table, button)
            self.open_edit_window_producto(producto_id)

    def adjust_stock_producto(self):
        button = self.sender()
        table = self.productos_table

        if button:
            producto_id = self.get_producto_id_from_table(table, button)
            self.open_addjust_stock_window_producto(producto_id)

    def delete_producto(self):
        button = self.sender()
        table = self.productos_table

        if button:
            producto_id = self.get_producto_id_from_table(table, button)
            data = productos.select_by_id(producto_id)

            if productos.delete(producto_id):
                print("+++++++++++++ PREELIMINADO +++++++++++++")
                self.set_table_data()
                print("+++++++++++++ ELIMINADO +++++++++++++")