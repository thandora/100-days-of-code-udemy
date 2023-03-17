import tkinter as tk
from tkinter import messagebox
import pyperclip
from chars import LETTERS, NUMBERS, SYMBOLS
import random
import json

"""
A password generator that can save details into a csv file.
"""
N_LETTERS_MAX = 8
N_SYMBOLS_MAX = 5
N_NUMBERS_MAX = 5
MIN_PASS_LENGTH = 12
n_max_sum = N_LETTERS_MAX + N_SYMBOLS_MAX + N_NUMBERS_MAX
if n_max_sum < MIN_PASS_LENGTH:
    raise ValueError("n_max_sum should be greater than mininum pass length")


# ---------------------------- PASSWORD GENERATOR AND SEARCH ------------------------------- #
# Taken from day 5 and modified.
def generate_password() -> None:
    """Generate password with number of characters defined by N_LETTERS_MAX,
    N_SYMBOLS_MAX, N_NUMBERS_MAX. Places password to password entry.
    Automatically copies the password to clipboard"""

    global N_LETTERS_MAX, N_SYMBOLS_MAX, N_NUMBERS_MAX, MIN_PASS_LENGTH
    password_length = 0

    while password_length < MIN_PASS_LENGTH:
        n_letters = random.randint(N_LETTERS_MAX - 3, N_LETTERS_MAX)
        n_symbols = random.randint(N_SYMBOLS_MAX - 3, N_SYMBOLS_MAX)
        n_numbers = random.randint(N_NUMBERS_MAX - 3, N_NUMBERS_MAX)
        password_length = n_letters + n_symbols + n_numbers

    password = []
    position = []

    for x in range(0, password_length):
        password.append("")
        position.append(x)
    # Create password
    for x in range(0, password_length):

        cr_position = random.choice(position)
        position.remove(cr_position)

        # Place random character in current position (cr_position).
        if n_letters:  # Exhaust letters first.
            password[cr_position] = random.choice(LETTERS)
            n_letters -= 1
        elif n_symbols:  # Exhaust symbols.
            password[cr_position] = random.choice(SYMBOLS)
            n_symbols -= 1
        elif n_numbers:  # Exhaust numbers.
            password[cr_position] = random.choice(NUMBERS)
            n_numbers -= 1

    password = "".join(password)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def search() -> None:
    """Search passwords.json for website credentials and display in message box if found."""
    website = web_entry.get()
    try:
        with open("passwords.json", "r") as f:
            data = json.load(f)

    except FileNotFoundError:
        messagebox.showinfo(
            title="File Not Found",
            message="json not found because web database is empty. Add an entry to start.",
        )

    else:
        # Ignore casing in search
        data_sites = [site.lower() for site in data.keys()]
        if website.lower() in data_sites:

            # Convert search string to original casing to avoid KeyError
            for site in data.keys():
                if website.lower() == site.lower():
                    website = site

            details = data[website]
            user = details["username/email"]
            password = details["password"]
            messagebox.showinfo(
                title=f"{website} Details",
                message=f"Username/Email: {user}\nPassword:{password}",
            )
        else:
            messagebox.showinfo(title="Site Not Found", message=f"{website} not found")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password() -> None:
    """Saves password into csv file."""
    website = web_entry.get()
    username = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username/email": username,
            "password": password,
        }
    }

    # Check for empty entry fields.
    if any_empty():
        messagebox.showinfo(
            title="Blank Field", message="Please make sure to fill out all fields."
        )

    else:

        try:
            with open("passwords.json", "r") as f:
                data = json.load(f)
                data.update(new_data)

            with open("passwords.json", "w") as f:
                json.dump(data, f, indent=4)

        except FileNotFoundError:
            with open("passwords.json", "w") as f:
                json.dump(new_data, f, indent=4)

        web_entry.delete(0, tk.END)
        user_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


def any_empty() -> bool:
    """Check if any entry field is empty

    Returns:
        bool: returns True if any entry is empty. False otherwise
    """
    entries = [web_entry, user_entry, password_entry]
    for entry in entries:
        if len(entry.get()) == 0:
            return True
    return False


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas
logo = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
web_label = tk.Label(text="Website:")
user_label = tk.Label(text="Email/Username:")
password_label = tk.Label(text="Password:")
# sticky="e" is basically "east" justified.
web_label.grid(row=1, column=0, sticky="e")
user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0, sticky="e")


# Entries
web_entry = tk.Entry()
web_entry.config(width=32)
web_entry.grid(row=1, column=1, columnspan=2, sticky="w")

user_entry = tk.Entry()
user_entry.config(width=32)
user_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = tk.Entry()
password_entry.config(width=32)
password_entry.grid(row=3, column=1, columnspan=2, sticky="w")


# Buttons
gen_button = tk.Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=2, columnspan=2, sticky="w")

add_button = tk.Button(text="Add", width=43, command=save_password)
add_button.grid(row=4, column=1, columnspan=3, sticky="w")

search_button = tk.Button(text="Search", width=14, command=search)
search_button.grid(row=1, column=2, sticky="w")

window.mainloop()
