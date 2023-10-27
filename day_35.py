import time
import os

# Initialize an empty list and a dictionary for mapping numerical codes to items
todo_list = []
item_map = {}
counter = 0  # Initialize a counter to keep track of the codes

def get_menu_choice():
    choice = input("""Do you want to 
    1. View an item from the to do list?
    2. Add an item to the to do list?
    3. Edit an item from the to do list?
    4. Remove an item from the to do list?\n""").lower()
    return choice

def print_list():
    if not todo_list:
        print("The to-do list is empty.")
    else:
        for code in todo_list:
            print(f"{code}: {item_map[code]}")

def execute_choice(choice):
    global counter  # Declare counter as global so we can modify it
    if choice == "view" or choice == "1":
        print_list()
    elif choice == "add" or choice == "2":
        item = input("What do you want to add?\n")
        code = counter  # Use the current value of counter as the code
        todo_list.append(code)
        item_map[code] = item
        counter += 1  # Increment counter for the next item
        print(f"\033[32m{item}\033[0m")  # Text will be green
        time.sleep(1)  # Sleep for 1 second
        os.system('clear')  # Clear the terminal (Unix)
    elif choice == "remove" or choice == "4":
        print_list()
        code = int(input("Enter the number of the item you want to remove:\n"))
        if code in todo_list:
            confirmation = input(f"Are you sure you want to remove: {item_map[code]}? (yes/no)\n").lower()
            if confirmation == 'yes' or confirmation == 'y':
                print(f"\033[31mRemoving: {item_map[code]}\033[0m")  # Text will be red
                time.sleep(1)  # Sleep for 1 second
                os.system('clear')  # Clear the terminal (Unix)
                todo_list.remove(code)
                del item_map[code]
            else:
                print("Item not removed.")
        else:
            print("Item not found!")
    elif choice == "edit" or choice == "3":
        print_list()
        code = int(input("Enter the number of the item you want to edit:\n"))
        if code in todo_list:
            new_item = input(f"Editing: {item_map[code]}\nEnter the new item:\n")
            print(f"\033[32m{new_item}\033[0m")  # Text will be green
            time.sleep(1)  # Sleep for 1 second
            os.system('clear')  # Clear the terminal (Unix)
            item_map[code] = new_item  # Update the item in item_map
        else:
            print("Item not found!")
    else:
        print("Invalid choice. Please try again.")

while True:
    choice = get_menu_choice()
    execute_choice(choice)
