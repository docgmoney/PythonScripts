import tkinter as tk
from tkinter import ttk
import itertools
import csv
import os

# Constants
CSV_FILE = "saved_codes.csv"
FONT = ("Arial", 16)

# Define a basic L33T dictionary
L33T_DICT = {
    'A': '4', 'E': '3', 'I': '1', 'O': '0', 'S': '5', 'Z': '2'
}

# Custom colors
BG_COLOR = "#000000"  # Dark Background
TEXT_COLOR = "#00FF00"  # Green Text
ENTRY_BG_COLOR = "#3C3C3B"  # Dark Entry Background
LISTBOX_BG_COLOR = "#3C3C3B"  # Dark Listbox Background
LISTBOX_SEL_COLOR = "#00FF00"  # Listbox Selection Color
BUTTON_BG_COLOR = "#FFFFFF"  # White Button Background
BUTTON_TEXT_COLOR = "#00FF00"  # Green Button Text

def to_l33t(text):
    """Converts a given text to L33T speak."""
    return ''.join(L33T_DICT.get(char.upper(), char) for char in text)

def get_color(count):
    """Returns color based on count of code usage."""
    if count >= 50:
        return "#8B008B"  # Purple
    elif count >= 40:
        return "#FF0000"  # Red
    elif count >= 30:
        return "#FF4500"  # OrangeRed
    elif count >= 20:
        return "#FFA500"  # Orange
    elif count >= 10:
        return "#FFFF00"  # Yellow
    elif count >= 5:
        return "#7FFF00"  # Chartreuse (Light Green)
    else:
        return "#008000"  # Green

def generate_all_possible_combinations(known_digits):
    """Generates all possible combinations of codes."""
    all_digits = set("0123456789")
    missing_digits = list(all_digits - set(known_digits))
    if len(known_digits) == 3:
        possible_combinations = set(itertools.permutations(known_digits + known_digits, 4))
    else:
        possible_combinations = set(itertools.permutations(known_digits + ''.join(missing_digits), 4))
    return sorted(possible_combinations)

def save_code_to_csv(code):
    """Saves the correct code to a CSV file."""
    code_dict = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                code_dict[row[0]] = int(row[1])

    count = code_dict.get(code, 0)
    code_dict[code] = count + 1

    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        for key, value in code_dict.items():
            writer.writerow([key, value])

