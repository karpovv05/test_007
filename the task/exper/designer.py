from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('Программа')
        self.setGeometry(300, 300, 400, 300)

        self.new_text = QtWidgets.QLabel(self)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('Как же я заебаlsя')
        self.main_text.move(150, 100)
        self.main_text.adjustSize()

        self.main_bat = QtWidgets.QPushButton(self)
        self.main_bat.setText('Кнопка')
        self.main_bat.clicked.connect(self.Batton)

    def Batton(self):
        self.new_text.setText('Вторая надпись')
        self.new_text.move(100,30)

def appli():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


appli()
