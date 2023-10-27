from getpass import getpass as input

print("Rock. Paper, Scissors!!!")
print("First to 3 wins")

# Keeping the score
count = 0
count1 = 0

# Loop continues until one of the players gets 3 wins
while count < 3 and count1 < 3:
  
# Getting information to set up the game
    choice1 = int(input("""Great! Player 1 what is your choice?:
1.Rock
2.Paper
3.Scissors \n"""))
    
    choice2 = int(input("""Great! Player 2 what is your choice?:
1.Rock
2.Paper
3.Scissors \n"""))

# Playing the game
    if choice1 == choice2:
        print("It's a Tie 👔")
    elif (choice1 == 1 and choice2 == 3) or \
         (choice1 == 2 and choice2 == 1) or \
         (choice1 == 3 and choice2 == 2):
        print("PLAYER 1 WINS this round! 🏆")
        count += 1
    else:
        print("Player 2 Wins this round! 🏆")
        count1 += 1

# Ending the game
if count == 3:
    print("PLAYER 1 WINS THE GAME!!! 🏆🏆🏆")
elif count1 == 3:
    print("Player 2 Wins THE GAME!!! 🏆🏆🏆")
else:
    print("Game ended prematurely!")