from PySide6.QtWidgets import QStyledItemDelegate
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from io import BytesIO
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class GraficoDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paint(self, painter, option, index):
        if not index.isValid():
            return

        # Obtener los datos del gráfico desde el modelo
        data = index.model().data(index, Qt.DisplayRole)
        if not data:
            return

        # Crear el gráfico con Matplotlib
        fig, ax = plt.subplots(figsize=(3, 2))
        ax.bar(data["ServiciosProgramados"], data["Cantidad"], color='skyblue')
        ax.axis('off')

        # Convertir el gráfico a QPixmap
        buf = BytesIO()
        fig.savefig(buf, format='png')
        plt.close(fig)
        pixmap = QPixmap()
        pixmap.loadFromData(buf.getvalue())

        # Dibujar el gráfico dentro de la celda
        painter.drawPixmap(option.rect, pixmap)
