#Scan n values in range 0–3 and print the number of times each value has occurred
n = int(input("Enter the number of values to scan: "))
count = [0, 0, 0, 0]  # Initialize counts for values 0 to 3

for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    if 0 <= value <= 3:
        count[value] += 1
    else:
        print("Value out of range (0-3). Ignoring.")

print("Counts for each value:")
for i in range(4):
    print(f"Value {i}: {count[i]} times")