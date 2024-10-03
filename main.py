from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from src.views.qlogin import QLogin

class MainApp(QMainWindow):
    def __init__(self):

        super().__init__()
        self.main_widget = QWidget()
        self.setWindowTitle('Imbutidora Saladino')
        self.resize(800, 600)
        self.setCentralWidget(self.main_widget)
        
    def run(self):
        login = QLogin()
        if login.exec():
            print('User logged in')
        else:
            print('User rejected')

    def show(self):
        super().show()
        self.run()
    
    def _show_main(self):
        self.show()
        


if __name__ == "__main__":
    app = QApplication([])
    m = MainApp()
    m.show()
    app.exec()