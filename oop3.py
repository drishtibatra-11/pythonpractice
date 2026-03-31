class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):   # correct
        return f"{self.name} is {self.age} years old"

dog1 = dog("buddy", 3)
dog2 = dog("charlie", 5)

print(dog1)
print(dog2)  