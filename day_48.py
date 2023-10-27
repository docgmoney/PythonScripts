import os
import time
import random

while True:

    menu = int(input("""What would you like to do?
                     1. Add to the high score list.
                     2. View the high score list.
                     3. Quit \n"""))

    if menu == 1:
        name = input("3 initials you want to be known as: ").upper()
        score = random.randint(1, 100000)
        print()

        f = open("high_scores", "a+")
        f.write(f"{name} {score}\n")
        f.close()

        print("Added")
        print(f"{name} you got a high score of {score}!")
        time.sleep(1.5)

        # Clear the screen
        os.system("clear")

    elif menu == 2:
        print("High Scores")
        with open("high_scores", "r") as f:
            lines = f.readlines()  # Read all lines from the file
            # Split each line into name and score, convert score to int for sorting
            scores = [(line.strip().split()[0], int(line.strip().split()[1])) for line in lines]
            # Sort scores in descending order
            sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
            
            # Print the sorted scores
            for name, score in sorted_scores:
                print(f"{name}: {score}")

    elif menu == 3:
        break  # Exit the loop and end the program
