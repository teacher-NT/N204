from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel,
    QPushButton
)
from PyQt5.QtGui import QFont

font1 = QFont("Comic Sans MS", 30)
font2 = QFont("Gabriola", 30)

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Super App")
oyna.setGeometry(1400, 200, 405, 720)
oyna.setStyleSheet("background-color: #8cd9fa;")

text1 = QLabel(oyna)
text1.setText("Counter")
text1.setStyleSheet("""
                    color: green; 
                    font-weight: bold;
                    """)
text1.setFont(font2)
text1.move(130, 10)

text2 = QLabel(oyna)
text2.setText("0")
text2.setStyleSheet("""
                    color: red; 
                    font-weight: bold;
                    """)
text2.setFont(font1)
text2.setFixedSize(300, 100)
text2.move(180, 100)


btn1 = QPushButton(oyna)
btn1.setText("Count")
btn1.setGeometry(125, 300, 155, 50)
btn1.setStyleSheet("""
    font-size: 20px;
    font-weight: bold;
                   background-color: #22c70c;
                   border-radius: 25px;
                   border: 2px solid black;
""")
def func():
    son = int(text2.text()) + 1
    text2.setText(str(son))
btn1.clicked.connect(func)


btn2 = QPushButton(oyna)
btn2.setText("Reset")
btn2.setGeometry(125, 360, 155, 50)
btn2.setStyleSheet("""
    font-size: 20px;
    font-weight: bold;
                   background-color: #cf3a0c;
                   border-radius: 25px;
                   border: 2px solid black;
""")
def func2():
    text2.setText("0")

btn2.clicked.connect(func2)

oyna.show()
app.exec_()