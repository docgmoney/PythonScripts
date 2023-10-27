import random
import time
import os

# Initialize both count and list... will be changed to a txt file later...
ideas = []

while True:
    menu = int(input("""What would you like to do?
                     1. Add a GREAT idea to the list.
                     2. See the Grand List of IDEAS!!!
                     3. See 1 random Idea from your list.
                     4. Quit: \n"""))

    if menu == 1:
        idea = input("What is your great idea this time Einstein?: \n")
        ideas.append(idea)
        print("Logging... Your Grand Idea has been logged...")

        # Open the file in "append" mode and write the new idea
        with open("ideas.txt", "a+") as f:
            f.write(idea + "\n")  # Write the idea followed by a newline

    elif menu == 2:
        print("Grand List of IDEAS!!!: \n")
        
        # Open the file in "read" mode and read its content into the ideas list
        with open("ideas.txt", "r") as f:
            ideas = f.readlines()

        # Print the list of ideas
        for idea in ideas:
            print(idea)

    elif menu == 3:
            with open("ideas.txt", "r") as f:
                ideas = f.read().splitlines()
            random_idea = random.choice(ideas)
            print(f"Random Idea: {random_idea}")
    elif menu == 4:
        break
    else:
        print("Invalid choice. Please choose a valid option.")
