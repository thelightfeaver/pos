
# from src.components.datagrid import QDataGrid

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QTableWidget, QTableWidgetItem, QLineEdit
class QProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._build()

    def _build(self):
        # add lables
        self.layout.addWidget(QLabel('Products'))

        # add field name
        self.layout.addWidget(QLabel("Name"))
        self.ql_name = QLineEdit()
        self.layout.addWidget(self.ql_name)

        # add field description
        self.layout.addWidget(QLabel("Description"))
        self.ql_description = QLineEdit()
        self.layout.addWidget(self.ql_description)

        # add field price details
        self.layout.addWidget(QLabel("Price Details"))
        self.ql_details = QLineEdit()
        self.layout.addWidget(self.ql_details)

        # add field price
        self.layout.addWidget(QLabel("Price Sale"))
        self.ql_price = QLineEdit()
        self.layout.addWidget(self.ql_price)

        # add field stock
        self.layout.addWidget(QLabel("Stock"))
        self.ql_stock = QLineEdit()
        self.layout.addWidget(self.ql_stock)



        
        