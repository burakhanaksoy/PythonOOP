# private classes can be accessed by same file or certain scope
# public classes can be accessed everywhere

class _Private:
    def __init__(self, name):
        self.name = name

    def _show(self):
        print("Showing content")


class NotPrivate:
    def __init__(self, name):
        self.name = name

    def _display(self):
        print('Hello')

    def display(self):
        print('Hi')
