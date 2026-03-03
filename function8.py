#Write a program to check whether all the values in a dictionary are same or not using lambda function
my_dict = {"a": 100, "b": 100, "c": 100}

check_same = lambda d: len(set(d.values())) == 1

print(check_same(my_dict))   # True