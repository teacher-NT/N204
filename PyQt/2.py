from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel
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
text1.setText("Bu birinchi matn")
text1.setStyleSheet("""
                    color: green; 
                    font-weight: bold;
                    """)
text1.setFont(font2)
text1.move(70, 10)

oyna.show()
app.exec_()