import tkinter as tk

"""
Pomodoro GUI using Tkinter
"""

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#F48484"
RED = "#F55050"
BLUE = "#86A3B8"
YELLOW = "#E8D2A6"
GREEN = "#1F8A70"
FONT_NAME = "Courier"
WORK_MIN = 30
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets everything to default/"""
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    check_label.config(text="   ")
    timer_label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts timer and handles timer label. Time is according to number of reps done."""
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer = long_break_sec
        text_label = "Long break"
        label_fg = GREEN
    elif reps % 2 == 0:
        timer = short_break_sec
        text_label = "Short Break"
        label_fg = GREEN
    else:
        timer = work_sec
        text_label = "Work"
        label_fg = RED

    timer_label.config(text=text_label, fg=label_fg)
    count_down(timer)


def add_check(reps: int):
    """Adds a check to screen. Creates new line every 4 reps.

    Args:
        reps (int): current number of reps (including breaks)
    """

    pom_rep = reps // 2
    i = pom_rep
    checks = []
    for i in range(1, pom_rep + 1):
        checks.append("✔")
        if i % 4 == 0:
            checks.append("\n")

    checks = "".join(checks)

    check_label.config(text=checks)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(time_rem: int):
    """Starts a countdown of time given. Also handles the display of the timer.
    Displays in mm:ss format.

    Args:
        time_rem (int): seconds remaining.
    """
    # Format remaining time
    global reps, timer

    rem_min = time_rem // 60
    rem_sec = time_rem % 60

    if len(str(rem_min)) == 1:
        rem_min = f"0{rem_min}"
    if len(str(rem_sec)) == 1:
        rem_sec = f"0{rem_sec}"

    time_rem_format = f"{rem_min}:{rem_sec}"
    canvas.itemconfig(timer_text, text=time_rem_format)
    if time_rem > 0:
        timer = window.after(1000, count_down, time_rem - 1)
    else:
        start_timer()
    add_check(reps=reps)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas for tomato background
tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold")
)
canvas.grid(row=1, column=1)


# Labels (timer and check)
# Timer
timer_label = tk.Label(text="Timer ", font=("Arial", 24, "bold"), fg=RED, bg=YELLOW)
timer_label.grid(row=0, column=1)
# Check
check_label = tk.Label(text="   ", font=("Arial", 14, "bold"), bg=YELLOW, fg=BLUE)
check_label.grid(row=3, column=1)


# Buttons (start and end)
# Start button
start_button = tk.Button(text="Start", font=("Arial", 10), command=start_timer)
start_button.config(fg=RED)
start_button.grid(row=2, column=0)
# Reset button
reset_button = tk.Button(text="Restart", font=("Arial", 10), command=reset_timer)
reset_button.config(fg=RED)
reset_button.grid(row=2, column=2)
window.mainloop()
