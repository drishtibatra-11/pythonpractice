#write a program to check whether all the values in a dictionary are same or not using lambda function..
check_same = lambda d: len(set(d.values())) == 1
my_dict = {"a": 10, "b": 10, "c": 10, "d": 10}
print(check_same(my_dict))
