#create dictionary to store n key value pairs and print the dictionary
students={}
n=int(input("enter number of students: "))
for i in range(n):
    name=input("enter name of student: ")
    city=int(input("enter score of student: "))
    students[name]=city
    print("students: ",students.keys())
    print("scores: ",students.values())
    