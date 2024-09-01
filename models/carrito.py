from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex

class CarritoTableModel(QAbstractTableModel):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._headers = ["ID", "Producto", "Cantidad", "Precio", "Total"]  # Definir los nombres de las columnas
        self._carrito = data or []  # Cambié 'self.data' a 'self._carrito' para evitar confusiones

    def rowCount(self, parent=QModelIndex()):
        return len(self._carrito)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)  # Devuelve el número de columnas basado en los headers

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            return self._carrito[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._headers[section]  # Devuelve el nombre de la columna
            else:
                return str(section + 1)  # Devuelve el número de fila
        return None

    def add_to_cart(self, product, quantity):
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        total_price = product[3] * quantity  # Asume que el precio está en la columna 3
        self._carrito.append([product[0], product[1], quantity, product[3], total_price])
        self.endInsertRows()

    def remove_from_cart(self, row):
        self.beginRemoveRows(QModelIndex(), row, row)
        del self._carrito[row]
        self.endRemoveRows()

    def clear_cart(self):
        self.beginResetModel()
        self._carrito.clear()
        self.endResetModel()

    def get_cart_items(self):
        return self._carrito
