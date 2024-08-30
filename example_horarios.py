import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton, QHeaderView

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calendario Semanal de Horarios")
        self.resize(600, 400)

        self.layout = QVBoxLayout(self)

        # Etiqueta para el nombre del empleado
        self.nombre_label = QLabel("Nombre del Empleado:")
        self.layout.addWidget(self.nombre_label)

        # Tabla para mostrar el calendario semanal
        self.table = QTableWidget()
        self.table.setRowCount(6)  # 7 filas para los días de la semana len empleados
        self.table.setColumnCount(7)  # 24 columnas para las horas del día
        self.table.setHorizontalHeaderLabels(["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"])  # Encabezados de las columnas
        self.table.setVerticalHeaderLabels(["Juan", "María", "Pedro", "Ana", "Carlos", "Laura"])  # Encabezados de las filas
        self.layout.addWidget(self.table)

        # Botón para guardar los horarios
        self.guardar_button = QPushButton("Guardar Horarios")
        self.guardar_button.clicked.connect(self.guardar_horarios)
        self.layout.addWidget(self.guardar_button)

    def guardar_horarios(self):
        # Ejemplo de cómo obtener y guardar los horarios
        for row in range(7):
            for col in range(24):
                item = self.table.item(row, col)
                if item:
                    print(f"Día: {row + 1}, Hora: {col}, Horario: {item.text()}")
                    # Aquí podrías guardar el horario en una base de datos o archivo

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())