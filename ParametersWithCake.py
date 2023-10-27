def whichCake():
    flavor = input("What kind of cake are you wanting to bake?: \n")
    cake = input("What kind of cake base would you like to have?: \n")
    frosting = input("What kind of frosting will it have?: \n")

    if flavor == "chocolate":
        print("mmm, chocolate cake is amazing")
    elif flavor == "broccoli":
        print("You want a what type of cake.... ew")
    else:
        print("Yeah, that's great I suppose...")
    
    print("So you want a", flavor, "cake on a", cake, "base with", frosting, " frosting on top?: \n")

# Call the function
whichCake()
