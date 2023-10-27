print("Animal Sound Generator")

# Variables
elephant_sound = "awooo"
horse_sound = "Neigh"
dog_sound = "Woof"
cat_sound = "Meow"
uexit = "no"

while uexit != "yes":
    animal = int(input("""What animal would you like to hear? \n
    1.Elephant
    2.Horse
    3.Dog
    4.Cat \n"""))

    # Converting animals to sounds
    sound = ""
    if animal == 1:
        sound = elephant_sound
    elif animal == 2:
        sound = horse_sound
    elif animal == 3:
        sound = dog_sound
    elif animal == 4:
        sound = cat_sound
    else:
        print("Try a valid selection")
        sound = ""

    if sound:
        print(sound)

    # Exit ask
    uexit = input("Would you like to exit at this time?: yes/no \n")
    if uexit == "yes":
      exit