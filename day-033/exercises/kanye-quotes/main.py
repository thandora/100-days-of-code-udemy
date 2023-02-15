import tkinter as tk
import requests

"""
Display random Kanye quotes through tkinter
"""
# Kanye quotes API endpoint
URL = "https://api.kanye.rest/"


def get_quote():
    response = requests.get(url=URL)
    response.raise_for_status()
    quote = response.json()["quote"]
    # quote = "A" * 50
    if len(quote) > 100:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 18, "bold"))
    elif len(quote) > 50:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 24, "bold"))
    else:
        canvas.itemconfig(quote_text, text=quote, font=("Arial", 30, "bold"))
    # Write your code here.


# UI
window = tk.Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=300, height=416)
background_img = tk.PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    205,
    text="Kanye Quote Goes HERE",
    width=250,
    font=("Arial", 30, "bold"),
    fill="black",
)
canvas.grid(row=0, column=0)

kanye_img = tk.PhotoImage(file="kanye.png")
kanye_button = tk.Button(
    image=kanye_img, borderwidth=0, highlightthickness=0, command=get_quote
)
kanye_button.grid(row=1, column=0)


window.mainloop()
