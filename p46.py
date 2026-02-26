#practice
contacts = {}

while True:
    print("\n1.Add 2.Search 3.Update 4.Delete 5.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Enter name to search: ")
        print("Phone:", contacts.get(name, "Not found"))

    elif choice == "3":
        name = input("Enter name to update: ")
        if name in contacts:
            contacts[name] = input("Enter new phone: ")
        else:
            print("Contact not found")

    elif choice == "4":
        name = input("Enter name to delete: ")
        contacts.pop(name, "Not found")

    elif choice == "5":
        break