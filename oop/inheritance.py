from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    # обязательно нужно переопределить метод
    @abstractmethod
    def calculate_payroll(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, id, name, weekly_salary):
        super().__init__(id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyEmployee(Employee):
    def __init__(self, id, name, hours_worked, hours_rate):
        super().__init__(id, name)
        self.hours_worked = hours_worked
        self.hours_rate = hours_rate

    def calculate_payroll(self):
        return self.hours_rate * self.hours_worked


class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name, weekly_salary, commission):
        super().__init__(id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class Manager(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} screams and yells for {hours} hours.')


class Secretary(SalaryEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours doing office paperwork.')


class SalesPerson(CommissionEmployee):
    def work(self, hours):
        print(f'{self.name} expends {hours} hours on the phone.')


class FactoryWorker(HourlyEmployee):
    def work(self, hours):
        print(f'{self.name} manufactures gadgets for {hours} hours.')


class PayrollSystem:
    @staticmethod
    def calculate_payroll(employees):
        print('Calculating Payroll')
        print('='*10)
        for employee in employees:
            print(f'Payroll for: {employee.id} - {employee.name}')
            print(f'- Check amount: {employee.calculate_payroll()}')


class ProductivitySystem:
    @staticmethod
    def track(employees, hours):
        print('Tracking employee productivity')
        print('=' * 10)
        for employee in employees:
            employee.work(hours)
        print('')


#
# salary_employee = SalaryEmployee(1, 'John Smith', 1500)
# hourly_employee = HourlyEmployee(2, 'Jane Doe', 40, 15)
# commission_employee = CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
# payroll_system = PayrollSystem()
# payroll_system.calculate_payroll([
#     salary_employee,
#     hourly_employee,
#     commission_employee
# ])

manager = Manager(1, 'Mary Poppins', 3000)
secretary = Secretary(1, 'John Smith', 1500)
sales_guy = SalesPerson(3, 'Kevin Bacon', 1000, 250)
factory_worker = FactoryWorker(2, 'Jane Doe', 40, 15)
employees = [manager, secretary, sales_guy, factory_worker]
productivity_system = ProductivitySystem()
productivity_system.track(employees, 40)
payroll_system = PayrollSystem()
payroll_system.calculate_payroll(employees)
