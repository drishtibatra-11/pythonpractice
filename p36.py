#WAP to enter a string and a substring. You have to print the number of times
#that the substring occurs in the given string. String traversal will take place from
#eft to right, not from right to left.
string = input("Enter main string: ")
substring = input("Enter substring: ")

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1

print(count)