import tkinter

window = tkinter.Tk()
window.title("My First Tkinter UI")
window.minsize(width=800, height=500)

# Label
my_label = tkinter.Label(text="First Label", font=("Arial", 24, "bold"))
my_label.pack()

# # Changing labels
# my_label["text"] = "Second Label"
# my_label.config(text="Another label")

# Button

def button_clicked():
    entry_text = input.get()
    my_label.config(text=entry_text)

button = tkinter.Button(text="Me button", command=button_clicked)
button.pack()

# Entry
input = tkinter.Entry()
input.pack()



window.mainloop()
