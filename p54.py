#7. Write functions to explain mentioned concepts: a. Keyword argument b. Default argument c. Variable length argument

def add(a, b):
    print("Sum =", a + b)


add(b=20, a=10)
def multiply(a, b=5):
    print("Multiplication =", a * b)


multiply(4)     
multiply(4, 3)  
def find_sum(*numbers):
    total = 0
    for n in numbers:
        total += n
    print("Total Sum =", total)


find_sum(10, 20)
find_sum(5, 10, 15, 20)