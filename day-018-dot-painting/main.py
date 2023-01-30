from turtle import Turtle, Screen
from random import randint, choice

screen = Screen()
screen.colormode(255)
# Spark the turtle
spark = Turtle()
spark.shape("turtle")
spark.fillcolor((155, 100, 255))
spark.pencolor("green")


# Tasks

# Rectangular spiral
def draw_rect_spiral(walker_object, initial_length, end_length, increment=50):
    while initial_length >= end_length:
        for _ in range(2):
            spark.fd(initial_length)
            spark.lt(90)
        initial_length -= increment


# Square
def draw_square(walker_object, side_length=100):
    for _ in range(4):
        walker_object.fd(side_length)
        walker_object.lt(90)
    screen.exitonclick()


# Dashed line
def draw_dashed(walker_object, length, dash_length=8, space_length=5):
    current_length = 0
    while current_length < length:
        walker_object.pd()
        walker_object.forward(dash_length)
        walker_object.pu()
        walker_object.forward(space_length)
        current_length += dash_length
        current_length += space_length


# Draw n-gons
def draw_ngon(walker_object, n_sides, side_length):
    for side in range(n_sides):
        # Random color for each line per instruction
        walker_object.pencolor(random_rgb)
        walker_object.fd(side_length)
        walker_object.rt(360 / n_sides)


# Random walk
def random_walk(walker_object, n_steps: int = 0, step_length: int = 50, is_color_random: bool = False):
    angles = [0, 90, 180, -90]
    for step in range(n_steps):
        walker_object.fd(step_length)
        walker_object.lt(choice(angles))
        if is_color_random:
            walker_object.pencolor(random_rgb())


# Generate random RGB for randomising color
def random_rgb():
    """Generates a tuple of RGB values ranging from 0 to 255
    """
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return (r, g, b)


# Spirograph
def draw_spirograph(walker_object, n_circles, radius):
    current_angle = 0
    for _ in range(n_circles):
        walker_object.pencolor(random_rgb())
        walker_object.circle(radius)
        current_angle += 360 / n_circles
        walker_object.seth(current_angle)


spark.speed(0)
draw_spirograph(spark, 33, 100)

screen.exitonclick()
