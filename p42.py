#Create a tuple to store n numeric values and find average
n = int(input("Enter the number of numeric values to store: "))
values = []

for i in range(n):
    value = float(input(f"Enter value {i+1}: "))
    values.append(value)

numeric_tuple = tuple(values)
average = sum(numeric_tuple) / len(numeric_tuple)
print(f"Tuple: {numeric_tuple}")
print(f"Average: {average}")