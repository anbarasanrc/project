tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def view_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(i+1, task)

def delete_task():
    view_tasks()
    if tasks:
        task_index = int(input("Enter task number to delete: "))
        if task_index > 0 and task_index <= len(tasks):
            tasks.pop(task_index-1)
            print("Task deleted.")
        else:
            print("Invalid input.")
    else:
        print("No tasks to delete.")

# main program loop
while True:
    print("\nSelect option:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    option = input("Enter option number: ")

    if option == '1':
        add_task()

    elif option == '2':
        view_tasks()

    elif option == '3':
        delete_task()

    elif option == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid input.")
