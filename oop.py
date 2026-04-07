class parent :
    def show(self) :
        print("This is parent class")
class child(parent) :        
    def display(self) :
        print("This is child class")
obj = child()        
obj.show()
obj.display()