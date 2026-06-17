from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])

oyna = QWidget()
oyna.setWindowTitle("Super App")
oyna.setGeometry(1400, 200, 405, 720)
oyna.show()

app.exec_()