print("Movie Quote Game")

# Counter to count how many wrong answers
counter = 0

# Question 1
answer = input("\"It's just a _____ wound.\" - Monty Python and the Holy Grail\nYour answer: ")
if answer != "flesh":
    counter += 1

# Question 2
answer = input("\"I ____ in your general direction!\" - Monty Python and the Holy Grail\nYour answer: ")
if answer != "fart":
    counter += 1

# Question 3
answer = input("\"What have the ______ ever done for us?\"- Life of Brian\nYour answer: ")
if answer != "Romans":
    counter += 1

# Question 4
answer = input("\"Your mother was a hamster and your father _____ of elderberries!\" - Monty Python and the Holy Grail\nYour answer: ")
if answer != "smelt":
    counter += 1

# Question 5
answer = input("\"Bring out yer ____!\" - Monty Python and the Holy Grail\nYour answer: ")
if answer != "dead":
    counter += 1

# Print the results
print("You got", counter, "questions wrong.")
