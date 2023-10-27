import random, os, time

# Create Bingo Card "Library"
bingo = []

def ran():
    rnumber = random.randint(1, 90)
    while rnumber in numbers:  # Ensure unique numbers
        rnumber = random.randint(1, 90)
    return rnumber

# Pretty print to tab and place | inbetween each int
def prettyPrint():
    for row in bingo:
        for item in row:
            print(item, end="\t|\t")
        print()

# Defining the card itself and creating it
def createCard():
    global bingo
    global numbers
    numbers = []

    for _ in range(8):
        numbers.append(ran())

    numbers.sort()

    # Formatting the card
    bingo = [
        [numbers[0], numbers[1], numbers[2]],
        [numbers[3], "BG", numbers[4]],
        [numbers[5], numbers[6], numbers[7]]
    ]

createCard()  # Create the initial bingo card

# Printing the Card
while True:
    os.system("clear")  # Clear the console for better visibility
    prettyPrint()
    num = int(input("What number was drawn?! \n"))
    
    for row in range(3):
        for item in range(3):
            if bingo[row][item] == num:
                bingo[row][item] = 'X'
                time.sleep(1.5)

    # Counter for win condition
    counter = 0
    for row in bingo:
        for item in row:
            if item == "X":
                counter += 1
    if counter == 8:
        print("You win Bingo!")
        break
