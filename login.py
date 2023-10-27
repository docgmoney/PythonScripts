#replit login system
#start counter
count = 0

while count < 3:
    uname = input("What is your username?: \n")
    upass = int(input("What is your 4 digit pin?: \n"))

#List of usernames and passcodes that are allowed
    if uname == "user" and upass == 1234:
        print("Welcome back to the server User!")
        break
    elif uname == "admin" and upass == 0000:
        print("Welcome Admin")
        break
    else:
        print("Wrong")
        count += 1
#exit parameters
if count == 3:
    print("Stop trying to hack in!!!!")
    exit()