myBill = float(input("What was the bill?: "))
tip = float(input("What % of a tip would you like to leave?: \n"))
numberOfPeople = int(input("How many people?: \n"))

# Calculate the actual tip amount
actual_tip = myBill * tip / 100

# Calculate the total amount per person
answer = (myBill + actual_tip) / numberOfPeople

print("You all owe", round(answer, 2))
