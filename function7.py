#7.     Write functions to explain mentioned concepts:
#a.   Keyword argument
#b.   Default argument
#c.   Variable length argument

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=18, name="Drishti")
def greet(name="Guest"):
    print("Hello", name)

greet()          
greet("Drishti")
def add_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    print("Sum:", total)

add_numbers(2, 4, 6)
add_numbers(1, 2, 3, 4, 5)