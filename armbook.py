def colorChange(color, text):
    color_codes = {
        'white': '\033[97m',
        'blue': '\033[94m',
        'yellow': '\033[93m',
        'red': '\033[91m'
    }
    return f"{color_codes[color]}{text}\033[0m"

print()
print()
text = "WELCOME TO"
print(f"{colorChange('white', text):^35}")
text = "--  ARMBOOK  --"
print(f"{colorChange('blue', text):^35}")
text = "Definitely not a rip off"
print(f"{colorChange('yellow', text):>35}")
text = "a certain other social"
print(f"{colorChange('yellow', text):>35}")
text = "networking site"
print(f"{colorChange('yellow', text):>35}")
text = "Honest."
print(f"{colorChange('red', text):^35}")
print("Username")
print("Password")
