import time
import os
#Screw this color shit its not just a flesh wound to the colorblind!

# Function to get the ANSI escape code based on the letter
def get_ansi_color(letter):
    colors = {'r': '\033[91m',  # Red
              'b': '\033[94m',  # Blue
              'g': '\033[92m',  # Green
              'p': '\033[95m',  # Purple
              'y': '\033[93m',  # Yellow
              'reset': '\033[0m'}  # Reset color

    return colors.get(letter, '')

import time
import os

# Function to get the ANSI escape code based on the letter
def get_ansi_color(letter):
    colors = {'r': '\033[91m',  # Red
              'b': '\033[94m',  # Blue
              'g': '\033[92m',  # Green
              'p': '\033[95m',  #Purple
              'y': '\033[93m',  # Yellow
              'reset': '\033[0m'}  # Reset color

    return colors.get(letter, '')

while True:
    # Input from the user
    input_sentence = input("Enter a sentence (type 'exit' to quit): \n")

    if input_sentence.lower() == 'exit':
        break

    # Initialize variables
    current_color = ''  # Default color

    # Loop through the input sentence
    for letter in input_sentence:
        if letter in 'rbgpy':
            new_color = get_ansi_color(letter)
            if new_color != current_color:
                current_color = new_color
                print(current_color, end='')
        elif letter == ' ':
            current_color = get_ansi_color('reset')  # Reset color for spaces
            print(current_color, end='')
        print(letter, end='')

    # Reset color at the end
    print(get_ansi_color('reset'))

    # Sleep for 5 seconds
    time.sleep(5)

    # Clear the console (works on Unix-based systems)
    os.system('clear')

# End of the program
print("Goodbye!")
