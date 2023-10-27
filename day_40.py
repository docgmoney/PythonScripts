# Initialize an empty dictionary for the new contact
new_contact = {}

# Input data from the user
new_contact["name"] = input("Input your name > ").lower()
new_contact["dob"] = input("Input your date of birth (mm/dd/yyyy) > ")
new_contact["telephone"] = input("Input your telephone number > ").replace(" ", "")
new_contact["email"] = input("Input your email > ").lower()
new_contact["address"] = input("Input your address > ")

# Display the contact card
print("🌟 Contact Card 🌟")
print(f"Hi {new_contact['name'].title()}. Our white pages says that you were born on {new_contact['dob']},")
print(f"we can call you on {new_contact['telephone']}, email {new_contact['email']}, or write to {new_contact['address']}.")
