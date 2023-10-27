userSays = {}
counter = 1

while True:
    if counter > 10:
        print("You ran out of memory space. \n")
        print(userSays.items())
        break
    
    say = input("Say something: \n")

    if say == '/end':
        print(userSays)
        break

    userSays[counter]= say
    counter +=1