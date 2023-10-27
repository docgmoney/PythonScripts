import random

print("Number Guesser")
chosen_number = random.randint(0, 10)  
attempts = 0
print("Guess the number between 0 and 10 \n")

while True:  # Allow multiple attempts
    # Ask for users guess
    guess = int(input("Enter your guess: \n"))

    if guess >= 11or guess < 0:  # Adjusted the condition to check for negative numbers
        print("Please choose a valid number between 0 and 10. Exiting game.")
        exit()
    else:
        print("Thank you for your guess of", guess)

    attempts += 1

    # Check the guess
    if guess == chosen_number:
        print("Congrats You have WON 👑🏆🏆🏆👑")
        print(f"It took you {attempts} attempts to guess the correct number.")
        break
    elif guess < chosen_number:
        print(guess, "is too LOW🎲🎲🎲")
    else:
        print(guess, "is too HIGH🎈🎈🎈")
