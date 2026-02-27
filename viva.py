#create aa set and find union,intersection,symmetruic difference
n=int(input("enter a number of fruits"))

s1=set()
s2=set()
print("enter the fruits for set1")
for i in range (n):
    s1.add(input())
print("enter the fruits for set2")
for i in range (n):
    s2.add(input())
print("union",s1&s2)
print("intersection",s1-s2)
print("symmetric difference",s1^s2)

