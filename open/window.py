from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont

class Window(QWidget):
    def __init__(self, parent, title = "Тест окно", size = (250, 170), font_size = 11):
        super().__init__()
        self.parent = parent
        self.setWindowFlags(Qt.Window | Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowTitle(title)
        self.resize(*size)
        font = QFont()
        font.setPointSize(font_size)
        self.setFont(font)
        self.widget = QWidget(self) # .centralwidget
        self.widget.setGeometry(QRect(10, 10, size[0] - 20, size[1] - 20))