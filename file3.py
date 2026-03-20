
f = open("name.txt", "w")
f.write("Aman\nRiya\nIshita\nOm\nAnkit\n")
f.close()
f = open("name.txt", "r")
names = f.readlines()
print("Total names:", len(names))
f.close()
f = open("name.txt", "r")
count = 0
for name in f:
    if name[0].lower() in "aeiou":
        count += 1

print("Names starting with vowel:", count)
f.close()
f = open("name.txt", "r")
longest = ""

for name in f:
    name = name.strip()
    if len(name) > len(longest):
        longest = name
print("Longest name:", longest)
f.close()