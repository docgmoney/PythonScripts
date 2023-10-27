print("Replit's Secure Login")
print("Username:admin")
print("Pin:1234")
# This is our list of approved username password combinations
correct_username = "admin"
correct_password = "1234"

def login():
    attempts = 0 

    while attempts < 3:
        username = input("What is your name?: \n")
        password = input("What is your 4 digit pin?: \n")

        if username == correct_username and password == correct_password:
            print("Login successful!")
        else:
            print("Incorrect username or password. Please try again.")
            attempts += 1

    # If user fails to login after 3 attempts:
    print("Too many incorrect attempts. Exiting for user safety.")
    exit()

login()
