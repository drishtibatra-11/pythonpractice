with open("city.txt", "r") as f:
    cities = [line.split() for line in f]

# a. Display all
print("All cities:")
for c in cities:
    print(c[0], c[1], c[2])

# b. Population > 10 lakhs
print("Cities with population > 10 lakhs:")
for c in cities:
    if float(c[1]) > 10:
        print(c[0])

# c. Sum of areas
total_area = sum(float(c[2]) for c in cities)
print("Total area:", total_area)