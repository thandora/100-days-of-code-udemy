from turtle import Turtle, Screen


class Level1(Turtle):
    """Generates simple box borders.

    Args:
        Turtle (object): turtle object
    """

    def __init__(self, screen_size: tuple, margin: int = 25) -> None:
        super().__init__()
        self.screen_size = screen_size
        self.margin = margin

    def create(self):
        self.penup()
        x = -(self.screen_size[0] / 2) + self.margin
        y = -(self.screen_size[1] / 2) + self.margin
        self.goto(x, y)
        self.pendown()
        self.pensize(5)
        self.hideturtle()
        self.color("white")
        for i in range(2):
            self.forward(self.screen_size[0] - (self.margin * 2))
            self.left(90)
            self.forward(self.screen_size[1] - (self.margin * 2))
            self.left(90)
