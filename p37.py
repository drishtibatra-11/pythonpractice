#Given a string containing both upper and lower case alphabets. Write a Python
#program to count the number of occurrences of each alphabet (case insensitive) and display the same.
string = input("Enter a string: ")
string = string.upper()

count_dict = {}

for ch in string:
    if ch.isalpha():
        count_dict[ch] = count_dict.get(ch, 0) + 1

for key in sorted(count_dict):
    print(str(count_dict[key]) + key)