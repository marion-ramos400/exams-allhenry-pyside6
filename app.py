from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

from container import MainContainer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Employee Data Generator')
#        self.setFixedSize(QSize(400, 300))
        container = MainContainer().getContainer()
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()


app.exec()
