#Create a dictionary of n persons where key is name and value is city.
#a) Display all names
#b) Display all city names
#c) Display student name and city of all students.
n = int(input("Enter the number of persons: "))
persons = {}
for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    persons[name] = city
print("Names of all persons:")
for name in persons.keys():
    print(name)
print("City names of all persons:")
for city in persons.values():
    print(city)
print("Name and city of all persons:")
for name, city in persons.items():
    print(f"{name} lives in {city}.")
