import tkinter as tk
from tkinter import messagebox
import pyperclip
from chars import LETTERS, NUMBERS, SYMBOLS
import csv
import random

"""
A password generator that can save details into a csv file.
"""
N_LETTERS = 5
N_SYMBOLS = 5
N_NUMBERS = 5


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Taken from day 5
def generate_password():
    """Generate password with number of characters defined by N_LETTERS, N_SYMBOLS, N_NUMBERS.
    Places password to password entry. Automatically copies the password to clipboard"""
    global N_LETTERS, N_SYMBOLS, N_NUMBERS
    n_letters = N_LETTERS
    n_symbols = N_SYMBOLS
    n_numbers = N_NUMBERS
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


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password() -> None:
    """Saves password into csv file."""
    website = web_entry.get()
    username = user_entry.get()
    password = password_entry.get()

    # Check for empty entry fields.
    if any_empty():
        messagebox.showinfo(
            title="Blank Field", message="Please make sure to fill out all fields."
        )
    else:
        m = f"These are the details entered: \nEmail: {username}\nPassword: {password} \nIs it ok to save?"
        is_confirmed = messagebox.askokcancel(title=website, message=m)

        if is_confirmed:

            with open("passwords.csv", "a", newline="") as f:
                data = [website, username, password]
                writer = csv.writer(f)
                writer.writerow(data)

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
web_entry.config(width=55)
web_entry.grid(row=1, column=1, columnspan=2, sticky="w")

user_entry = tk.Entry()
user_entry.config(width=55)
user_entry.grid(row=2, column=1, columnspan=2, sticky="w")

password_entry = tk.Entry()
password_entry.config(width=35)
password_entry.grid(row=3, column=1, columnspan=2, sticky="w")


# Buttons
gen_button = tk.Button(text="Generate Password", command=generate_password)
gen_button.grid(row=3, column=1, columnspan=2, sticky="e")

add_button = tk.Button(text="Add", width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="w")

window.mainloop()
