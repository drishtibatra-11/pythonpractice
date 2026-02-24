n = int(input("Enter number of students: "))
students = {}

# Input details
for i in range(n):
    name = input("Enter name: ")
    city = input("Enter city: ")
    students[name] = city

while True:
    print("\n---- MENU ----")
    print("1. Display all names")
    print("2. Display all city names")
    print("3. Display student name and city")
    print("4. Count students in each city")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Student Names:")
        for name in students.keys():
            print(name)

    elif choice == "2":
        print("City Names:")
        for city in students.values():
            print(city)

    elif choice == "3":
        print("Student Details:")
        for name, city in students.items():
            print(name, "lives in", city)

    elif choice == "4":
        city_count = {}
        for city in students.values():
            city_count[city] = city_count.get(city, 0) + 1
        
        print("Number of students in each city:")
        for city, count in city_count.items():
            print(city, ":", count)

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")