from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import Qt, QDateTime


from ui_files.prueba_combobox import PruebaCB
from views.general_custom_ui import GeneralCustomUi

from database import empleados

data_cb= empleados.select_barber_cb_nombre()
lista_formateada = [f"{id} ) {nombre}" for id, nombre in data_cb]
print (tuple(lista_formateada))