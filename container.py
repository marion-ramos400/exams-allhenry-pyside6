from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QGridLayout,
    QFileDialog,
    QHBoxLayout,
)
from PySide6.QtGui import QIntValidator

from employee.controller import EmployeeController

class MainContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.labelLog = QLabel()
        self.labelinputNumEmployees = QLabel()

        self.labelinputNumEmployees.setText('Number of Employees')
        self.inputNumEmployees = QLineEdit()
        self.setIntValidator()

        self.btnFolder = QPushButton('Select Folder')
        btnGenerate = QPushButton('Generate Data')
        btnExport = QPushButton('Export')

        btnGenerate.clicked.connect(self.generateData)


        hLayout =  QHBoxLayout()
        hLayout.addWidget(self.labelinputNumEmployees)
        hLayout.addWidget(self.inputNumEmployees)
        hLayout.addWidget(self.btnFolder)
        hLayout.addWidget(btnGenerate)
        hLayout.addWidget(btnExport)

        layout = QGridLayout()
        layout.addLayout(hLayout, 0, 0)
        layout.addWidget(self.labelLog, 1, 0)

        self.setLayout(layout)

        self.empData = []

        self.empControl = EmployeeController()

    def setIntValidator(self):
        intValidator = QIntValidator(0, 999999, self.inputNumEmployees)
        self.inputNumEmployees.setValidator(intValidator)

    def generateData(self):
        numEmp = self.inputNumEmployees.text()
        if len(numEmp) < 1:
            self.labelLog.setText('Please enter number of employees')
            return
        numEmp = int(numEmp)
        self.empData = self.empControl.generateEmployees(numEmp)
        for p in self.empData:
            print(p.full_name, p.salary, p.hire_date)




