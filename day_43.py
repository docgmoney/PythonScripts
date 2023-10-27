import random

bingo = []

# Using random function to get new numbers for the card
def ran():
    number = random.randint(1, 90)
    return number

# Pretty print
def prettyPrint():
    for row in bingo:
        print(row)

numbers = []

# Generate 8 random numbers
for i in range(8):
    numbers.append(ran())

# Sort the numbers
numbers.sort()

# Create a 3x3 "Bingo" card
bingo = [
    [numbers[0], numbers[1], numbers[2]],
    [numbers[3], "Bingo", numbers[4]],
    [numbers[5], numbers[6], numbers[7]]
]

# Display the Bingo card as a table
prettyPrint()
