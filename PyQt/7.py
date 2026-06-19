import os
os.system("cls")

from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QLineEdit, QComboBox,
    QCheckBox,
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

check_style = """
    font-size: 16px;
    font-weight: bold;
    color: #941690;
    background-color: #d7d7db;
    padding: 5px;
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

        self.add_checkbox()

        self.setLayout(self.grid)
        self.show()
    
    def get_food(self):
        b = self.menu.currentText()
        print(f"Tanlandi: {b}")

    def add_checkbox(self):
        self.ch1 = QCheckBox("Choy")
        self.ch1.stateChanged.connect(self.drink_choice)
        self.ch2 = QCheckBox("Kofe")
        self.ch2.stateChanged.connect(self.drink_choice)
        self.ch3 = QCheckBox("Kapuchino")
        self.ch3.stateChanged.connect(self.drink_choice)
        self.ch4 = QCheckBox("Cola")
        self.ch4.stateChanged.connect(self.drink_choice)
        self.ch5 = QCheckBox("Ayron")
        self.ch5.stateChanged.connect(self.drink_choice)
        self.ch6 = QCheckBox("Salfetka")
        self.ch6.stateChanged.connect(self.drink_choice)

        self.ch1.setStyleSheet(check_style)
        self.ch2.setStyleSheet(check_style)
        self.ch3.setStyleSheet(check_style)
        self.ch4.setStyleSheet(check_style)
        self.ch5.setStyleSheet(check_style)
        self.ch6.setStyleSheet(check_style)

        self.grid.addWidget(self.ch1, 2, 1)
        self.grid.addWidget(self.ch2, 2, 2)
        self.grid.addWidget(self.ch3, 3, 1)
        self.grid.addWidget(self.ch4, 3, 2)
        self.grid.addWidget(self.ch5, 4, 1)
        self.grid.addWidget(self.ch6, 4, 2)

    def drink_choice(self):
        drinks = []
        if self.ch1.isChecked():
            drinks.append(self.ch1.text())
        if self.ch2.isChecked():
            drinks.append(self.ch2.text())
        if self.ch3.isChecked():
            drinks.append(self.ch3.text())
        if self.ch4.isChecked():
            drinks.append(self.ch4.text())
        if self.ch5.isChecked():
            drinks.append(self.ch5.text())
        if self.ch6.isChecked():
            drinks.append(self.ch6.text())
        print(drinks)

oyna1 = Window()
app.exec_()