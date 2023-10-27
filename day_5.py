print("We are the Knights who say... Ni!")
print("Whom are you?")

witch = input("Do you look like a witch?: ")
if witch == "yes":
    print("You're a witch!")
else:
    bow = input("Can you shoot a bow?: ")
    if bow == "yes":
        print("You're an ARCHER!")
    else:
        sail = input("Can you sail?: ")
        if sail == "yes":
            print("You're a PIRATE!")
        else:
            print("I give up, you're special 😋")
