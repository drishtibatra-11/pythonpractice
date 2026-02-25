#count occurences of each element
string=input("enter a string: ")
for ch in sorted(set(string)):
    print(ch, "occurs", string.count(ch), "times")
