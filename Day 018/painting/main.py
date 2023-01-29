import random
import colorgram
from turtle import Turtle, Screen

# Initialise
spark = Turtle()
spark.hideturtle()
screen = Screen()
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

    def paint(self, width, height, spacing, is_random=False):
        dot_radius = self.turtle.pensize()
        # -1 is there because somehow the dot size starts at 0, not 1
        spacing_distance = (dot_radius * 2) + spacing - 1

        for c_height in range(height):
            for c_width in range(width):
                if is_random:
                    random_color = random.choice(self.palette)
                    self.turtle.pencolor(random_color)
                self.turtle.pu()
                self.turtle.dot()
                # Don't move turtle if drawing last dot in row
                if c_width == (width - 1):
                    if not c_height == (height - 1):
                        # If turtle is going right:
                        if self.turtle.heading() == 0:
                            self.turtle.rt(90)
                            self.turtle.forward(spacing_distance)
                            self.turtle.rt(90)
                        else:
                            self.turtle.lt(90)
                            self.turtle.forward(spacing_distance)
                            self.turtle.lt(90)
                    continue

                self.turtle.forward(spacing_distance)


painter = SpotPainter(spark, 15, colors)
painter.turtle.speed(0)
painter.paint(5, 15, 15, True)
print(painter.turtle.pensize())
screen.exitonclick()
