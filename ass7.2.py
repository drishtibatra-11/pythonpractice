with open("numbers.txt", "r") as f:
    nums = [int(line.strip()) for line in f]

# a. Max number
print("Max:", max(nums))

# b. Average
avg = sum(nums) / len(nums)
print("Average:", avg)

# c. Count > 100
count = sum(1 for n in nums if n > 100)
print("Numbers > 100:", count)