from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QStackedLayout

class QMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        self._build()

    def _build(self):
        # Add side layout
        self.side_layout = QStackedLayout()
        self.side_layout.addWidget(QLabel('Menu'))
        
        # Add buttons
        self.side_layout.addWidget(QPushButton('Home'))
        self.side_layout.addWidget(QPushButton('Products'))
        self.side_layout.addWidget(QPushButton('Orders'))
        self.side_layout.addWidget(QPushButton('Sell'))
        
        # Add side layout to the main layout
        self.layout.addLayout(self.side_layout)
        
        # Add stretch to push side_layout to the left
        self.layout.addStretch()

    def _show_home(self):
        pass

    def _show_products(self):
        pass

    def _show_orders(self):
        pass

    def _show_sell(self):
        pass

    