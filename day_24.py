import random

def rollDice(sides):
    return random.randint(1, sides)

# Asks for die size
num_sides = int(input("How many sides does your dice have? "))

while True:
    print(f"You rolled a {rollDice(num_sides)}!")
    
    # Ask the user for the next action
    choice = int(input("""
    What would you like to do?:
    1. Roll again
    2. Select a new die to roll
    3. Quit
    """))
    
    if choice == 1:
        continue
    elif choice == 2:
        num_sides = int(input("How many sides does your dice have? "))
    elif choice == 3:
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
