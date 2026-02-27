#print 1 to n using recursion
def print_numbers(n):
    if n>0:
        print_numbers(n-1)
        print(n)
n=int(input("enter a number: "))
print_numbers(n)