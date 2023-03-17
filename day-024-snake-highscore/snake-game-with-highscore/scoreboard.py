from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):
    def __init__(
        self,
        snake: object,
        food: object,
        screen_size: tuple,
        margin: int = 30,
        high_score: int = 0,
    ) -> None:
        super().__init__()
        self.snake = snake
        self.food = food
        self.score = 0
        self.high_score = high_score
        self.penup()
        self.hideturtle()
        self.goto(0, ((screen_size[1] / 2) - margin))

    def scored(self) -> int:
        self.score += 1
        return self.score

    def show(self) -> None:
        self.clear()
        self.write(
            f"Score: {self.score}, High score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.show()

    def gameover(self) -> None:
        self.goto(0, 0)
        self.write("GAME\nOVER", align=ALIGNMENT, font=("Courier", 50, "bold"))
