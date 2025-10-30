
class Employee:
    def __init__(
        self,
        emp_id=None,
        full_name=None,
        department=None,
        salary=None,
        hire_date=None
    ):
        self.emp_id = emp_id
        self.full_name = full_name
        self.department = department
        self.salary = salary
        self.hire_date = hire_date

    def setEmpId(self, id):
        self.emp_id = id
        return self

    def setFullName(self, name):
        self.full_name = name
        return self

    def setDepartment(self, department):
        self.department = department
        return self

    def setSalary(self, salary):
        self.salary = salary
        return self

    def setHireDate(self, hire_date):
        self.hire_date = hire_date
        return self
