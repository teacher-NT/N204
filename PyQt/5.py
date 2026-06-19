import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
px = round(37.8)

app = QApplication([])

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QHBoxLayout()
        self.grid = QGridLayout()
        self.setWindowTitle("Dastur")
        # self.setGeometry(1400,100,px*9,px*16)
        self.text1 = QLabel("Salom dunyo")
        self.text1.setStyleSheet("""
                            font-size: 30px;
                            font-family: Gabriola;
        """)
        # self.vbox.addWidget(self.text1)
        self.grid.addWidget(self.text1, 1, 1)
        self.btn1 = QPushButton("1")
        # self.vbox.addWidget(self.btn1)
        self.grid.addWidget(self.btn1, 2, 1)

        self.btn2 = QPushButton("2")
        # self.vbox.addWidget(self.btn2)
        self.grid.addWidget(self.btn2, 2, 2)

        self.btn3 = QPushButton("3")
        # self.vbox.addWidget(self.btn3)
        self.grid.addWidget(self.btn3, 3, 1)

        self.btn4 = QPushButton("4")
        # self.vbox.addWidget(self.btn4)
        self.grid.addWidget(self.btn4, 3, 2) 
        # self.setLayout(self.vbox)
        self.setLayout(self.grid)
        self.show()

oyna1 = Window()
app.exec_()