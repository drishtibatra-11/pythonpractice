#give a string containing both wap to count number of occurences of each character in the string
string = input("Enter a string: ")
count=0
for ch in sorted(set(string)):
    count=string.count(ch)
    print(ch,":",count)