list1 =[]
list2=[]
n=int(input("Enter number of elements in list: "))
for i in range(n):
    list1.append(int(input("Enter key: ")))
    for i in range(n):
        list2.append(int(input("Enter value: ")))
        result_dict = dict(zip(list1, list2))
        print(result_dict)