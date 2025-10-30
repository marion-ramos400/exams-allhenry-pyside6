from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QFileDialog,
)

from employee.controller import EmployeeController

class MainContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.labelLog = QLabel()
        self.labelinputNumEmployees = QLabel()

        self.labelinputNumEmployees.setText('Number of Employees')
        self.inputNumEmployees = QLineEdit()

        self.btnFolder = QPushButton('Select Folder')
        self.btnGenerate = QPushButton('Generate Data')
        btnExport = QPushButton('Export')

        self.btnGenerate.clicked.connect(self.generateData)

        layout = QGridLayout()
        layout.addWidget(self.labelinputNumEmployees, 0, 0)
        layout.addWidget(self.inputNumEmployees, 0, 1)
        layout.addWidget(self.btnFolder, 0, 2)
        layout.addWidget(self.btnGenerate, 0, 3)
        layout.addWidget(btnExport, 0, 4)
        layout.addWidget(self.labelLog, 1, 0)

        self.setLayout(layout)

        self.emp_data = []

#        empControl = EmployeeController()
#        pips = empControl.generateEmployees(100)
#        for p in pips:
#            print(p.salary, p.hire_date)

    def generateData(self):
        print('test click')



