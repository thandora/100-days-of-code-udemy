from turtle import Turtle


class Scoreboard(Turtle):
    """Draws out scoreboard, keeps track of scores, and update it.

    Args:
        Turtle (turtleObject): Turtle!!!
    """

    def __init__(self, screen_size: tuple):
        """Scoreboard parameters

        Args:
            screen_size (tuple): size of game screen in pixels (x, y)
        """
        super().__init__()
        self.screen_size = screen_size
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_a = 0
        self.score_b = 0
        self.update()

    def update(self):
        """Updates drawn scoreboard with updated (intended) scores"""
        self.clear()
        self.goto(-100, (self.screen_size[1] / 2 - 155))
        self.write(self.score_a, align="center", font=("Courier", 70, "normal"))
        self.goto(100, (self.screen_size[1] / 2 - 155))
        self.write(self.score_b, align="center", font=("Courier", 70, "normal"))

    def add_score_a(self):
        """Updates Scoreboard.score_a and scoreboard"""
        self.score_a += 1
        self.update()

    def add_score_b(self):
        """Updates Scoreboard.score_b and scoreboard"""
        self.score_b += 1
        self.update()
