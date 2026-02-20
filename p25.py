#scan n values in range 0 to 3 and print the number of times each value is entered
values = {}
for i in range(5):
    value = int(input("Enter a value between 0 and 3: "))
    if value in values:
        values[value] += 1
    else:
        values[value] = 1
print("Value counts: ", values)

