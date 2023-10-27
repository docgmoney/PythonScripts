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
myEvents = []

#f = open("calander.txt", "r")
#myEvents = eval(f.read())
#f.close()

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
        date = input("What is the date of the event \n")
        myEvents.append([item, rating, date])
        myEvents.sort(key=lambda x: x[1])  # Sort by rating
        print(myEvents)
        time.sleep(3)
        os.system("clear")

    # Editing the list
    elif menu == 2:
        item_to_edit = input("What would you like to edit? \n")
        for item_rating in myEvents:
            item, rating = item_rating
            if item == item_to_edit:
                new_item = input("What would you like to change it to? ")
                new_rating = int(input("What's the NEW rating (1-5)? "))
                new_date = input("What is the NEW date of the event \n")
                myEvents.remove(item_rating)
                myEvents.append([new_item, new_rating, new_date])
                myEvents.sort(key=lambda x: x[1])  # Sort by rating
                print(myEvents)

    elif menu == 3:
        print("Your List:")
        for item_rating in myEvents:
            item, rating, date = item_rating
            print(f"{COLORS.get(rating, '')}{item} (Rating: {rating}, Date: {date}){RESET_COLOR}")
        time.sleep(5)
        input("Press Enter to continue...")
        os.system("clear")

    # Deleting an item from the list
    elif menu == 4:
        item_to_delete = input("What would you like to delete? \n")
        for item_rating in myEvents:
            item, rating = item_rating
            if item == item_to_delete:
                myEvents.remove(item_rating)
                print(myEvents)

    # Quitting the program
    elif menu == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid input. Please choose a valid option.")

    f = open("calander.txt", "w")
    f.write(str(myEvents))
    f.close