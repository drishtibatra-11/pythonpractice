#sum of cubes
def sum_of_cubes(n):
    if(n==1):
        return 1
    else:
        return n**3 + sum_of_cubes(n-1)
n=int(input("enter a number: "))
print("sum of cubes: ",sum_of_cubes(n))