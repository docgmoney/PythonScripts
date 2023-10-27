print("Multiplication Game")
name = input("What is your name?")
table = int(input("""Which table would you like to compete on?
1's times table
2's times table
3's times table
4's times table
5's times table
6's times table
7's times table
8's times table
9's times table
10's times table
11's times table
12's times table \n"""))
#Creates grade book
correct_count = 0
#creates our looping range
for i in range(1, 13):
#pulls the table from storage
    answer = int(input(f"{table}x{i} = "))
# calculate the correct answer
    correct_answer = table * i  
#printing outputs of answers
    if answer == correct_answer:
        print("Good Job!")
# increment the correct answer counter    
        correct_count += 1  
    else:
        print(f"Oops! The correct answer was {correct_answer}.")

# Calculate the score as a percentage
score = (correct_count / 12) * 100

# Assign a letter grade based on the score
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
#final score print
print(name, f"You got {correct_count} out of 12 correct. That's a {score:.2f}%! Your grade is: {grade}.")
