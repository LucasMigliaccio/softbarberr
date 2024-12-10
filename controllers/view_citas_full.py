import pandas as pd
from PySide6.QtWidgets import QWidget, QVBoxLayout, QAbstractItemView
from PySide6.QtCore import Qt

from controllers.edit_cita import EditWindowForm

from views.general_custom_ui import GeneralCustomUi
from views.view_citas_full import ViewCitasFull

from models.citas import CitasTableModel

from database import citas

#from models.producto import


class ViewCitasFullForm(QWidget, ViewCitasFull):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)

        self.marcas_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.citas_model = CitasTableModel(citas.select_all_join_tableview_complete())

        self.marcas_table.setModel(self.citas_model)

        self.delete_pushButton.clicked.connect(self.delete_selected)
        self.edit_pushButton.clicked.connect(self.edit_selected)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def delete_selected(self):
        # Obtener la fila seleccionada
        selected_indexes = self.marcas_table.selectionModel().selectedRows()
        
        if not selected_indexes:
            print("No se ha seleccionado ninguna fila.")
            return

        # Suponemos que la columna 0 es donde está el ID
        selected_row = selected_indexes[0].row()
        cita_id = self.citas_model.data(self.citas_model.index(selected_row, 0), Qt.DisplayRole)

        # Confirmar o realizar la eliminación
        if citas.delete(cita_id):  # Llama a la función SQL con el ID
            print(f"Cita con ID {cita_id} eliminada exitosamente.")
            # Actualizar la tabla después de la eliminación
            self.citas_model._data.pop(selected_row)
            self.citas_model.layoutChanged.emit()
        else:
            print(f"Error al intentar eliminar la cita con ID {cita_id}.")

    def edit_selected(self):
        selected_indexes = self.marcas_table.selectionModel().selectedRows()
        if not selected_indexes:
            print("No se ha seleccionado ninguna fila.")
            return

        selected_row = selected_indexes[0].row()
        cita_id = self.citas_model.data(self.citas_model.index(selected_row, 0), Qt.DisplayRole)

        edit_window = EditWindowForm(parent=self, cita_id=cita_id, source_view=self.marcas_table)
        edit_window.edit_finished.connect(self.refresh_table)
        edit_window.show()
        

    def open_edit_window_cita(self, cita_id):
        window= EditWindowForm(self, cita_id)
        window.show()

    def refresh_table(self):
        self.citas_model.refresh_data()
        print("Tabla actualizada después de editar la cita.")
