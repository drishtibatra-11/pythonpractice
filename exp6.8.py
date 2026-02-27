numbers=list(map(int,input("enter numbers: ").split()))
result=(lambda x: max(x), min(x))(numbers)
print(result)
