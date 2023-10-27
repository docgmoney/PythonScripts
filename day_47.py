import os
import time
import random

# Dictionary to store user data
trumps = {}

def load_users_from_file(filename='users.txt'):
    if not os.path.exists(filename):
        return
    
    with open(filename, 'r') as file:
        for line_num, line in enumerate(file.readlines(), start=1):
            try:
                username, i, j, k, l, w = line.strip().split(',')
                trumps[username] = {"Intelligence": int(i), "Speed": int(j), "Guile": int(k), "Style": int(l), "Wins": int(w)}
            except ValueError as e:
                print(f"Error on line {line_num}: {str(e)}. Skipping malformed line: {line.strip()}")

def save_users_to_file(filename='users.txt'):
    with open(filename, 'w') as file:
        for username, stats in trumps.items():
            line = f"{username},{stats['Intelligence']},{stats['Speed']},{stats['Guile']},{stats['Style']},{stats['Wins']}\n"
            file.write(line)

def create_user():
    username = input("Enter your username: ")
    trumps[username] = {"Intelligence": 0, "Speed": 0, "Guile": 0, "Style": 0, "Wins": 0}
    for stat in ["Intelligence", "Speed", "Guile", "Style"]:
        input(f"Press [Enter] to roll for {stat}...")
        trumps[username][stat] = random.randint(1, 100)
        print(f"{stat}: {trumps[username][stat]}")
    save_users_to_file()
    return username

def select_user():
    load_users_from_file()
    print("Available users: ")
    for username in trumps.keys():
        print(username)
    while True:
        selected_user = input("Choose a user: ")
        if selected_user in trumps:
            return selected_user
        else:
            print("User not found. Try again.")

def battle(user1, user2):
    score1 = sum(trumps[user1].values())
    score2 = sum(trumps[user2].values())
    
    print(f"\n{user1} vs {user2}\nFight!\n")
    time.sleep(5)
    
    if score1 > score2:
        winner, loser = user1, user2
    elif score2 > score1:
        winner, loser = user2, user1
    else:
        print("\nIt's a tie!\n")
        return
    
    trumps[winner]["Wins"] += 1
    save_users_to_file()
    print(f"\n\033[92m{winner} wins!\033[0m (Win streak: {trumps[winner]['Wins']})")
    print(f"\033[91m{loser} loses.\033[0m")
    del trumps[loser]
    save_users_to_file()

# Main script logic
while True:
    action = input("\nDo you want to continue? (yes/no) ")
    if action.lower() != 'yes':
        break
    
    print("\nPlayer 1, get ready!")
    action = input("Do you want to [load] a user or [create] a new one? ")
    user1 = select_user() if action.lower() == 'load' else create_user()
    
    print("\nPlayer 2, get ready!")
    action = input("Do you want to [load] a user or [create] a new one? ")
    user2 = select_user() if action.lower() == 'load' else create_user()
    
    battle(user1, user2)
