#dice roller
import random
print("Welcome to the Custom Dice Roller!")
def rollDice():
    sides = int(input("How many sides does the die have?: \n"))
    roll = random.randint(1,sides)
    print("You rolled a ", roll)
rollDice()
#start the exit loop
i = "y"
while i == "y":
    rollDice()
    i = input("Do you want to roll again?: y/n \n")
          