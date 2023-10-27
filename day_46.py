# MonDex
print("Welcome to MonDex, your friendly Mon library indexer...")

# Creating library
mondex = []

# Library Definitions for the elements and special moves
element_colors = {
    "fire": "\033[91m",   # Red
    "water": "\033[94m",  # Blue
    "earth": "\033[92m",  # Green
    "air": "\033[97m",    # White
    "electric": "\033[93m",  # Yellow
    "spirit": "\033[95m"  # Purple
}

while True:
    # Ask the user for their choice (add, view, or quit)
    choice = input("\nChoose an option:\n1. Add Mon\n2. View Index\n3. Quit\nEnter the number of your choice: \n")

    if choice == "1":
        # Ask the user to input details for one Mon
        input_details = input("Enter Mon details (name, type, special_move, starting_HP, starting_MP): \n")
        details = input_details.split()

        # Check if the input contains all required details
        if len(details) == 5:
            name, beast_type, special_move, starting_hp, starting_mp = details

            # Create a dictionary for the Mon
            mokemon_info = {
                "Name": name,
                "Type": beast_type,
                "Special Move": special_move,
                "Starting HP": starting_hp,
                "Starting MP": starting_mp
            }

            # Append the Mon to the MonDex
            mondex.append(mokemon_info)

            # Print the Mon's details with the appropriate text color
            if beast_type.lower() in element_colors:
                print(f"\n{element_colors[beast_type.lower()]}Mon Added to MonDex:")
                for key, value in mokemon_info.items():
                    print(f"{key}: {value}")
                print("\033[0m")  # Reset color to default
            else:
                print("Invalid beast type. Cannot display Mon information.")
        else:
            print("Please provide all required details for the Mon.")

    elif choice == "2":
        # Print the entire index of known Mons with color formatting
        print("\n🌟 MonDex Index 🌟")
        for idx, mokemon_info in enumerate(mondex, 1):
            print(f"\n{element_colors[mokemon_info['Type'].lower()]}Mon #{idx}:")
            for key, value in mokemon_info.items():
                print(f"{key}: {value}")
            print("\033[0m")  # Reset color to default

    elif choice == "3":
        # Quit the program
        print("Goodbye! Thank you for using MonDex.")
        break

    else:
        print("Invalid choice. Please select a valid option (1, 2, or 3).")
