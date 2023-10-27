import random

def rollDice():
    side0 = 6
    side1 = 12
    roll0 = random.randint(1, side0)
    roll1 = random.randint(1, side1)
    health_roll = roll0 * roll1
    print(name, "the", char_class, ".You rolled a ", health_roll, "for your health!")
    return roll0, roll1, health_roll

while True:
    name = input("What is your character's name?: \n")
    char_class = input("What class are you? \n")
    roll = input("Ready to roll stats? y/n \n")

    if roll == "y":
        roll0, roll1, health_roll = rollDice()
        # Health for NPC
        health = (health_roll / 2) + 10
        # Roll stats Strength
        strength = ((roll0 * roll1) / 2) + 12
        print(name, "you rolled", strength, "for your strength stat. \n")
    else:
        print("You chose not to roll.")
  
    another = input("Do you want to generate another NPC? y/n ?: \n")
    if another != 'y':
        break
