import os
import time
import random

listOfEmails = [
    "john.doe@example.com",
    "jane.smith@example.com",
    "user1234@gmail.com",
    "testuser@hotmail.com",
    "alice.doe@yahoo.com",
    "support@website.com",
    "no-reply@company.net",
    "info@domain.org",
    "contact@service.io",
    "admin@adminmail.com",
]

def prettyPrint():
    os.system("clear")
    print("List of Emails \n")
    print()
    num_emails_to_display = 10
    random_emails = random.sample(listOfEmails, num_emails_to_display)
    for index, email in enumerate(random_emails):
        print(f"{index + 1}: {email}")
    
    user_choice = input("Do you want to:\n1. Send Emails\n2. Return to the main menu\n")
    if user_choice == '1':
        sendEmails()

def sendEmails():
    os.system("clear")
    print("Sending Emails...\n")
    template = """Dear {name},
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't, we will pass on your email address to every spammer we've ever encountered and also sign you up for the My Little Pony newsletter, because that's neat. We might just do that anyway.
Love and hugs,
Ian Spammington III"""

    for email in listOfEmails:
        name = email.split('@')[0]  # Extract the name from the email address
        email_text = template.replace("{name}", name)
        print(email_text)
        time.sleep(2)
        os.system("clear")

while True:
    print("Spammer Inc.")
    menu = int(input("""Do you want to 
    1. Input Emails
    2. Remove Emails
    3. Print list of Emails
    4. Quit
    """))

    if menu == 1:
        email = input("What is the email you wish to enter?: \n")
        listOfEmails.append(email)
    elif menu == 2:
        email = input("Which email would you like to remove?: \n")
        if email in listOfEmails:
            listOfEmails.remove(email)
    elif menu == 3:
        prettyPrint()
    elif menu == 4:
        break
    else:
        print("Invalid option. Please choose a valid menu option.")

os.system("clear")
