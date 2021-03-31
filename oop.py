class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def set_name(self, name):
        self.name = name


dog1 = Dog("Husky", 15)
dog1.set_age(7)
print(dog1.get_age())
