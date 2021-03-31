class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name
        Person.add_people()

    def get_name():
        return self.name

    @classmethod
    def get_number_of_people(cls):
        return cls.number_of_people

    @classmethod
    def add_people(cls):
        cls.number_of_people += 1

p1 = Person('burak')
p2 = Person('ahmet')

print(Person.get_number_of_people())