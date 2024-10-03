from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton



class QMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self._build()



    def _build(self):
        self.side_layout = QVBoxLayout()
        self.side_layout.addWidget(QLabel('Menu'))
        self.side_layout.addWidget(QPushButton('Home'))
        self.side_layout.addWidget(QPushButton('Products'))
        self.side_layout.addWidget(QPushButton('Orders'))
        self.side_layout.addWidget(QPushButton('Sell'))
        self.layout.addLayout(self.side_layout)
        