import tkinter
import math

# Simple tkinter GUI which converts alternating current (AC)
# peak voltage to root mean square voltage (Vrms)
# Vrms = Vpeak / sqrt(2)


# Initialize window
window = tkinter.Tk()
window.title("My First Tkinter UI")
window.minsize(width=259, height=120)
window.config(padx=25, pady=20)


# Button
# function to be called on button click
def calc_button_clicked():
    vpeak = float(my_entry.get())
    vrms = round((vpeak / math.sqrt(2)))
    result_label.config(text=f"{vrms}")


# Label 1 (From units)
my_label_1 = tkinter.Label(text="Peak Voltage")
my_label_1.grid(row=0, column=2)

# Label 2 (Literal: "is equal to")
my_label_2 = tkinter.Label(text="is equal to")
my_label_2.grid(row=1, column=0)

# Label 3 (To units)
my_label_3 = tkinter.Label(text="RMS voltage")
my_label_3.grid(row=1, column=2)

# Label 4 (result)
result_label = tkinter.Label(text=0)
result_label.grid(row=1, column=1)
result_label.config(padx=10, pady=25)


# Entry (input for vpeak)
my_entry = tkinter.Entry()
my_entry.insert(tkinter.END, string="voltage")
my_entry.config(width=8)
my_entry.grid(row=0, column=1)

# Calls button_clicked() on click
calc_button = tkinter.Button(text="Calculate", command=calc_button_clicked)
calc_button.grid(row=2, column=1)


window.mainloop()
