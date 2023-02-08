from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self) -> None:
        self.forward(MOVE_DISTANCE)

    def at_finish(self) -> bool:
        """bool to check if player has reached finsih line.

        Returns:
            bool: True if at finish, false otherwise.
        """
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False
