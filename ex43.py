#count occurrence of each word in a sentence
substring=input("enter a substring: ")
sentence=input("enter a sentence: ")
count=0
while True:
       pos=sentence.find(substring,start)
    if pos == -1:
        break
    count+=1
    start=pos +1
print("number of occurrences: ",count)