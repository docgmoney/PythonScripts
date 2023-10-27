#Npc Battle
import random
import time
import os
from getpass import getpass as input

def rollDice(sides=6):
    return random.randint(1, sides)

def createCharacter(player_name):
    print(f"Creating {player_name}...\n")
    name = input(f"{player_name}, what is your character's name?: \n")
    char_class = input(f"{player_name}, what class are you? \n")
    roll = input(f"{player_name}, roll your stats? (y/n/max) \n")

    side0, side1 = 6, 12
    
    if roll == "y":
        roll0, roll1 = random.randint(1, side0), random.randint(1, side1)
        health_roll = roll0 * roll1
        health = (health_roll / 2) + 10
        strength = ((roll0 * roll1) / 2) + 12
    elif roll == "max":
        health_roll = side0 * side1
        health = (health_roll / 2) + 10
        strength = ((side0 * side1) / 2) + 12
    else:
        health = ((side0 + side1) / 2) + 9
        strength = ((side0 + side1) / 2) + 11

    print(f"{name} the {char_class}. Health: {health}, Strength: {strength}\n")
    time.sleep(5)
    os.system("clear")
    return {"name": name, "class": char_class, "health": health, "strength": strength}

character1 = createCharacter("Player 1")
character2 = createCharacter("Player 2")
consecutive_wins = {"Player 1": 0, "Player 2": 0}

while True:
    # Battle countdown
    for i in range(5, 0, -1):
        print(f"Battle starts in {i}...")
        time.sleep(1)
    os.system("clear")

    # Simulate the battle
    char1_roll = rollDice()
    char2_roll = rollDice()

    if char1_roll > char2_roll:
        damage = abs(character1["strength"] - character2["strength"]) // 2  # Every 2 points of strength gives 1 damage
        character2["health"] -= damage
        print(f"{character1['name']} wins this round and deals {damage} damage!")
        consecutive_wins["Player 1"] += 1
        consecutive_wins["Player 2"] = 0
    elif char2_roll > char1_roll:
        damage = abs(character2["strength"] - character1["strength"]) // 2
        character1["health"] -= damage
        print(f"{character2['name']} wins this round and deals {damage} damage!")
        consecutive_wins["Player 2"] += 1
        consecutive_wins["Player 1"] = 0
    else:
        print("It's a tie!")

    print(f"{character1['name']} Health: {character1['health']}")
    print(f"{character2['name']} Health: {character2['health']}")

    if character1["health"] <= 0:
        print(f"{character2['name']} wins the battle! 🎉")
        if consecutive_wins["Player 2"] == 3:
            print(f"\n🐀 {character2['name']} is now the Rat King! 🐀")
            print("And now for something completely different... a man with three buttocks!")
        # Prompt to create a new character
        response = input("Would Player 1 like to create a new character to challenge the champion? (y/n): ")
        if response == 'y':
            character1 = createCharacter("Player 1")
        else:
            break
    elif character2["health"] <= 0:
        print(f"{character1['name']} wins the battle! 🎉")
        if consecutive_wins["Player 1"] == 3:
            print(f"\n🐀 {character1['name']} is now the Rat King! 🐀")
            print("And now for something completely different... a man with a tape recorder up his nose!")
        # Prompt to create a new character
        response = input("Would Player 2 like to create a new character to challenge the champion? (y/n): ")
        if response == 'y':
            character2 = createCharacter("Player 2")
        else:
            break

    input("\nPress enter to proceed to the next round.")
