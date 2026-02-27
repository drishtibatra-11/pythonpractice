#program to count number of unique characters in a string
string = input("Enter a string: ")
unique_characters = set(string)
print("number of unique characters: ", len(unique_characters))