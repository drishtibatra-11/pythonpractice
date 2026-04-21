class Parent:
    def show(self):
        print("This is Parent method")

class Child(Parent):
    def show(self):  # overriding
        print("This is Child method")

c = Child()
c.show()