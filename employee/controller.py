
from employee.model import Employee
from employee.department import randomDept
import pandas as pd
import names
import datetime
import random

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




