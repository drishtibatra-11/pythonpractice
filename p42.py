#Create a tuple to store n numeric values and find average
n = int(input("Enter number of values: "))
values = []

for i in range(n):
    num = float(input("Enter number: "))
    values.append(num)

numbers = tuple(values)
average = sum(numbers) / len(numbers)

print("Tuple:", numbers)
print("Average:", average)