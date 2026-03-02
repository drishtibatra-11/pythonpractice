#1.     Write a Python function to find the maximum and minimum numbers from a sequence of numbers.
def find_max_min(numbers):
    if len(numbers) == 0:
        return None
    
    maximum = numbers[0]
    minimum = numbers[0]
    
    for num in numbers:
        if num > maximum:
            maximum = num
        if num < minimum:
            minimum = num
            
    return maximum, minimum
 
numbers = [3, 1, 4, 1, 5, 9]
max_num, min_num = find_max_min(numbers)
print(f"Maximum: {max_num}, Minimum: {min_num}")
