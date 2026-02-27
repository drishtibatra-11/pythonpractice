#create tuple to store n numeric values and find the sum and average of the values
numbers=tuple(map(int,input("enter numbers: ").split()))
average=sum(numbers)/len(numbers)
print("average: ",average)