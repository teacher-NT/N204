from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton, QLineEdit
)
from PyQt5.QtGui import QFont

font1 = QFont("Comic Sans MS", 30)
font2 = QFont("Gabriola", 30)

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Super App")
oyna.setGeometry(1400, 200, 405, 720)
oyna.setStyleSheet("background-color: #8cd9fa;")

line = QLineEdit(oyna)
line.setGeometry(25, 20, 355, 50)
line.setStyleSheet("""
                    font-size: 28px;
                   background-color: white;
                   border: 2px solid black;
""")
line.setPlaceholderText("Ism kiriting...")

btn1 = QPushButton(oyna)
btn1.setText("Saqlash")
btn1.setGeometry(125, 150, 155, 50)
btn1.setStyleSheet("""
                    font-size: 20px;
                    font-weight: bold;
                   background-color: #22c70c;
                   border-radius: 25px;
                   border: 2px solid black;
""")
def func():
    text = line.text()
    with open("names.txt", "a") as file:
        file.write(f"{text}\n")
    line.clear()
    line.setFocus()
btn1.clicked.connect(func)
line.returnPressed.connect(func)

oyna.show()
app.exec_()