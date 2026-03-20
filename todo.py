 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

tasks = []

while True:
    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            num = int(input("Enter task number to delete: "))
            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number!")

    elif choice == "4":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice! Please try again.")

