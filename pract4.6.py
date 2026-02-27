#count numbers(0-3)
numbers=list(map(int,input("enter numbers(0-3): ").split()))
count=[0,0,0,0]
for i in range(4):
    print("number of ",i,": ",numbers.count(i))