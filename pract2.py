#count the unique words in a string
string=input("enter a string: ")
words=string.split()
unique_words=set(words)
print("number of unique words: ",len(unique_words))