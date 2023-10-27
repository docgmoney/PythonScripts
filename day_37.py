# Makes your Star Wars name
print("Star Wars Name Generator!")

# Asks for needed variables
first, last, city = input("Please enter your full name (first name first) and the city you hail from: \n").split()

# Slices for new first
starwars_first = (first[:3] + last[:3]).title()

# Slices for new last
starwars_last = (last[:2] + city[-3:]).title()

# Print your new name
print(f"{first}, {last}, your new name is {starwars_first}, {starwars_last}")
