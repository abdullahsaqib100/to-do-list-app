# Creating an empty list to store tasks

tasks = []

# Creating a fuction to display all the tasks

def show_tasks():
    if len(tasks) == 0:
        print("No task is present.")
    
    else:
        print("Your Tasks: ")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}" )

# Creating a function to add a task

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("f Task '{task}' is added")

# Creating a function to remove a task

def remove_task():
    show_tasks()
    task_num_to_remove = int(input("Enter the task number you want to remove: "))
    if 0 < task_num_to_remove <= len(tasks):
        removed_task = tasks.pop(task_num_to_remove - 1)
        print(f" Task '{task_num_to_remove}' is removed")

    else:
        print("You entered an invalid task number.")


# Creating a function to show the main menu of to-do list app 

def show_menu():
    print("\nTo-Do List App")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

# Creating a loop to remain in the app

while True:
    show_menu()
    choice = input("Enter an option:")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Existing the App, GoodBye!") 
        break
    else:
        print("Enter a valid choise & Try Again")

    



