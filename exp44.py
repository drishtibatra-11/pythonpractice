s = input("entera string")
s=s.upper()
letters={}
for ch in s:
    if ch is alpha:
        letters[ch]=letters.get(ch,0)+1
        for key is sorted(letters):
            print(key,letters[key])