from turtle import Turtle


class Player(Turtle):
    """Creates paddle and its movements.

    Args:
        Turtle (turtleObject): Turtle
    """

    def __init__(
        self,
        length: int,
        screen_size: tuple,
        screen_margin: int,
        location: str = "left",
        distance: int = 20,
    ):
        """Initialise paddle parameters

        Args:
            length (int): vertical length of paddle in pixel
            screen_size (tuple): size of game screen in pixels (x, y)
            screen_margin (int): offset of playing area in pixels
            location (str, optional): Where to place paddle. Can choose from ["left", "right"]. Defaults to "left".
            distance (int, optional): Travel distance for each movement. Defaults to 20.
        """
        super().__init__()
        self.length = length
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=length / 20)
        self.speed(0)
        self.travel_distance = distance

        # 15 is offself from screen border.
        # For the player to touch the border, use offset of 12.5
        if location == "left":
            x = (-(screen_size[0] / 2) + screen_margin) + 15
        elif location == "right":
            x = -((-(screen_size[0] / 2) + screen_margin) + 15)

        self.goto(x, 0)

    def up(self):
        """Moves paddle north of screen, Player.travel_distance pixels."""
        self.forward(self.travel_distance)

    def down(self):
        """Moves paddle south of screen, Player.travel_distance pixels."""
        self.backward(self.travel_distance)
