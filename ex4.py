s=input("enter a string: ")
count=0
for ch in s:
    if ch.isupper():
        count+=1
print("number of uppercase letters: ",count)