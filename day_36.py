# Create an empty list to store names
name_list = []

# Define a function to tidy up and capitalize names
def clean_and_capitalize(name):
    # Remove extra spaces, capitalize the name, and return it
    return " ".join(name.split()).capitalize()

# Function to remove a name from the list
def remove_name(name):
    if name in name_list:
        name_list.remove(name)
        print(f"Removed {name} from the list.")
    else:
        print(f"{name} not found in the list.")

# Loop to enter and manage names
while True:
    action = input("Enter add, remove, or 'quit': \n").strip()
    
    if action == 'quit':
        break
    
    if action == 'add':
        # Ask for first name and last name separately
        first_name = input("Enter the first name: ").strip()
        last_name = input("Enter the last name: ").strip()
        
        # Clean and capitalize names
        first_name = clean_and_capitalize(first_name)
        last_name = clean_and_capitalize(last_name)
        
        # Create a new string using f-string
        full_name = f"{first_name} {last_name}"
        
        # Check for duplicates without considering extra spaces
        if all(full_name != name for name in name_list):
            name_list.append(full_name)       
        # Print the updated list
        print("Updated name list:")
        for name in name_list:
            print(name)
    
    elif action == 'remove':
        name_to_remove = input("Enter the name you want to remove: ").strip()
        name_to_remove = clean_and_capitalize(name_to_remove)
        remove_name(name_to_remove)
