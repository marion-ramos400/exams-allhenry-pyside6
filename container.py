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
import os

from employee.controller import EmployeeController
from messages import ERROR, SUCCESS

class MainContainer(QWidget):
    def __init__(self):
        super().__init__()
        self.labelLog = QLabel()
        self.labelinputNumEmployees = QLabel()

        self.labelinputNumEmployees.setText('Number of Employees')
        self.inputNumEmployees = QLineEdit()
        self.setIntValidator()

        btnFolder = QPushButton('Select Folder')
        btnGenerate = QPushButton('Generate Data')
        btnExport = QPushButton('Export')

        btnFolder.clicked.connect(self.openFolderBrowser)
        btnGenerate.clicked.connect(self.generateData)
        btnExport.clicked.connect(self.exportData)

        hLayout =  QHBoxLayout()
        hLayout.addWidget(self.labelinputNumEmployees)
        hLayout.addWidget(self.inputNumEmployees)
        hLayout.addWidget(btnFolder)
        hLayout.addWidget(btnGenerate)
        hLayout.addWidget(btnExport)

        layout = QGridLayout()
        layout.addLayout(hLayout, 0, 0)
        layout.addWidget(self.labelLog, 1, 0)

        self.setLayout(layout)

        self.empData = []
        self.empControl = EmployeeController()

        self.fileDir = None

    def setIntValidator(self):
        intValidator = QIntValidator(0, 999999, self.inputNumEmployees)
        self.inputNumEmployees.setValidator(intValidator)

    def showMsg(self, msg):
        self.labelLog.setText(msg)

    def generateData(self):
        numEmp = self.inputNumEmployees.text()
        if len(numEmp) < 1:
            self.showMsg(ERROR.NumEmployees)
            return
        numEmp = int(numEmp)
        self.empData = self.empControl.generateEmployees(numEmp)
        if len(self.empData) > 0:
            self.showMsg(SUCCESS.DataGenerated)
        else:
            self.showMsg(ERROR.NoDataGenerated)

    def openFolderBrowser(self):
        dialog = QFileDialog(self)
        dialog.setDirectory(os.getcwd())
        dialog.setFileMode(QFileDialog.FileMode.Directory)
        if dialog.exec():
            dirsRes = dialog.selectedFiles()
            if len(dirsRes) > 1:
                self.showMsg(ERROR.OneDirOnly)
                return
            if len(dirsRes) < 1:
                self.showMsg(ERROR.NoDirSelected)
                return
            self.fileDir = dirsRes[0]

    def exportData(self):
        if not self.fileDir:
            self.showMsg(ERROR.FolderNotSet)
            return
        if not self.inputNumEmployees.text():
            self.showMsg(ERROR.NumEmployees)
            return
        if len(self.empData) < 1:
            self.showMsg(ERROR.NoEmployeeData)
            return

    



