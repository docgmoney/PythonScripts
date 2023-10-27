to_do_list = []

while True:
    menu = int(input("""Would you like to:
1. Add to the To-Do List
2. Cross off or Remove from List
3. Print the list and exit the program
Please enter the corresponding number: \n"""))

    if menu == 1:
        task = input("What task would you like to add to the list?: ")
        to_do_list.append(task)
    elif menu == 2:
        if not to_do_list:
            print("The list is empty. Nothing to remove.")
        else:
            print("Current To-Do List:")
            for i, task in enumerate(to_do_list):
                print(f"{i + 1}. {task}")
            task_index = int(input("Enter the number of the task you want to remove: ")) - 1

            if task_index >= 0 and task_index < len(to_do_list):
                removed_task = to_do_list.pop(task_index)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number.")
    elif menu == 3:
        if not to_do_list:
            print("The list is empty.")
        else:
            print("Current To-Do List:")
            for i, task in enumerate(to_do_list):
                print(f"{i + 1}. {task}")
        print("Thank you for using the To-Do Manager!")
        break
    else:
        print("Invalid input. Please enter a valid option (1, 2, or 3).")
