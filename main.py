from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget)
from src.views.qlogin import QLogin
from src.views.qmenu import QMenu

class MainApp(QMainWindow):
    def __init__(self):

        super().__init__()
        self.main_widget = QWidget()
        self.resize(800, 600)

        self.setWindowTitle('Imbutidora Saladino')
        self.setCentralWidget(self.main_widget)
        self.qmenu = QMenu()

    def run(self):
        login = QLogin()
        if login.exec():
            self._show_menu()
            print('User logged in')
        else:
            print('User rejected')

    def _show_menu(self):
        self.main_widget = self.qmenu
        self.setCentralWidget(self.main_widget)
        self.main_widget.show()
        
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