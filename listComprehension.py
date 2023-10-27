#List of temps
temps = [221, 234, 340, 230, -9999]

#creates empty list
new_temps = []

# Function for the list
for temp in temps:
    if temp == -9999:
        print("0")
    else:
        new_temps.append(temp / 10)

#give output....
print(new_temps)


#OR

new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)