from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from src.controllers.user import login

class QLogin(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self._build()

    def _build(self):
        # Add widgets
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.login = QPushButton('Login')
        self.login.clicked.connect(self._login)
        # Add widgets to layout
        self.layout.addWidget(QLabel('Username'))
        self.layout.addWidget(self.username)
        self.layout.addWidget(QLabel('Password'))
        self.layout.addWidget(self.password)
        self.layout.addWidget(self.login)

    def _login(self):
        user = login(self.username.text(), self.password.text())
        if user:
            self.accept()
        else:
            self.reject()


