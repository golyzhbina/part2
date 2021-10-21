from PyQt5.QtWidgets import QMainWindow, QPushButton, QListWidget, QApplication
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setGeometry(400, 200, 300, 300)
        self.setWindowTitle("Перемешиватель")

        self.pushbutton_mixer = QPushButton(self)
        self.pushbutton_mixer.setGeometry(20, 20, 90, 30)
        self.pushbutton_mixer.setText("Перемешать")
        self.pushbutton_mixer.clicked.connect(self.mix)

        self.list = QListWidget(self)
        self.list.setGeometry(20, 60, 260, 220)
        self.list.setEnabled(False)

        self.flag = True

    def mix(self):

        self.list.clear()
        with open("not_for_me.txt", "r", encoding="utf-8") as out_file:
            if self.flag:
                text = list(map(lambda x: x.strip(), out_file.readlines()[1::2]))
            else:
                text = list(map(lambda x: x.strip(), out_file.readlines()[::2]))

        self.flag = not self.flag

        self.list.addItems(text)


sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())
