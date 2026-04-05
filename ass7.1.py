
with open("name.txt", "r") as f:
    names = [line.strip() for line in f]

print("Total names:", len(names))

vowels = "AEIOUaeiou"
count_vowel = sum(1 for name in names if name[0] in vowels)
print("Names starting with vowel:", count_vowel)

longest = max(names, key=len)
print("Longest name:", longest)