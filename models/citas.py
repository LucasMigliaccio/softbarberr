from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
from database import citas

class CitasTableModel(QAbstractTableModel):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._data = data or []
        self._headers = ["ID","IMAGEN", "FECHA","CLIENTE(id)", "MONTO", "BARBERO(id)", "SERVICIOS", "TRANSACCIÓN","ESTADO"]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            if orientation == Qt.Vertical:
                return section + 1
        return None

    def get_citas(self, row):
        return self._data[row]
    
    def refresh_data(self):
        self._data = citas.select_all_join_tableview_complete()
        self.layoutChanged.emit()

"""
    def add_citas(self, citas):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append(citas)
        self.endInsertRows()

    def remove_citas(self, row):
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._data[row]
        self.endRemoveRows()
"""


