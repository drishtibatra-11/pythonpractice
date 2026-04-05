n = int(input("enter number of test cases: "))

for _ in range(n):
    try:
        a, b = input().split()
        result = int(a) // int(b)
        print(result)

    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")

    except ValueError as e:
        print("Error Code:", e)