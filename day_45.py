import os
import time

# ANSI color codes
COLORS = {
    1: '\033[93m',  # Gold (yellow)
    2: '\033[91m',  # Red
    3: '\033[33m',  # Orange
    4: '\033[92m',  # Green
    5: '\033[94m',  # Blue
}
RESET_COLOR = '\033[0m'

# Life Organizer
print("Organize Your Life!")

# Creating a list to store items and ratings
organizer_list = []

# Creating a menu to loop through...
while True:
    menu = int(input("""What would you like to do? 
    1. Add to your list
    2. Edit an item on your list
    3. View the list
    4. Delete an item on your list
    5. QUIT \n"""))

    # Adding to the list
    if menu == 1:
        item = input("What would you like to add? \n")
        rating = int(input("Rate its importance (1-5): \n"))
        organizer_list.append([item, rating])
        organizer_list.sort(key=lambda x: x[1])  # Sort by rating
        print(organizer_list)
        time.sleep(3)
        os.system("clear")

    # Editing the list
    elif menu == 2:
        item_to_edit = input("What would you like to edit? \n")
        for item_rating in organizer_list:
            item, rating = item_rating
            if item == item_to_edit:
                new_item = input("What would you like to change it to? ")
                new_rating = int(input("What's the new rating (1-5)? "))
                organizer_list.remove(item_rating)
                organizer_list.append([new_item, new_rating])
                organizer_list.sort(key=lambda x: x[1])  # Sort by rating
                print(organizer_list)

    elif menu == 3:
        for item, rating in organizer_list:
            print(f"{COLORS.get(rating, '')}{item} (Rating: {rating}){RESET_COLOR}")
        time.sleep(5)
        os.system("clear")

    # Deleting an item from the list
    elif menu == 4:
        item_to_delete = input("What would you like to delete? \n")
        for item_rating in organizer_list:
            item, rating = item_rating
            if item == item_to_delete:
                organizer_list.remove(item_rating)
                print(organizer_list)

    # Quitting the program
    elif menu == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please choose a valid option.")
