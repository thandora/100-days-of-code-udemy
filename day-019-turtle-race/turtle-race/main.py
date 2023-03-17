from turtle import Turtle, Screen
from math import floor
import random

# Setup
screen = Screen()
screen_size = (1200, 1000)
screen.setup(width=screen_size[0], height=screen_size[1])

# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
colors = ["red", "orange", "blue"]
# Create a list of turtles for each of the color in colors.
turtles = []
for i, color in enumerate(colors):
    turtles.append(Turtle())
    turtles[i].shape("turtle")
    turtles[i].turtlesize(stretch_wid=2.2, stretch_len=2.2)
    turtles[i].fillcolor(color)
    turtles[i].penup()
    turtles[i].speed(8)


class Race:
    """Responsible for all racing operations"""

    def __init__(self, racers, screen_size):
        """Init.

        Args:
            racers (list of turtle objects): Contains turtle objects
            screen_size (tuple): Tuple of screen size to be initialised, in pixels.
        """
        self.racers = racers
        self.screen_size = screen_size
        self.n_racers = len(racers)

    def move_to_start(self, spacing):
        """Moves all racers to the starting line

        Args:
            spacing (number): positive number, vertical pixel spacing between each racer
        """
        n = self.n_racers

        if self.is_even(n):
            first_position_y = (spacing / 2) * (n - 1)
        else:
            first_position_y = int(floor(n / 2)) * spacing

        for racer in self.racers:
            starting_line = -((self.screen_size[0] / 2) - (spacing * 1.5))
            racer.goto(starting_line, first_position_y)
            first_position_y -= spacing

    def is_even(self, number):
        if (number % 2) == 0:
            return True
        else:
            return False

    def start_race(self, finish_line):
        """Starts the race. Returns the color of the winner racer

        Args:
            finish_line (number): x-coordinate of finish line

        Returns:
            str: color of winner
        """
        racers = self.racers
        race_on = True

        self.draw_finish(finish_line)
        while race_on:
            for racer in racers:
                # Move current racer a random distance (yes, it can move backward)
                distance = random.randint(-2, 16)
                racer.forward(distance)
                if racer.xcor() >= finish_line:
                    winner = racer.fillcolor()
                    race_on = False
                    print(f"{winner.capitalize()} has won!")
                    return winner

    def draw_finish(self, finish_line):
        """Draws a vertical line at x-coordinate finish_line

        Args:
            finish_line (number): x-coordinate of finish line
        """
        x = Turtle()
        x.penup()
        x.hideturtle()
        x.speed(8)
        x.width(5)
        x.goto(finish_line, self.screen_size[1] / 2)
        x.pendown()
        x.goto(finish_line, -(self.screen_size[1] / 2))


race_brain = Race(turtles, (1000, 1000))
race_brain.move_to_start(60)

# For dynamically prompting user for choices among racers
racers_text = []
for racer in turtles:
    racers_text.append(racer.fillcolor()[0].capitalize())
racers_text = "".join(racers_text)
user_choice = screen.textinput(title="CHOOSE YOUR TURTLE", prompt=f"Who wins? ({racers_text})")


winner = race_brain.start_race(400)
if user_choice[0].lower() == winner[0].lower():
    print("u won boy")
else:
    print("u lost boy")


screen.exitonclick()
