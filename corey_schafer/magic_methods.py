# magic methods help us change built in methods and/or operations
from datetime import timedelta
import math


class Employee:
    raise_amt = 1.04

    def __init__(self, f_name, l_name, pay):
        self.f_name = f_name
        self.l_name = l_name
        self.email = self.f_name.lower() + '.' + self.l_name.lower() + '@company.com'
        self.pay = pay

    def fullname(self):
        return f"{self.f_name} {self.l_name}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee('{self.f_name}', '{self.l_name}', {self.pay})"

    def __str__(self):
        return f"Employee('{self.fullname()} -- {self.email}')"

    def __add__(self, other):
        return self.pay + other.pay

    def __sub__(self, other):
        return self.pay - other.pay

    # override __len__() method to calculate length of employee full name
    def __len__(self):
        # didn't use fullname() since it contains space
        return len(self.f_name + self.l_name)

        # It's good to have at least __repr__() method since if we don't define __str__() method and call it,
        # Python will automatically look for __repr__() method...


emp1 = Employee('burak', 'aksoy', 2000)
emp2 = Employee('Marash', 'Raghev', 5700)
print(emp1)
print(repr(emp1))
print(str(emp1))
print(emp1 + emp2)
print(emp1 - emp2)
print(len(emp2))  # same as print(emp2.__len__())

time1 = timedelta(1, 2, 3, 4, 5, 6, 1)
time2 = timedelta(1, 3, 5, 2, 1, 3, 4)

print(timedelta.__add__(time1, time2))
