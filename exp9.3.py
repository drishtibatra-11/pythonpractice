class Parent:
    def show(self):
        print("This is Parent class")

class Child(Parent):
    def display(self):
        print("This is Child class")

c = Child()
c.show()
c.display()
#multiple inheritance
class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skills(self):
        print("Child has skills:")

c = Child()
c.skill1()
c.skill2()
#multilevel inheritence
class Grandparent:
    def house(self):
        print("Grandparent's House")

class Parent(Grandparent):
    def car(self):
        print("Parent's Car")

class Child(Parent):
    def bike(self):
        print("Child's Bike")

c = Child()
c.house()
c.car()
c.bike()
#heirarchical inheritance
class Parent:
    def property(self):
        print("Parent Property")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.property()
c2.property()

