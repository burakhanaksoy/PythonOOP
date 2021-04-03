import datetime


class Employee:
    raise_amount = 1.04  # Class variable
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employees += 1

    def fullname(self):
        return self.first + ' ' + self.last

    def apply_raise(self):
        # Can also use Employee.raise_amount
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

# class method as alternative constructor

    @classmethod
    def from_string(cls, emp_str):
        "construct a new employee from string kebab case"
        first_name, last_name, pay = emp_str.split('-')
        # calling constructor with cls keyword, denoting class
        return cls(first_name, last_name, pay)

    @staticmethod
    def is_work_day_with_string(day):
        work_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
        for d in work_days:
            if d.upper() == day.upper():
                print('work day')
                return True
        print('not a work day')
        return False

    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            print('not a work day')
            return False
        else:
            print('work day')
            return True


# creating employees by parsing kebab-case string
emp_str1 = 'John-Doe-7000'

# parsing
emp1 = Employee.from_string(emp_str1)
emp2 = Employee('Burak', 'Aksoy', 3000)

print(emp1.__dict__)
print(emp2.__dict__)

# regular methods pass self def my_func(self),
# class methods pass cls def class_func(cls),
# However, static methods do not pass anyhting

print(Employee.is_work_day_with_string('monday'))
print(Employee.is_work_day_with_string('saturday'))

my_date = datetime.date.today()
print(my_date)
print(Employee.is_work_day(my_date))
