import time
import sys

def print_with_color(text, color_code):
    sys.stdout.write(f"\r{color_code}{text}\033[0m")
    sys.stdout.flush()

colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Purple
    "\033[96m",  # Cyan
    "\033[97m",  # White
]

def hide_cursor():
    print("\033[?25l", end="")

def show_cursor():
    print("\033[?25h", end="")

def main():
    hide_cursor()
    while True:
        user_text = input("Enter the text (or 'quit' to exit): \n")
        if user_text.lower() == 'quit':
            break

        for color in colors:
            print_with_color(user_text, color)
            time.sleep(0.5)  # Wait for 0.5 seconds

    show_cursor()

if __name__ == "__main__":
    main()
