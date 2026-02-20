#count number of unique words in a sentence
sentence=input("enter a sentence: ")
words=sentence.split()
unique_words=set(words)
print("number of unique words: ",len(unique_words))