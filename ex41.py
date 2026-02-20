#total no of vowels in a string
s=input("enter a string: ")
vowels="aeiouAEIOU"
count=0
for ch in s:
    if ch in vowels:
        count+=1
print("number of vowels: ",count)
