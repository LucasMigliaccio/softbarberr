import os
import PySide6.QtGui
from PySide6.QtWidgets import QWidget, QTableWidgetItem, QAbstractItemView, QHBoxLayout, QFrame

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi
from views import components


from controllers.add_cita import AddWindowForm
from controllers.edit_cita import EditWindowForm
from controllers.details_cita import DetailWindowForm
from controllers.horarios import ViewHorariosForm

from controllers.view_cliente import ViewClienteWindowForm
from controllers.view_empleado import ViewEmpleadoWindowForm
from controllers.view_productos import ViewProductoWindowForm
from database import citas

class MainWindowForm(QWidget, MainWindow):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.config_table()
        self.set_table_data()

        self.new_request_button.clicked.connect(self.open_add_window_cita)
        self.search_line_edit.returnPressed.connect(self.search)
        self.search_line_edit.textChanged.connect(self.restore_table_data)
        self.co_pushButton_pedidos.clicked.connect(self.open_horarios_window)

        self.op_pushButton_cliente.clicked.connect(self.open_clientes_view)
        self.co_pushButton_menu.clicked.connect(self.open_empleados_view)
        self.op_pushButton_menu.clicked.connect(self.open_productos_view)

    
    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def open_horarios_window(self):
        window= ViewHorariosForm(self)
        window.show()

    def open_add_window_cita(self):
        window= AddWindowForm(self)
        window.show()

    def open_edit_window_cita(self, cita_id):
        window= EditWindowForm(self, cita_id)
        window.show()

    def open_clientes_view(self):
        window = ViewClienteWindowForm(self)
        window.show() 

    def open_empleados_view(self):
        window = ViewEmpleadoWindowForm(self)
        window.show()

    def open_productos_view(self):
        window = ViewProductoWindowForm(self)
        window.show()    

    def config_table(self):
        column_label = ("ID","IMAGEN", "FECHA","CLIENTE(id)", "MONTO", "BARBERO(id)", "SERVICIOS", "TRANSACCIÓN","ESTADO","") 
        self.infopedidos_table.setColumnCount(len(column_label))
        self.infopedidos_table.setHorizontalHeaderLabels(column_label)
        self.infopedidos_table.setColumnWidth(1,200) #img
        self.infopedidos_table.setColumnWidth(2,120) #fecha
        self.infopedidos_table.setColumnWidth(3,120) #cliente cambiar id por innerjoin de nombre + apellido
        self.infopedidos_table.setColumnWidth(4,120) #monto
        self.infopedidos_table.setColumnWidth(5,120) #barbero cambiar id por innerjoin de nombre + apellido
        self.infopedidos_table.setColumnWidth(6,120) #servicios
        self.infopedidos_table.setColumnWidth(7,120) #metodo pago
        self.infopedidos_table.setColumnWidth(8,120) #estado
        self.infopedidos_table.setColumnWidth(9,110) #buttons
        self.infopedidos_table.verticalHeader().setDefaultSectionSize(150)
        self.infopedidos_table.setColumnHidden(0, True)
        self.infopedidos_table.setSelectionBehavior(QAbstractItemView.SelectRows)

            
    def populate_table(self, data):
        self.infopedidos_table.setRowCount(len(data))

        for(index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                if index_cell == 1:
                    self.infopedidos_table.setCellWidget(
                        index_row, index_cell, components.CitaImg(cell)
                    )
                else:
                    self.infopedidos_table.setItem(
                        index_row, index_cell, QTableWidgetItem(str(cell))
                    )
            self.infopedidos_table.setCellWidget(
                index_row,9, self.build_action_button()
            )
    
    def set_table_data(self):
        data = citas.select_all_join_prueba()
        self.populate_table(data)

    def restore_table_data(self):
        param = self.search_line_edit.text()
        if param == "":
            self.set_table_data()

    def search(self):
        param = self.search_line_edit.text()
        if param != "":
            data =citas.select_by_parameter(param)
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

        view_button.clicked.connect(self.view_cita)
        edit_button.clicked.connect(self.edit_cita)
        delete_button.clicked.connect(self.delete_cita)

        return buttons_frame
    
    def open_detail_window_cita(self,cita_id):
        window = DetailWindowForm(self, cita_id)
        window.show()

######################### DOOM #########################
        
    def view_cita(self):
        button = self.sender()
        table = self.infopedidos_table

        if button:
            cita_id = self.get_cita_id_from_table(table, button)
            self.open_detail_window_cita(cita_id)

    def edit_cita(self):
        button = self.sender()
        table = self.infopedidos_table

        if button:
            cita_id = self.get_cita_id_from_table(table, button)
            self.open_edit_window_cita(cita_id)

    def delete_cita(self):
        button = self.sender()
        table = self.infopedidos_table

        if button:
            cita_id = self.get_cita_id_from_table(table, button)
            data = citas.select_by_id(cita_id)

            # COMPARAR SI LA IMAGEN ESTA REPETIDA, SI ES ASI QUE NO LA BORRE #
            img_path_to_compare = data[8]
            fetched_images = citas.contrast_img(img_path_to_compare)
            
            if fetched_images and img_path_to_compare in (img[0] for img in fetched_images):
                if citas.delete(cita_id):
                    self.remove_img(data[8])
                    self.set_table_data()
            else:
                if citas.delete(cita_id):
                    self.set_table_data()
                    print("La imagen no está repetida en la base de datos, la cita se eliminará pero no la imagen")

    def remove_img(self, img_path):
        os.remove(img_path)

    def get_cita_id_from_table(self,table,button):
        row_index = table.indexAt(button.parent().pos()).row()
        cell_id_index= table.model().index(row_index,0)
        cita_id= table.model().data(cell_id_index)
        return cita_id
    
######################### DOOM #########################