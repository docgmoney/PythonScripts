from getpass import getpass as input
print("R,S,P! GO!!!")

# Getting information to set up the game
player1 = input("Are you ready player one?: \n")
if player1 == "yes":
    choice1 = int(input("""Great! What is your choice?:
1.Rock
2.Paper
3.Scissors \n"""))
else:
    print("Lame! Why would you start this then?!")
    exit()  # exit the program if player1 is not ready

player2 = input("Are you ready player two?: \n")
if player2 == "yes":
    choice2 = int(input("""Great! What is your choice?:
1.Rock
2.Paper
3.Scissors \n"""))
else:
    print("Lame! Why would you start this then?!")
    exit()  # exit the program if player2 is not ready

# Playing the game
if choice1 == choice2:
    print("It's a Tie 👔")
elif (choice1 == 1 and choice2 == 3) or \
     (choice1 == 2 and choice2 == 1) or \
     (choice1 == 3 and choice2 == 2):
    print("PLAYER 1 WINS!!! 🏆🏆🏆")
else:
    print("Player 2 Wins!!! 🏆🏆🏆")