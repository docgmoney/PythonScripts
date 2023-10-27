import random

# Hangman
print("Welcome to 21st Century Hangman!\n")
menu = int(input("""What would you like to do?
1. Play a game of hangman
2. Quit\n"""))

while menu == 1:
    while True:  # Start a loop for a single game
        # Start the counter for drawing
        counter = 0

        # Creates the list of words the executioner knows
        listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

        # Picks a random word from the listOfWords
        word = random.choice(listOfWords).lower()  # Convert the word to lowercase for easier comparison

        # Create a set to store guessed letters
        guessed_letters = set()

        while counter < 6:
            # Display the current state of the word with underscores for unknown letters
            display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
            print("Word:", display_word)

            # Check if there are no underscores left in the word
            if '_' not in display_word:
                print("Congratulations, you won! The word was:", word)
                break  # Exit the game loop when all letters are guessed correctly

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input. Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You've already guessed that letter.")
            elif guess in word:
                print("Correct!")
                guessed_letters.add(guess)
            else:
                print("Incorrect!")
                counter += 1

            if counter == 6:
                print("Sorry, you lose! The word was:", word)
                break  # Exit the game loop when the player loses

        menu_choice = input("What would you like to do?\n1. Play another game of hangman\n2. Quit\n")
        
        if menu_choice != '1':
            break  # Exit the game loop if the player chooses to quit

    menu = int(input("What would you like to do?\n1. Play a game of hangman\n2. Quit\n"))

print("Thank you for playing Hangman!")
