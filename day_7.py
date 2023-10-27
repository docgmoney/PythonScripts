print("Fake Pokemon Fan Finder 2000")
fan = input("Are you a Pokemon fan?: ")

if fan == "yes":
    print("Fantastic lets test your understanding of the subject")
    favchar = input("Who is your favorite main character?")
    
    if favchar == "Ash":
        print("The main character huh... pretty lame")
        firstP = input("Who was his first pokemon?: ")
        
        if firstP == "Pikachu":
            print("You're a real fan")
        else:
            print("SEE YOU'RE A LAME FAKER!!!")
    
    elif favchar == "Misty":
        print("Red heads huh?...")
        firstP = input("What was the first thing she caught in the Original TV series?: ")
        
        if firstP == "Ash":
            print("You're a true fan at heart!!!")
        else:
            print("You're bad at this...and not a true Pokemon fan!")
    
    else:
        print("Brock the ladies man...")
        firstP = input("What gym do we find Brock at in the Original TV series?: ")
        
        if firstP == "Pewter City":
            print("Your memory is strong as a rock!")
        else:
            print("Gotta be a true fan to know where the Brock rocks!")
else:
    print("Lame, You should go watch it some more!")
