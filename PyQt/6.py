import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox,
    QVBoxLayout, QHBoxLayout, QGridLayout
)
px = round(37.8)

app = QApplication([])

combo_style = """
    font-size: 20px;
    font-weight: bold;
    color: #1532b0;
    background-color: #d7d7db;
    border-radius: 10px;
    padding: 10px;
"""

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.vbox = QHBoxLayout()
        self.grid = QGridLayout()
        self.setWindowTitle("Dastur")
        # self.setGeometry(1400,100,px*9,px*16)
        self.text1 = QLabel("Milliy taomlar")
        self.text1.setStyleSheet("""
                            font-size: 30px;
                            font-family: Gabriola;
        """)
        self.grid.addWidget(self.text1, 1, 1)

        self.menu = QComboBox()
        self.menu.addItems([" Ovqatlar", "Lavash", "Chuchvara", "Shovurma", "Moshxo'rda", "Osh", "Beshpanja"])
        self.menu.setStyleSheet(combo_style)
        self.menu.currentTextChanged.connect(self.get_food)
        self.grid.addWidget(self.menu, 1,2)

        self.btn1 = QPushButton("1")
        self.grid.addWidget(self.btn1, 2, 1)

        self.btn2 = QPushButton("2")
        self.grid.addWidget(self.btn2, 2, 2)

        self.btn3 = QPushButton("3")
        self.grid.addWidget(self.btn3, 3, 1)

        self.btn4 = QPushButton("4")
        self.grid.addWidget(self.btn4, 3, 2) 
        self.setLayout(self.grid)
        self.show()
    
    def get_food(self):
        b = self.menu.currentText()
        print(f"Tanlandi: {b}")

oyna1 = Window()
app.exec_()