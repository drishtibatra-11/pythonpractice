class dog:
    species = "canine"

    def __init__(self, name, age):   # fixed
        self.name = name
        self.age = age

dog1 = dog("buddy", 3)
dog2 = dog("charlie", 5)

print(dog1.species)
print(dog1.name)
print(dog2.name)  
dog1.name ="MAX"
print(dog1.name)
dog_species = "faline"
print(dog1.species)
print(dog2.species)    