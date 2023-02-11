import tkinter

window = tkinter.Tk()
window.title("My First Tkinter UI")
window.minsize(width=500, height=500)

# Label
my_label = tkinter.Label(text="First Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")

# #Changing labels
# my_label["text"] = "Second Label"
# my_label.config(text="Another label")

# Button
button = tkinter.Button(text="Me button")


window.mainloop()
