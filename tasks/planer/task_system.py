import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDateEdit, QCalendarWidget, QListWidget
from py_main_window import Ui_MainWindow


class TaskSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QApplication(sys.argv)
window = TaskSystem()
window.show()
sys.exit(app.exec())

