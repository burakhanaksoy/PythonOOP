class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

# Getter method
    @property
    def email(self):
        if not(self.first == None and self.last == None):
            return f'{self.first.lower()}.{self.last.lower()}@company.com'
        else:
            return 'first and last name not defined'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Fullname deleted!')
        self.first = None
        self.last = None

    def __repr__(self):
        return f'Employee("{self.first}", "{self.last}")'

    def __str__(self):
        return f'Employee("{self.first}", "{self.last}")'


emp1 = Employee('John', 'Smith')
emp1.first = 'Jim'
# with @property decorator, we don't have to call .email like function, we call like attribute
print(emp1.email)
# do the same for fullname()
print(emp1.fullname)

# using the setter method
emp1.fullname = 'Burakhan Aksoy'
print(emp1.fullname)
print(emp1.email)

# deleter
del emp1.fullname
print(emp1.email)
print(emp1)
