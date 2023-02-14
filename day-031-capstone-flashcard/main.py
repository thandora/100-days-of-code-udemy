import tkinter as tk
import pandas as pd

LANGUAGE_FROM = "French"
LANGUAGE_TO = "English"
BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- FUNCTIONS------------------------------- #
def next_card(language, word):
    flashcard.itemconfig(lang_text, text=word, font=("Arial", 30, "italic"))


def show_front(word: str) -> None:
    flashcard.itemconfig(lang_text, text=LANGUAGE_FROM)
    flashcard.itemconfig(word_text, text=word)


def show_back(word: str) -> None:
    flashcard.itemconfig(lang_text, text=LANGUAGE_TO)
    flashcard.itemconfig(word_text, text=word)


def flip_card():
    


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
front_img = tk.PhotoImage(file="images/card_front.png")
flashcard = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard.create_image(400, 263, image=front_img)
# Canvas text
# word = next_card()
lang_text = flashcard.create_text(400, 145, text="French", font=("Arial", 30, "italic"))
word_text = flashcard.create_text(
    400, 265, text="c'est la vie", font=("Arial", 45, "bold")
)

flashcard.grid(row=0, column=0, columnspan=2)

# Buttons
WRONG_IMG = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(width=100, height=99)
wrong_button.config(image=WRONG_IMG, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)

RIGHT_IMG = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(width=100, height=99, command=show_front)
right_button.config(image=RIGHT_IMG, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)
window.mainloop()
