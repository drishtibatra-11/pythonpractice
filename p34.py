#count total numberof vowels in a given string.
string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0

for ch in string:
    if ch in vowels:
        count += 1

print("Total number of vowels:", count)