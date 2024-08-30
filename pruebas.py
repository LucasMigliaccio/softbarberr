from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableView, QApplication
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex
from views.carritocompras import CarritoCompras
from database import productos  # Asumiendo que usas un ORM o una función para obtener datos

class CarritoComprasWindow(QMainWindow, CarritoCompras):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # Configurar la tabla de productos
        self.model_productos = ProductosTableModel(productos.select_all())
        self.productos_tableView.setModel(self.model_productos)
        
        # Configurar la tabla del carrito
        self.model_carrito = CarritoTableModel([])
        self.carrito_tableView.setModel(self.model_carrito)
        
        # Conectar botones
        self.add_pushButton.clicked.connect(self.agregar_al_carrito)
        self.add_edit_button.clicked.connect(self.procesar_compra)
        self.add_edit_button_2.clicked.connect(self.salir)

    def agregar_al_carrito(self):
        selected = self.productos_tableView.selectionModel().selectedIndexes()
        if selected:
            row = selected[0].row()
            producto = self.model_productos.get_producto(row)
            cantidad = self.contador_spinBox.value()
            if cantidad > 0:
                self.model_carrito.agregar_producto(producto, cantidad)
            else:
                QMessageBox.warning(self, "Cantidad Inválida", "La cantidad debe ser mayor a cero.")
        else:
            QMessageBox.warning(self, "Selección Inválida", "Seleccione un producto para agregar.")

    def procesar_compra(self):
        # Implementa la lógica para procesar la compra
        pass

    def salir(self):
        self.close()

class ProductosTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data or []
        self._headers = ["ProductoID", "NombreDelProducto", "Descripcion", "Precio", "CantidadEnStock", "Codigo", "CodigoDeBarra"]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
            else:
                return section + 1
        return None

    def get_producto(self, row):
        return self._data[row]

class CarritoTableModel(QAbstractTableModel):
    def __init__(self, data=None):
        super().__init__()
        self._data = data
        self._headers = ["Producto", "Cantidad", "Precio Unitario", "Total"]

    def rowCount(self, parent=QModelIndex()):
        return len(self._data)

    def columnCount(self, parent=QModelIndex()):
        return len(self._headers)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]
        return None

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self._headers[section]
            else:
                return section + 1
        return None

    def agregar_producto(self, producto, cantidad):
        total = producto["Precio"] * cantidad
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append([producto["NombreDelProducto"], cantidad, producto["Precio"], total])
        self.endInsertRows()

if __name__ == "__main__":
    app = QApplication([])
    window = CarritoComprasWindow()
    window.show()
    app.exec()
