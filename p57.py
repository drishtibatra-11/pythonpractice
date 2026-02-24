def create_dictionary(list1, list2):
    return dict(zip(list1, list2))
list1 = input("Enter keys separated by space: ").split()
list2 = input("Enter values separated by space: ").split()
result = create_dictionary(list1, list2)
print("Generated Dictionary:", result)