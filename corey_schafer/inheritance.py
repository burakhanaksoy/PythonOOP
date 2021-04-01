# Python OOP
class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name.lower() + '.' + last_name.lower() + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def from_string(cls, emp_str):
        name, surname, pay = emp_str.split('-')
        return cls(name, surname, pay)


class Developer(Employee):
    raise_amt = 1.01  # overriding raise_amt

    def __init__(self, first_name, last_name, pay, prog_lang=None):
        super().__init__(first_name, last_name, pay)
        self.prog_lang = prog_lang

    @classmethod
    def with_prog_lang(cls, first_name, last_name, pay, prog_lang):
        return cls(first_name, last_name, pay, prog_lang)

    @classmethod
    def from_string_kebab_case(cls, emp_str):
        first_name, last_name, pay, prog_lang = emp_str.split('-')
        return cls(first_name, last_name, pay, prog_lang)


class Manager(Employee):
    raise_amt = 1.1

    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        self.supervised_employee = []
        if employees is not None:
            self.supervised_employee = employees

    def add_emp(self, employee):
        if employee not in self.supervised_employee:
            self.supervised_employee.append(employee)

    def remove_emp(self, employee):
        if employee in self.supervised_employee:
            self.supervised_employee.remove(employee)

    def show_employees(self):
        if (len(self.supervised_employee) == 0):
            print(f"{self.first_name} is managing no one")
        else:
            print(f"{self.first_name} is supervising ")

            for emp in self.supervised_employee:
                print(f'--> {emp.fullname()}')


emp1 = Developer('Burak', 'Aksoy', 5000)
emp2 = Developer('Ozgur', 'Ozceylan', 5000, 'Python')

manager1 = Manager('Ahmet', 'Nazli', 10000, [emp1])
manager1.add_emp(emp2)

manager2 = Manager('Faruk', 'Tuncer', 10000)

manager1.show_employees()
manager2.show_employees()
