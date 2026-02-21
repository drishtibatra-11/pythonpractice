#7. Create 2 sets s1 and s2 of n fruits each by taking input from user and find:
#a) Fruits which are in both sets s1 and s2
#b) Fruits only in s1 but not in s2
# c)countof all fruits from s1 and s2
n = int(input("Enter number of fruits in each set: "))

s1 = set()
s2 = set()

print("Enter fruits for Set 1:")
for i in range(n):
    s1.add(input())

print("Enter fruits for Set 2:")
for i in range(n):
    s2.add(input())

# a) Fruits in both sets
print("Common fruits:", s1.intersection(s2))

# b) Fruits only in s1
print("Fruits only in Set 1:", s1.difference(s2))

# c) Count of all fruits from s1 and s2
all_fruits = s1.union(s2)
print("Total distinct fruits:", len(all_fruits))




