from PySide6.QtWidgets import QStyledItemDelegate, QPushButton, QWidget, QHBoxLayout
from PySide6.QtCore import Qt, QModelIndex

from controllers.add_productos import AddProductoForm
from controllers.edit_producto import EditWindowProductoForm
from controllers.details_productos import DetailWindowProductoForm

from database import productos

class ButtonDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(ButtonDelegate, self).__init__(parent)

    def paint(self, painter, option, index):
        if index.column() == 7:  # Columna donde estarán los botones
            widget = QWidget()
            layout = QHBoxLayout(widget)

            # Crear botones
            view_button = QPushButton("View")
            edit_button = QPushButton("Edit")
            delete_button = QPushButton("Delete")

            # Agregar botones al layout
            layout.addWidget(view_button)
            layout.addWidget(edit_button)
            layout.addWidget(delete_button)

            # Renderizar los botones
            widget.render(painter, option.rect.topLeft())
        else:
            super(ButtonDelegate, self).paint(painter, option, index)


    def get_producto_id_from_table(self, table, button):
        index = table.indexAt(button.parent().pos())
        producto_id = table.model().data(table.model().index(index.row(), 0))
        return producto_id

    def view_producto(self):
        button = self.sender()
        table = self.productos_table

        if button:
            producto_id = self.get_producto_id_from_table(table, button)
            self.open_detail_window_producto(producto_id)

    def edit_producto(self):
        button = self.sender()
        table = self.productos_table

        if button:
            producto_id = self.get_producto_id_from_table(table, button)
            self.open_edit_window_producto(producto_id)

    def delete_producto(self):
        button = self.sender()
        table = self.productos_table

        if button:
            producto_id = self.get_producto_id_from_table(table, button)
            if productos.delete(producto_id):
                self.set_table_data()