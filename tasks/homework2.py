from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QTextEdit
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.Winit()

    def Winit(self):

        self.setGeometry(550, 300, 200, 200)
        self.setWindowTitle("Прятки для виджетов")

        self.ch_b_1 = QCheckBox(self)
        self.ch_b_1.setGeometry(10, 10, 100, 40)
        self.ch_b_1.setText("Edit1")
        self.ch_b_1.stateChanged.connect(self.switch)

        self.line_e_1 = QTextEdit(self)
        self.line_e_1.setGeometry(70, 10, 100, 30)
        self.line_e_1.setText("Поле Edit1")

        self.ch_b_2 = QCheckBox(self)
        self.ch_b_2.setGeometry(10, 50, 100, 40)
        self.ch_b_2.setText("Edit2")
        self.ch_b_2.stateChanged.connect(self.switch)

        self.line_e_2 = QTextEdit(self)
        self.line_e_2.setGeometry(70, 50, 100, 30)
        self.line_e_2.setText("Поле Edit2")

        self.ch_b_3 = QCheckBox(self)
        self.ch_b_3.setGeometry(10, 90, 100, 40)
        self.ch_b_3.setText("Edit3")
        self.ch_b_3.stateChanged.connect(self.switch)

        self.line_e_3 = QTextEdit(self)
        self.line_e_3.setGeometry(70, 90, 100, 30)
        self.line_e_3.setText("Поле Edit3")

        self.ch_b_4 = QCheckBox(self)
        self.ch_b_4.setGeometry(10, 130, 100, 40)
        self.ch_b_4.setText("Edit4")
        self.ch_b_4.stateChanged.connect(self.switch)

        self.line_e_4 = QTextEdit(self)
        self.line_e_4.setGeometry(70, 130, 100, 30)
        self.line_e_4.setText("Поле Edit4")

        self.flags = {self.ch_b_1.text(): [True, self.line_e_1],
                 self.ch_b_2.text(): [True, self.line_e_2],
                 self.ch_b_3.text(): [True, self.line_e_3],
                 self.ch_b_4.text(): [True, self.line_e_4]}

    def switch(self):

        sender = self.sender().text()
        if self.flags[sender][0]:
            obj = self.flags[sender][1]
            obj.hide()

        else:
            obj = self.flags[sender][1]
            obj.show()

        self.flags[sender][0] = not self.flags[sender][0]


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())