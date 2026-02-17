n = int(input("Enter value of n: "))
total = 0

for i in range(1, n + 1):
    total += 1 / i

print("Sum =", total)