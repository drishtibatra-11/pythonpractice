#set operations on fruits
n=int(input("enter number of fruits in each set: "))
s1=set()
s2=set()
print("enter number of fruits in set 1: ")

for i in range(n):  
    s1.add(input())
    print("enter number of fruits in set 2: ")
    for i in range(n):
        s2.add(input())
        print("fruits in set 1: ",s1&s2)
        print("fruits in set 2: ",s1|s2)
        print("fruits in set 1 but not in set 2: ",s1-s2)