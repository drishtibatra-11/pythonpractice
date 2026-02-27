#find maximum and minimum 
def find_max_min(list):
    max=list[0]
    min=list[0]
    for i in list:
        if i>max:
            max=i
        if i<min:
            min=i
    return max,min
numbers=list(map(int,input("enter numbers: ").split()))
print(find_max_min(numbers))