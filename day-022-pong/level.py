from turtle import Turtle


class Level(Turtle):
    """Creates game borders and center line.

    Args:
        Turtle (turtleObject): Turtle!
    """

    def __init__(self, size: tuple, margin: int) -> None:
        """Initialise level parameters

        Args:
            size (tuple): screen size in pixels (x, y)
            margin (int): border offset in p-ixels
        """
        super().__init__()
        self.size = size
        self.margin = margin

        self.speed(0)
        self.hideturtle()
        self.pensize(5)
        self.color("white")

    def create_border(self) -> None:
        """Draws out the four borders of the game"""
        x = -(self.size[0] / 2) + self.margin
        y = -(self.size[1] / 2) + self.margin

        self.penup()
        self.goto(x, y)
        self.setheading(0)
        self.pendown()
        for i in range(2):
            self.forward(self.size[0] - (self.margin * 2))
            self.left(90)
            self.forward(self.size[1] - (self.margin * 2))
            self.left(90)

    def create_line(self, length, interval):
        """Draws center line

        Args:
            length (int): length of each line in pixels
            interval (int): gap between each line in pixels
        """
        x = 0
        y = -(self.size[1] / 2) + self.margin
        y2 = -y
        self.penup()
        self.goto(x, y)
        self.setheading(90)
        self.pendown()
        while self.ycor() < y2:
            self.pendown()
            self.forward(length)
            self.penup()
            self.forward(interval)
