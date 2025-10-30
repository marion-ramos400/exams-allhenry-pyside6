
from employee.model import Employee
from employee.department import randomDept
import pandas as pd
import openpyxl
import names
import datetime
import random
import os

class EmployeeController:
    def __init__(self):
        self.range_salary = [25000, 120000]
        self.range_step_salary = 1000
        self.hire_date_range = [datetime.datetime(2020, 1, 1),
                                datetime.datetime.now()]

    def generateEmployees(self, numEmployees):
        return [Employee(
            i + 1,
            names.get_full_name(),
            randomDept(),
            self.randomSalary(),
            self.randomHireDate()
        ) for i in range(numEmployees)]

    def randomSalary(self):
        return random.randrange(
                self.range_salary[0],
                self.range_salary[1],
                self.range_step_salary
            )

    def randomHireDate(self):
        dt_diff = (self.hire_date_range[1] -
                   self.hire_date_range[0]).total_seconds()
        out_date = self.hire_date_range[0] + datetime.timedelta(
                seconds=random.randint(0, int(dt_diff))
            )

        return out_date.date()

    def exportToExcel(self, outDir, empData):
        try:
            fpath = os.path.join(outDir, 'employees.xlsx')

            # Employees DataFrame
            dfEmp = pd.DataFrame([
                emp.__dict__ for emp in empData
            ])

            # Summary DataFrame
            dfSummary = dfEmp.groupby('department')['salary'].mean()
            dfSummary.name = "Average Salary"
            dfSummary = dfSummary.to_frame().T
            dfSummary = dfSummary.round(2)


            with pd.ExcelWriter(fpath) as writer:
                dfEmp.to_excel(writer, sheet_name="Employees", index=False)
                dfSummary.to_excel(writer, sheet_name="Summary")

            self.cleanUpFile(fpath) #, ["Employees", "Summary"])


            return True, ''
        except Exception as e:
            errinfo = e
            if hasattr(e, 'message'):
                errinfo = e.message
            return False, f'Extraction Failed. {errinfo}'

    def cleanUpFile(self, fpath):
        wb = openpyxl.load_workbook(fpath)
        sheetNames = ["Employees", "Summary"]
        self.addExportTime(wb, sheetNames[1])
        self.fixColumnSpacing(wb, sheetNames)
        wb.save(fpath)

    def fixColumnSpacing(self, wb, sheetNames):
        for sheet in sheetNames:
            ws = wb[sheet]
            for col in ws.columns:
                #ws.column_dimensions[col[0].column_letter].auto_size = True
                ws.column_dimensions[col[0].column_letter].width = 20

    def addExportTime(self, wb, sheet):
        ws = wb[sheet]
        for i in range(2): ws.append(('',''))
        ws.append(('Exported At', datetime.datetime.now()))
