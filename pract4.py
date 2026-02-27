#count and display the number of capital letters in a string
string = input("Enter a string: ")
count=0
for ch in string:
    if ch.upper() == ch:
        count+=1
print("number of capital letters: ",count)