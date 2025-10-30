from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QFileDialog,
)

from employee.controller import EmployeeController

class MainContainer:
    def __init__(self):

        self.labelLog = QLabel()
        self.labelinputNumEmployees = QLabel()

        self.labelinputNumEmployees.setText('Number of Employees')
        self.inputNumEmployees = QLineEdit()

        self.btnFolder = QPushButton('Select Folder')
        self.btnGenerate = QPushButton('Generate Data')
        self.btnExport = QPushButton('Export')


        layout = QGridLayout()
        layout.addWidget(self.labelinputNumEmployees, 0, 0)
        layout.addWidget(self.inputNumEmployees, 0, 1)
        layout.addWidget(self.btnFolder, 0, 2)
        layout.addWidget(self.btnGenerate, 0, 3)
        layout.addWidget(self.btnExport, 0, 4)
        layout.addWidget(self.labelLog, 1, 0)

        self.container = QWidget()
        self.container.setLayout(layout)

        self.emp_data = []

#        empControl = EmployeeController()
#        pips = empControl.generateEmployees(100)
#        for p in pips:
#            print(p.salary, p.hire_date)

    def getContainer(self):
        return self.container

#    def generate_data(self):



