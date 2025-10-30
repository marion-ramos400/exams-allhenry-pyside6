from PySide6.QtWidgets import QApplication, QMainWindow
import sys

from container import MainContainer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Employee Data Generator')
        container = MainContainer()
        self.setCentralWidget(container)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
