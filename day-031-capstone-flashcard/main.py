import tkinter as tk
from tkinter import messagebox
import pandas as pd

"""
A language learning flashcard from translating between French to English.
"""
FROM_LANG = "French"
TO_LANG = "English"
BACKGROUND_COLOR = "#B1DDC6"
timer = None

# Load csv to dict.
words_df = {}
while len(words_df) < 1:
    try:
        words_df = pd.read_csv("data/words_to_learn.csv")
        assert len(words_df) > 0

    except FileNotFoundError:
        words_df = pd.read_csv("data/french_words.csv")

    except AssertionError:
        is_confirmed = messagebox.askokcancel(
            "Confirm Reset", "Word database is empty. Would you like to reset it?"
        )
        if is_confirmed:
            words_df = pd.read_csv("data/french_words.csv")
            words_df.to_csv("data/words_to_learn.csv")
            break


def next_card() -> None:
    """Displays next unanswered word available from word data source."""
    global current_word_df
    try:
        words_to_learn = words_df[words_df["Answered"] == False]
        words_to_learn.to_csv("data/words_to_learn.csv")
        word = get_unanswered_word(words_df)
    except ValueError:
        messagebox.showinfo(
            title="Game Over",
            message="Congratulations\nYou've correctly answered every word.",
        )
    else:
        current_word_df = word[0]
        from_word = word[1]
        to_word = word[2]

        flashcard.itemconfig(flashcard_img, image=front_img)
        flashcard.itemconfig(lang_text, text=FROM_LANG)
        flashcard.itemconfig(word_text, text=from_word)
        flip_card(to_word)


def show_back(word: str) -> None:
    """Display the answer and change canvas image.

    Args:
        word (str): word to be displayed
    """
    flashcard.itemconfig(flashcard_img, image=back_img)
    flashcard.itemconfig(lang_text, text=TO_LANG)
    flashcard.itemconfig(word_text, text=word)


def flip_card(word: str) -> None:
    """Flips the card after 3000 ms.

    Args:
        word (str): word to be displayed on card flip.
    """

    global timer
    timer = window.after(3000, show_back, word)


def get_unanswered_word(words_df: any) -> list:
    """Generate a random word from words dataframe.

    Args:
        words_df (any): dataframe of words

    Returns:
        list: a list of [<word dataframe>, <word>, <translated word>]
    """
    words_df = words_df[words_df["Answered"] == False]
    word_df = words_df.sample()
    un_word = word_df.iloc[0][FROM_LANG]
    un_words_transl = word_df.iloc[0][TO_LANG]
    return [word_df, un_word, un_words_transl]


def right_ans() -> None:
    """Marks the current word as answered."""

    i = current_word_df.index[0]
    words_df["Answered"][i] = True
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
# Window
window = tk.Tk()
window.title("Flashky")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
front_img = tk.PhotoImage(file="images/card_front.png")
back_img = tk.PhotoImage(file="images/card_back.png")
flashcard = tk.Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
flashcard_img = flashcard.create_image(400, 263, image=front_img)
# Canvas text
lang_text = flashcard.create_text(400, 145, text="French", font=("Arial", 30, "italic"))
word_text = flashcard.create_text(
    400, 265, text="c'est la vie", font=("Arial", 45, "bold")
)

flashcard.grid(row=0, column=0, columnspan=2)

# Buttons
WRONG_IMG = tk.PhotoImage(file="./images/wrong.png")
wrong_button = tk.Button(width=100, height=99, command=next_card)
wrong_button.config(image=WRONG_IMG, borderwidth=0, highlightthickness=0)
wrong_button.grid(row=1, column=0)

RIGHT_IMG = tk.PhotoImage(file="./images/right.png")
right_button = tk.Button(width=100, height=99, command=right_ans)
right_button.config(image=RIGHT_IMG, borderwidth=0, highlightthickness=0)
right_button.grid(row=1, column=1)


words_df["Answered"] = False
un_word = get_unanswered_word(words_df)
next_card()


window.mainloop()
