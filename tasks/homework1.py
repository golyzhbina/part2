from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QApplication
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Winit()

    def Winit(self):
        self.setGeometry(300, 300, 360, 60)
        self.setWindowTitle("Фокус")

        self.label_left = QLineEdit(self)
        self.label_left.setGeometry(10, 10, 130, 40)
        self.label_left.setText("Фокус")

        self.label_right = QLineEdit(self)
        self.label_right.setGeometry(220, 10, 130, 40)

        self.button = QPushButton(self)
        self.button.setGeometry(150, 10, 60, 40)
        self.button.setText("->")
        self.button.clicked.connect(self.switch)
        self.flag = True

    def switch(self):
        if self.flag:
            self.label_left.setText("")
            self.label_right.setText("Фокус")
            self.button.setText("<-")
        else:
            self.label_right.setText("")
            self.label_left.setText("Фокус")
            self.button.setText("->")

        self.flag = not self.flag


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
