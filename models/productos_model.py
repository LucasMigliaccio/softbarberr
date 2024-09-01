from PySide6.QtCore import QAbstractTableModel, Qt

class ProductosTableModel(QAbstractTableModel):
    def __init__(self, data):
        super(ProductosTableModel, self).__init__()
        self._data = data

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        if self._data:
            return len(self._data[0])
        return 0

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        headers = ["ID", "NOMBRE", "DESCRIPCION", "PRECIO", "STOCK", "CODIGO", "CODEBAR", ""]
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return headers[section]
            else:
                return section + 1
        return None
