#Write a Python function that takes a positive integer and returns the sum of the cube of
#all the positive integers smaller than the specified number. 
def sum_of_cubes(n):
    total = 0
    for i in range(1, n):
        total += i ** 3
    return total

n = int(input("Enter a positive integer: "))
result = sum_of_cubes(n)
print("Sum of cubes of all positive integers smaller than", n, "is:", result)