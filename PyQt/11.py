import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QComboBox, QCheckBox, QRadioButton,
    QMessageBox, QTextEdit,QLineEdit,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
from PyQt5.QtCore import Qt


class Window2(QWidget):
    def __init__(self, oldingi):
        super().__init__()
        self.oldingi = oldingi
        self.grid = QGridLayout()
        self.setGeometry(1400, 200, 405,720)

        self.label1 = QLabel("Ikkinchi Oyna")
        self.label1.setStyleSheet("""
                font-size: 40px;
                font-weight:bold;
                font-family: Gabriola;
                                  color: red;
        """)
        self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.grid.addWidget(self.label1, 1,1,1,2)

        self.btn1 = QPushButton("Orqaga")
        self.btn1.setStyleSheet("""
                font-size: 20px;
                                font-weight:bold;
                                padding: 5px;
                                background-color: red;
                                color: white;
        """)
        self.btn1.clicked.connect(self.open_back)
        self.grid.addWidget(self.btn1, 2,1,1,2)
        self.setLayout(self.grid)

    def open_back(self):
        self.prev = MainWindow()
        self.prev.show()
        self.hide()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.grid = QGridLayout()
        self.setGeometry(1400, 200, 405,720)

        self.label1 = QLabel("Bosh oyna")
        self.label1.setStyleSheet("""
                font-size: 40px;
                                  font-weight:bold;
                font-family: Gabriola;
        """)
        self.label1.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        self.grid.addWidget(self.label1, 1,1,1,2)
        self.line = QLineEdit()
        self.line.setStyleSheet("""
                                font-size: 20px;
                                border: 2px solid black;
        """)
        self.line.setPlaceholderText("Nimadir kiriting...")
        self.grid.addWidget(self.line,2,1,1,2)
        self.btn1 = QPushButton("Keyingi")
        self.btn1.setStyleSheet("""
                font-size: 20px;
                                font-weight:bold;
                                padding: 5px;
                                background-color: green;
                                color: white;
        """)
        self.btn1.clicked.connect(self.open_next)
        self.grid.addWidget(self.btn1, 3,1,1,2)
        self.setLayout(self.grid)
        self.show()

    def open_next(self):
        self.keyingi = Window2(self)
        self.keyingi.show()
        self.hide()


app = QApplication([])
win = MainWindow()
app.exec_()