from turtle import Turtle


class Player(Turtle):
    def __init__(
        self,
        length: int,
        screen_size: tuple,
        screen_margin: int,
        location: str = "left",
    ):
        super().__init__()
        self.length = length
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.turtlesize(stretch_len=length / 20)
        self.speed(0)

        # 15 is offself from screen border.
        # For the player to touch the border, use offset of 12.5
        if location == "left":
            x = (-(screen_size[0] / 2) + screen_margin) + 15
        elif location == "right":
            x = -((-(screen_size[0] / 2) + screen_margin) + 15)

        self.goto(x, 0)

    def up(self):
        self.forward(10)
        # new_y = self.ycor() + 20
        # self.goto(self.xcor(), new_y)

    def down(self):
        self.backward(10)
