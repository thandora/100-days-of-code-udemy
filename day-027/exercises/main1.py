import tkinter
import main

"""
Exercise on using layout managers, pack(), place(), grid()
"""


def button_clicked():
    entry_text = my_entry.get()
    my_label.config(text=f"{entry_text} (label)")


# Initialize window
window = tkinter.Tk()
window.title("My First Tkinter UI")
window.minsize(width=500, height=400)
window.config(padx=125, pady=100)

# Label
my_label = tkinter.Label(text="First Label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=0)
my_label.config(padx=20, pady=20)

# Button
my_button = tkinter.Button(text="I'm button", command=button_clicked)
my_button.grid(row=1, column=1)

# Entry
my_entry = tkinter.Entry()
my_entry.insert(tkinter.END, string="Starting message")
my_entry.grid(row=2, column=3)

# New button
my_new_button = tkinter.Button(text="I'm another button", command=button_clicked)
my_new_button.grid(row=0, column=2)

window.mainloop()
