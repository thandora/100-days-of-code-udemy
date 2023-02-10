import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game (Enter exit to exit)")
screen.setup(width=800, height=600)

# Save blank states as turtle shape and display
screen.addshape("blank_states.gif")
turtle.shape("blank_states.gif")
turtle_writer = turtle.Turtle()
turtle_writer.penup()
turtle_writer.shape("circle")
turtle_writer.speed(7)
turtle_writer.goto(225, 200)
turtle_writer.turtlesize(0.8, 0.8)


def ask_user(score: int) -> str:
    """Ask user through turtle prompt

    Args:
        score (int): int

    Returns:
        str: returns guess as str
    """
    return screen.textinput(
        title=f"{score}/50 Correct States", prompt="Name a state:"
    ).title()


guessed_states = []
score = len(guessed_states)

df = pd.read_csv("50_states.csv")
states = df["state"].values

while score < 50:
    user_guess = ask_user(score=score)
    # Check if user guess is correct and havent been guessed before.
    if user_guess in states and user_guess not in guessed_states:
        guessed_states.append(user_guess)
        score = len(guessed_states)

        state_Data = df[df["state"] == user_guess]
        state_coor = (float(state_Data["x"]), float(state_Data["y"]))
        state = state_Data["state"].values[0]
        turtle_writer.goto(state_coor)
        turtle_writer.write(state)

    # Exit
    if user_guess == "Exit":
        # Creates a list of the difference between all the states and guessed states
        s = [x for x in states if x not in guessed_states]

        # Create csv for reviewing states
        unguessed_states = {"unguessed states": s}
        reviewer_df = pd.DataFrame(unguessed_states)
        reviewer_df.to_csv("reviewer.csv")
        break

    # This just makes the prompt active after the guess. QOL
    turtle_writer.goto(225, 200)
