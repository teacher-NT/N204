from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel
)

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Super App")
oyna.setGeometry(1400, 200, 405, 720)
oyna.setStyleSheet("background-color: #8cd9fa;")

text1 = QLabel(oyna)
text1.setText("Bu birinchi matn")
text1.setStyleSheet("""font-size: 30px; 
                    color: green; 
                    font-weight: bold;
                    """)
text1.move(70, 10)

oyna.show()
app.exec_()