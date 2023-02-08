from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-285, 255)
        self.level = 0
        self.update()

    def update(self) -> None:
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self) -> None:
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level} (GAME OVER)", font=FONT)

    
