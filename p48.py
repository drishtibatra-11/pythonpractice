#Write a Python function to find the maximum and minimum numbers from a sequence of
numbers
def max_min(numbers):
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    return max_num, min_num

numbers = [1, 2, 3, 4, 5]
max_val, min_val = max_min(numbers)
print("Maximum number:", max_val)
print("Minimum number:", min_val)