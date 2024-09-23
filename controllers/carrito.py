from PySide6.QtWidgets import QWidget, QFileDialog, QAbstractItemView
from PySide6.QtCore import Qt
from views.carritocompras import CarritoCompras
from views.general_custom_ui import GeneralCustomUi
from database import productos

from models.carrito import CarritoTableModel
from models.productos import ProductosTableModel


class CarritoForm(QWidget, CarritoCompras):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)
        self.setWindowFlag(Qt.Window)
        self.productos_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        # Configura los modelos de tabla
        self.productos_model = ProductosTableModel(productos.select_all())
        self.carrito_model = CarritoTableModel([])  # Inicialmente vacío

        #almacena las filas
        self.filas_seleccionadas = []

        # Asocia los modelos a los QTableView
        self.productos_tableView.setModel(self.productos_model)
        self.carrito_tableView.setModel(self.carrito_model)

        # Conecta los botones a sus respectivas funciones
        self.add_pushButton.clicked.connect(self.agregar_al_carrito)
        self.add_edit_button.clicked.connect(self.agregar_producto)
        self.add_edit_button_2.clicked.connect(self.salir)

    def mousePressEvent(self, event):
        self.ui.mouse_press_event(event)

    def agregar_al_carrito(self):
        # Almacena varias filas seleccionadas 
        selected_indexes = self.productos_tableView.selectionModel().selectedRows()
        print ("++++++++++",selected_indexes)

        for index in selected_indexes:
            fila_completa = []
            for column in range(self.productos_model.columnCount()):
                cell_data = self.productos_model.data(self.productos_model.index(index.row(), column), Qt.DisplayRole)
                fila_completa.append(cell_data)

            cantidad = self.contador_spinBox.value()
            #if cantidad > 1: 
            self.carrito_model.add_to_cart(fila_completa, cantidad)
            self.filas_seleccionadas.append(fila_completa)


    def agregar_producto(self):

        table_view = self.carrito_tableView
        model = table_view.model()  # Obtener el modelo asociado al QTableView

        # Inicializar una lista vacía para almacenar los diccionarios de los productos
        productos_list = []

        # Índices de las columnas para nombre, cantidad y precio
        columna_nombre = 1
        columna_cantidad = 2
        columna_precio = 3

        # Recorrer todas las filas de la tabla
        for row in range(model.rowCount()):
            # Obtener los datos de las columnas que nos interesan
            nombre = model.index(row, columna_nombre).data()
            cantidad = model.index(row, columna_cantidad).data()
            precio = model.index(row, columna_precio).data()

            # Si la cantidad es mayor a 1, multiplicar el precio por la cantidad
            if cantidad > 1:
                precio_total = precio * cantidad
            else:
                precio_total = precio

            # Crear un diccionario con los datos del producto
            producto = {
                "Nombre": nombre,
                "Cantidad": cantidad,
                "Precio Total": precio_total
            }

            # Agregar el diccionario a la lista de productos
            productos_list.append(producto)

        # Ahora `productos_list` tiene todos los productos con sus respectivos datos
        #print(productos_list, "++++\n")
        for vuelta in productos_list:
            print(vuelta)
        return productos_list


    def salir(self):
        self.close()
