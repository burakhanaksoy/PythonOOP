class Person:
    number_of_people = 0  # this is a static attribute

    def __init__(self, name):
        self.name = name
        # Person.number_of_people += 1

p1 = Person('burak')
p2 = Person('james')

print(p1.number_of_people)
print(p2.number_of_people)
print(Person.number_of_people) # all print 0

Person.number_of_people = 8

print(p1.number_of_people)
print(p2.number_of_people)
print(Person.number_of_people) # all print 8