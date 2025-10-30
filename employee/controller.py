
from employee.model import Employee
from employee.department import randomDept
import pandas as pd
controller = 'hi test world'
#emp = Employee()
#emp.setEmpId(23)
#emp.setDepartment(Department.ADMINISTRATION)
#print(emp.department)

class EmployeeController:
    def __init__(self):
        pass

    def generateEmployees(self, numEmployees):
        return [Employee(
        
            department=randomDept()
        ) for i in range(1, numEmployees + 1)]



