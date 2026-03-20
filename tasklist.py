def manage_tasks():
    tasks = []
    while True:
        print("\n===== Task List =====")
        print("[1] Add a task")
        print("[2] View all tasks")
        print("[3] Remove a task")
        print("[0] Return to main menu")

        choice = input("Select an option: ")

        if choice == "1":
            task = input("Enter task: ")
            tasks.append(task)
            print(f"Task '{task}' added.")
        elif choice == "2":
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks yet.")
        elif choice == "3":
            if tasks:
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Task '{removed}' removed.")
                else:
                    print("Invalid number.")
            else:
                print("No tasks to remove.")
        elif choice == "0":
            break
        else:
            print("Invalid option.")
