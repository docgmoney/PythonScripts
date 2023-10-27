print("Dakota's Grading Calculator!")

#Variables
name = input("What is your name?: \n")
test = input("What is the test called?: \n")
max = int(input("What was the max points possible?: \n"))
score = int(input("What was your point total?: \n"))

#Maths
grade = score / max * 100

# Grading scale
if 90 <= grade <= 100:
    letter_grade = 'A+'
elif 80 <= grade < 90:
    letter_grade = 'A'
elif 70 <= grade < 80:
    letter_grade = 'B'
elif 60 <= grade < 70:
    letter_grade = 'C'
elif 50 <= grade < 60:
    letter_grade = 'D'
else:
    letter_grade = 'U'
#Grading results
print(name, "you got an", letter_grade, "on the", test,)