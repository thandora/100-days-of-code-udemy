import tkinter

# Initialize window
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
# function to be called on button click
def button_clicked():
    entry_text = my_entry.get()
    my_label.config(text=f"{entry_text} (label)")


# Calls button_clicked() on click
my_button = tkinter.Button(text="I'm button", command=button_clicked)
my_button.pack()

# Entry
my_entry = tkinter.Entry()
# END is just a constant that points the cursor the the end of the writing space
my_entry.insert(tkinter.END, string="Starting message")
my_entry.pack()

# Text
my_text = tkinter.Text(height=3, width=20)
my_text.insert(tkinter.END, "Multi-line text entry")
# Slice characters at line 1 index 0, to end of file.
print(my_text.get(index1="1.0", index2=tkinter.END))
my_text.pack()


# Print to console current value on
def spinbox_used():
    print(my_spinbox.get())


# Spinbox
my_spinbox = tkinter.Spinbox(from_=0, to=5, width=3, command=spinbox_used)
my_spinbox.pack()

# Scale
def scale_used(scale_value):
    print(scale_value)


# Note that command here passes the current value of the scale to the function.
my_scale = tkinter.Scale(from_=0, to=50, command=scale_used)
my_scale.pack()


# Checkbutton
def checkbutton_used():
    print(checked_state.get())


# Variable class for holding checked state.
checked_state = tkinter.IntVar()
my_check_button = tkinter.Checkbutton(
    text="On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
my_check_button.pack()

# Radiobutton
def radio_used():
    if radio_state.get() == 1:
        print("So you choose Option 1, huh.")
    else:
        print("Not a bad choice, going for Option 2.")


# tkinter's intvar used here to hold active radio state
radio_state = tkinter.IntVar()

# When this radiobutton is selected, the intvar would be 1 (value kwarg)
my_radio_1 = tkinter.Radiobutton(
    text="Option 1", value=1, variable=radio_state, command=radio_used
)
# When this radiobutton is selected, the intvar would be 2 (value kwarg)
my_radio_2 = tkinter.Radiobutton(
    text="Option 2", value=2, variable=radio_state, command=radio_used
)
my_radio_1.pack()
my_radio_2.pack()


# Listbox
def listbox_used(event):
    # Get current selection from listbox
    print(my_list_box.get(my_list_box.curselection()))


my_list_box = tkinter.Listbox(height=3)

# Populate listbox
my_choices = ["Foo", "Bar", "Ipsum"]
for i, choice in enumerate(my_choices):
    my_list_box.insert(i, choice)

my_list_box.bind("<<ListboxSelect>>", listbox_used)
my_list_box.pack()

# Keeps the window open and listens on it, must be at the end of the program.
window.mainloop()
