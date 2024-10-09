
from src.components.datagrid import QDataGrid

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem

class QProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._build()

    def _build(self):
        pass


