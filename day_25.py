import random

def rollDice():
    side0 = 6
    side1 = 8
    roll0 = random.randint(1, side0)
    roll1 = random.randint(1, side1)
    print(name, "the", char_class, ".You rolled a ", roll0 * roll1, "for your health!")

name = input("What is your character's name?: \n")
char_class = input("What class are you? ")
roll = input("Roll your health? y/n \n")

if roll == "y":
    rollDice()
