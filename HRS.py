# A human Resource Sytem implemented using OOP.
# the HR system needs to process payroll but there are different employees so different payrolls need to be calculated.
class PayrollSystem:
    # interfaces need not be defined explicitly.Interfaces are defined by the attributes used and the methods called
    # by other functions and methods.
    def calculate_payroll(self, employees):
        print("Calculating payroll")
        print("==================")
        for employee in employees:
            print(f"payroll for {employee.id} - {employee.name}")
            print(f"Cheque amount: {employee.calculate_payroll()}")


# every employee must have a name and an id assigned
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# employees paid a fixed salary
class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


# employees paid per hour e.g manufacturing employees
class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hourly_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hourly_rate * self.hours_worked


# employees paid commission + fixed sales for the sales that they make
class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        super().calculate_payroll()
        fixed_salary = super().calculate_payroll()
        return fixed_salary + self.commission


salary_employee = SalaryEmployee(1, "Kelvin Njuguna",1500)
hourly_employee = HourlyEmployee(2, "John Smith", 40, 15)
commission_employee = CommissionEmployee(3, "Jane Doe", 1000, 250)

payroll_system = PayrollSystem()
payroll_system.calculate_payroll([
    salary_employee, hourly_employee, commission_employee
])