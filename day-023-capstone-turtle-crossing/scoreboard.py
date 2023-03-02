from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """Responsible for showing and updating the level on screen.

    Args:
        Turtle (_type_): turtleObject
    """

    def __init__(self) -> None:
        """Setup for display"""
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-285, 255)
        self.level = 0
        self.update()

    def update(self) -> None:
        """Update score and display."""
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self) -> None:
        """Display gave over screen."""
        self.clear()
        self.write(f"Level: {self.level} (GAME OVER)", font=FONT)
