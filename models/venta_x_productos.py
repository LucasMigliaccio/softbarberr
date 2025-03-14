from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex
import pandas as pd

class VentaProductosTableModel(QAbstractTableModel):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._data = data.copy() if isinstance(data, pd.DataFrame) else pd.DataFrame()

        self._headers = [
        "ServiciosProgramados", "Cantidad"]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]
            if orientation == Qt.Vertical:
                return section + 1
        return None

    def get_cita(self, row):
        if 0 <= row < len(self._data):
            return self._data.iloc[row].to_dict()
        return None

    def update_data(self, new_data):
        self.beginResetModel()
        self._data = new_data.copy() if isinstance(new_data, pd.DataFrame) else pd.DataFrame()
        self.endResetModel()