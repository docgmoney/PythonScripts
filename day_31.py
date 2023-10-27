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

import sys

# Define colors used
def print_with_color(text, color_code):
    return f"{color_code}{text}\033[0m"

colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Purple
    "\033[96m",  # Cyan
    "\033[97m",  # White
]

title = f"{print_with_color('=', colors[0])}{print_with_color('=', colors[6])}{print_with_color('=', colors[3])} {print_with_color('Music App', colors[2])} {print_with_color('=', colors[3])}{print_with_color('=', colors[6])}{print_with_color('=', colors[0])}"
print(f"        {title:^35}")
print(f"🔥▶️\t{print_with_color('Radio Gaga', colors[6])}")
print(f"\t{print_with_color('Queen', colors[2])}")
prev = "prev"
next = "next"
pause = "pause"
print(f"{print_with_color(prev, colors[6]):<35}")
print(f"{print_with_color(next, colors[1]):^35}")
print(f"{print_with_color(pause, colors[4]):>35}")
