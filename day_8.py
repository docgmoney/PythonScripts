print("Today's Affirmation Machine")
name = input("What is your name? ")
print(name, ", thank you for using the Affirmation Machine.")
goal = input("How is today going on a scale of 1 - 10? 1:😥, 10: 🤑\n")

affirmations = {
    "1": "Today is a new chance to be my best self.",
    "2": "Small steps lead to big changes.",
    "3": "I attract positivity and repel negativity.",
    "4": "I believe in myself and trust my journey.",
    "5": "My potential to succeed is infinite.",
    "6": "Challenges are opportunities in disguise, and I welcome them.",
    "7": "I am deserving of love, success, and happiness.",
    "8": "Every day, I grow stronger and more powerful in my convictions.",
    "9": "The universe aligns in perfect harmony with my dreams and desires.",
    "10": "I am a limitless force, capable of achieving anything I set my mind to."
}

if goal in affirmations:
    print(affirmations[goal])
    satisfaction = input("How would you rate this Affirmation today? ")
    
    if satisfaction == "good":
        print(name,"Thank you for your feedback in making Affirmation Machine better")
    else:
        print(name, "Shoot, looks like your feedback got lost on the web. Sorry, try again tomorrow!")
else:
    print("Invalid input. Please rate on a scale of 1 to 10.")
