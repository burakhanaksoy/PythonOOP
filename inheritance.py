class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")


class Dog(Animal):
    def bark(self):
        print("howl howl")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print("meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color} colored")


dog = Dog("husky", 15)
dog.bark()
dog.show()

cat = Cat('whiskers', 12, 'green')
cat.meow()
cat.show()
