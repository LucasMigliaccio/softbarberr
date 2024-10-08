import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTableView, QPushButton, QVBoxLayout, QWidget, 
    QHBoxLayout, QLabel, QSpinBox, QAbstractItemView, QMessageBox
)
from PySide6.QtCore import QAbstractTableModel, Qt


class ProductTableModel(QAbstractTableModel):
    def __init__(self, products):
        super().__init__()
        self._products = products

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._products[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._products)

    def columnCount(self, index):
        return len(self._products[0])

class CartTableModel(QAbstractTableModel):
    def __init__(self, cart_items):
        super().__init__()
        self._cart_items = cart_items

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._cart_items[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._cart_items)

    def columnCount(self, index):
        if self._cart_items:
            return len(self._cart_items[0])
        return 0  # Si la lista está vacía, no hay columnas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Carrito de Compras")

        # Definir productos (ID, Nombre, Precio, Stock)
        self.products = [
            [1, "Producto A", 10.0, 5],
            [2, "Producto B", 15.0, 3],
            [3, "Producto C", 7.5, 8],
        ]

        # Carrito vacío
        self.cart = []

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Tabla de productos
        self.product_table = QTableView()
        self.product_model = ProductTableModel(self.products)
        self.product_table.setModel(self.product_model)
        self.product_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        layout.addWidget(self.product_table)

        # Controles para agregar al carrito
        self.quantity_label = QLabel("Cantidad:")
        self.quantity_spinbox = QSpinBox()
        self.quantity_spinbox.setRange(1, 100)
        self.add_button = QPushButton("Agregar al Carrito")
        self.add_button.clicked.connect(self.add_to_cart)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.quantity_label)
        h_layout.addWidget(self.quantity_spinbox)
        h_layout.addWidget(self.add_button)
        layout.addLayout(h_layout)

        # Tabla del carrito
        self.cart_table = QTableView()
        self.cart_model = CartTableModel(self.cart)
        self.cart_table.setModel(self.cart_model)
        layout.addWidget(self.cart_table)

        # Configuración final de la ventana
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def add_to_cart(self):
        selected = self.product_table.selectionModel().selectedIndexes()
        if selected:
            row = selected[0].row()
            product_id = self.products[row][0]
            product_name = self.products[row][1]
            product_price = self.products[row][2]
            stock = self.products[row][3]
            quantity = self.quantity_spinbox.value()

            if stock >= quantity:
                self.products[row][3] -= quantity

                # Verificar si el producto ya está en el carrito
                for item in self.cart:
                    if item[0] == product_id:
                        item[2] += quantity
                        break
                else:
                    self.cart.append([product_id, product_name, quantity, product_price * quantity])

                # Actualizar las tablas
                self.product_model.layoutChanged.emit()
                self.cart_model.layoutChanged.emit()

                QMessageBox.information(self, "Éxito", f"{quantity} unidades de '{product_name}' añadidas al carrito.")
            else:
                QMessageBox.warning(self, "Error", "Stock insuficiente.")
        else:
            QMessageBox.warning(self, "Error", "Seleccione un producto.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
