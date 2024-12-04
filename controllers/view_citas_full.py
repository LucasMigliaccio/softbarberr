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
        # Obtener la fila seleccionada
        selected_indexes = self.marcas_table.selectionModel().selectedRows()

        if not selected_indexes:
            print("No se ha seleccionado ninguna fila.")
            return

        # Obtener la fila seleccionada y su ID
        selected_row = selected_indexes[0].row()
        cita_id = self.citas_model.data(self.citas_model.index(selected_row, 0), Qt.DisplayRole)

        try:
            print("Entrando a editar cita...")
            # Abre la ventana de edición y pasa la ID de la cita seleccionada
            self.open_edit_window_cita(cita_id, selected_row)
        except Exception as e:
            print(f"El error lo provoca: {e}")

    def open_edit_window_cita(self, cita_id, selected_row):
        # Crear la ventana de edición
        window = EditWindowForm(self, cita_id)

        # Conectar una señal personalizada para actualizar el modelo después de editar
        window.data_updated.connect(lambda new_data: self.update_row_data(selected_row, new_data))

        # Mostrar la ventana de edición
        window.show()

    def update_row_data(self, row, new_data):
        # Actualiza los datos en el modelo
        self.citas_model._data[row] = new_data
        # Emite la señal para refrescar la tabla
        self.citas_model.layoutChanged.emit()
        print(f"Datos actualizados para la fila {row}: {new_data}")
