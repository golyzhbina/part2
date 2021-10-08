from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.MWinit()

    def MWinit(self):

        self.setGeometry(700, 300, 400, 200)
        self.setWindowTitle("Азбука Морзе 2")

        self.buttons = []

        count = 1
        for i in range(97, 123):

            x = 10 + 30 * (i - 97)

            if 10 < i - 97 <= 20:
                count = 2
                x = 10 + 30 * (i - 108)

            elif 20 < i - 97 <= 30:
                count = 3
                x = 10 + 30 * (i - 118)

            a = QPushButton(self)
            a.setGeometry(x,
                          count * 10 + 10 * (count - 1) * 2, 30, 30)
            a.setText(chr(i))
            a.clicked.connect(self.out)
            self.buttons.append(a)

        del count

        self.line = QTextEdit(self)
        self.line.setGeometry(10, 120, 370, 30)
        self.line.setReadOnly(True)
        self.line.setFontPointSize(14)

        self.alphabet = {
            'A': '.-',
            'B': '-...',
            'C': '-.-.',
            'D': '-..',
            'E': '.',
            'F': '..-.',
            'G': '--.',
            'H': '....',
            'I': '..',
            'J': '.---',
            'K': '-.-',
            'L': '.-..',
            'M': '--',
            'N': '-.',
            'O': '---',
            'P': '.--.',
            'Q': '--.-',
            'R': '.-.',
            'S': '...',
            'T': '-',
            'U': '..-',
            'V': '...-',
            'W': '.--',
            'X': '-..-',
            'Y': '-.--',
            'Z': '--..',
        }

        self.button_clear = QPushButton(self)
        self.button_clear.setGeometry(330, 160, 40, 25)
        self.button_clear.setText("Clear")
        self.button_clear.clicked.connect(lambda: self.line.clear())

    def out(self):
        sender = self.sender().text().upper()
        letter = self.line.toPlainText() + self.alphabet[sender]
        self.line.setText(letter)


app = QApplication(sys.argv)
ex = MainWindow()
ex.show()
sys.exit(app.exec())
