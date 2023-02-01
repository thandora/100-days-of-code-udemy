import random
import colorgram
from turtle import Turtle, Screen

# Initialise
spark = Turtle()
spark.hideturtle()
screen = Screen()
# This allows rgb values. color(r, g, b) doesnt work otherwise.
screen.colormode(255)

palette = colorgram.extract("image.jpg", 150)
colors = []
color_rgb = []
for color in palette:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    # Filter saturated colors
    if r > 210 and g > 210 and b > 210:
        continue
    colors.append((r, g, b))


class SpotPainter:
    def __init__(self, turtle, thickness, palette):
        self.palette = palette
        self.turtle = turtle
        self.turtle.pensize(thickness)
        self.turtle.fillcolor("green")

    def paint(self, n_row, n_column, spacing, color_random=False):

        dot_radius = self.turtle.pensize()
        # -1 is there because somehow the dot size starts at 0, not 1
        spacing_distance = (dot_radius * 2) + spacing - 1
        direction = "right"

        for i in range(n_row):
            self.paint_row(n_column, spacing_distance, direction, color_random)
            # Don't move turtle after drawing last dot
            if i == (n_row) - 1:
                continue

            if direction == "right":
                self.u_turn(spacing_distance, direction)
                direction = "left"

            elif direction == "left":
                self.u_turn(spacing_distance, direction)
                direction = "right"

    def paint_row(self, n_elements, spacing, direction="right", color_random=False):
        """Paint's a row of n_lements dots, spaced.

        Args:
            n_elements (_type_): _description_
            spacing (_type_): _description_
            direction (str, optional): _description_. Defaults to "right".
            color_random (bool, optional): _description_. Defaults to False.
        """
        for i in range(n_elements):
            if color_random:
                self.random_color()
            self.turtle.pu()
            self.turtle.dot()

            # Don't move forward after drawing last dot in row
            if i == (n_elements - 1):
                continue
            self.turtle.forward(spacing)

    def u_turn(self, distance, turn_direction: str = "right"):
        """Does a u-turn on the direction provided, distance moved each step, but does not move
        forward on the final turn.

        Args:
            current_direction (str): U-turns into the direction provided: "left" or "right"
        """
        if turn_direction == "right":
            direction = 90
        elif turn_direction == "left":
            direction = -90

        self.turtle.rt(direction)
        self.turtle.forward(distance)
        self.turtle.rt(direction)

    def random_color(self):
        """Changes self.turtle.pencolor randomly from self.palette"""
        color = random.choice(self.palette)
        self.turtle.pencolor(color)


painter = SpotPainter(spark, 15, colors)
painter.turtle.speed(0)
painter.paint(5, 5, 15, True)
screen.exitonclick()
