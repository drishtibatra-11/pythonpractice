tasks = []

while True:
    print("\n1.Add Task 2.View Tasks 3.Remove Task 4.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            print(i, task)

    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            tasks.pop(task_no - 1)
        else:
            print("Invalid task number")

    elif choice == "4":
        break