# GUI for Safe Cracker
class SafeCrackerApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window settings
        self.title("PayDay 5af3 Cr4ck3r")
        self.geometry("708x540")
        self.configure(bg=BG_COLOR)

        # Set equal weight for all columns
        self.grid_columnconfigure(0, weight=1)  # First column
        self.grid_columnconfigure(1, weight=1)  # Second column
        self.grid_columnconfigure(2, weight=1)  # Third column

        # Label
        ttk.Label(self, text=to_l33t("Enter the known digits:"), font=FONT, foreground=TEXT_COLOR, background=BG_COLOR).grid(row=0, column=0, pady=20, padx=10, sticky=tk.W)

        # Entry for digits
        self.digit_string = tk.StringVar()
        self.digit_entry = ttk.Entry(self, textvariable=self.digit_string, font=FONT, background=ENTRY_BG_COLOR, foreground=TEXT_COLOR)
        self.digit_entry.grid(row=0, column=1, padx=10)
        self.digit_entry.bind("<Return>", lambda event=None: self.generate_combinations())

        # Generate combinations button
        self.generate_button = ttk.Button(self, text=to_l33t("Generate Combinations"), command=self.generate_combinations, style="Dark.TButton")
        self.generate_button.grid(row=1, column=0, columnspan=2, pady=10)

        # Listboxes for showing combinations
        self.used_frequently = tk.Listbox(self, bg=LISTBOX_BG_COLOR, font=FONT, selectbackground=LISTBOX_SEL_COLOR, foreground=TEXT_COLOR)
        self.used_once = tk.Listbox(self, bg=LISTBOX_BG_COLOR, font=FONT, selectbackground=LISTBOX_SEL_COLOR, foreground=TEXT_COLOR)
        self.garbage_pail = tk.Listbox(self, bg=LISTBOX_BG_COLOR, font=FONT, selectbackground=LISTBOX_SEL_COLOR, foreground=TEXT_COLOR)

        self.used_frequently.grid(row=2, column=0, pady=10, padx=10, sticky=tk.W+tk.E)
        self.used_once.grid(row=2, column=1, pady=10, padx=10, sticky=tk.W+tk.E)
        self.garbage_pail.grid(row=2, column=2, pady=10, padx=10, sticky=tk.W+tk.E)

        # Entry for correct code
        ttk.Label(self, text=to_l33t("Correct Code:"), font=FONT, foreground=TEXT_COLOR, background=BG_COLOR).grid(row=3, column=0, pady=20, padx=10, sticky=tk.W)
        self.correct_code = tk.StringVar()
        self.correct_code_entry = ttk.Entry(self, textvariable=self.correct_code, font=FONT, background=ENTRY_BG_COLOR, foreground=TEXT_COLOR)
        self.correct_code_entry.grid(row=3, column=1, padx=10)
        self.correct_code_entry.bind("<Return>", self.submit_code)

        # Button to submit the correct code
        self.submit_button = ttk.Button(self, text=to_l33t("Submit Code"), command=self.submit_code, style="Submit.TButton")
        self.submit_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Create a custom style for dark buttons
        style = ttk.Style()
        style.configure("Dark.TButton", background=BUTTON_BG_COLOR, foreground=TEXT_COLOR)
        style.configure("Submit.TButton", background=BG_COLOR, foreground=TEXT_COLOR)

        # Label for last saved code
        self.last_saved_label = ttk.Label(self, text="Last Saved Code:", font=("Arial", 20), foreground=TEXT_COLOR, background=BG_COLOR)
        self.last_saved_label.grid(row=5, column=0, pady=10, padx=10, columnspan=3, sticky=tk.W)

        # Variable to store the last saved code
        self.last_saved_code = tk.StringVar()
        self.last_saved_code_label = ttk.Label(self, textvariable=self.last_saved_code, font=("Arial", 24), foreground=TEXT_COLOR, background=BG_COLOR)
        self.last_saved_code_label.grid(row=6, column=0, pady=10, padx=10, columnspan=3, sticky=tk.W)

    def generate_combinations(self, event=None):
        """Generates combinations based on the given digits and populates the listbox."""
        known_digits = self.digit_string.get()
        if not known_digits:
            return

        self.used_frequently.delete(0, tk.END)
        self.used_once.delete(0, tk.END)
        self.garbage_pail.delete(0, tk.END)

        all_combinations = generate_all_possible_combinations(known_digits)

        # Load codes from CSV
        code_dict = {}
        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, mode='r', newline='') as file:
                reader = csv.reader(file)
                for row in reader:
                    code_dict[row[0]] = int(row[1])

        # Populate listboxes based on usage frequency
        for code in all_combinations:
            str_code = ''.join(code)
            count = code_dict.get(str_code, 0)
            display_text = f"{str_code} ({count})"
            if count >= 10:
                self.used_frequently.insert(tk.END, display_text)
                self.used_frequently.itemconfig(tk.END, {"fg": get_color(count)})
            elif count > 0:
                self.used_once.insert(tk.END, display_text)
                self.used_once.itemconfig(tk.END, {"fg": get_color(count)})
            else:
                self.garbage_pail.insert(tk.END, display_text)
                self.garbage_pail.itemconfig(tk.END, {"fg": get_color(count)})

    def submit_code(self, event=None):
        """Handles submission of the correct code."""
        code = self.correct_code.get()
        save_code_to_csv(code)
        self.correct_code.set("")
        self.digit_string.set("")
        self.last_saved_code.set(code)
        self.generate_combinations()

# Start the GUI
if __name__ == "__main__":
    app = SafeCrackerApp()
    app.mainloop()
