class Math:

    @staticmethod
    def add5(x):
        return x + 5

# in order to use this class' method somewhere else, we don't have to
# create an instance of this class, like m = Math(), instead we just
# import this class and use the static method


print(Math.add5(15))  # prints 20

# I also imported this class in app.py file