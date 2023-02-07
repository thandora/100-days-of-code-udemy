from turtle import Turtle
from random import random


class Ball(Turtle):
    def __init__(
        self, screen_size: tuple, margin: int, player_size: tuple, radius: int = 10
    ):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed = 3
        self.shapesize(((radius * 2) / 20), ((radius * 2) / 20))
        self.radius = radius

        self.screen_size = screen_size
        self.margin = margin
        self.x_mult = 0
        self.y_mult = 0
        while self.x_mult < 0.45 or self.y_mult < 0.45:
            self.x_mult = random()
            self.y_mult = random()
        self.player_width = player_size[0]
        self.player_height = player_size[1]

    def move(self):
        x = self.xcor()
        y = self.ycor()
        self.setx(x + (self.speed * self.x_mult))
        self.sety(y + (self.speed * self.y_mult))

    def bounce_y(self):
        self.y_mult *= -1

    def bounce_x(self):
        self.x_mult *= -1

    def wall_collision(self) -> bool:
        top_border_pos = (self.screen_size[1] / 2) - (self.margin + 15)
        bot_border_pos = -top_border_pos
        if self.ycor() >= top_border_pos or self.ycor() <= bot_border_pos:
            return True
        False

    def player_horizontal_collision(
        self, player_position: tuple, accel: int = 0.75
    ) -> bool:
        # Player coordinates
        p_x = player_position[0]
        p_y = player_position[1]
        # Player dimensions
        p_w = self.player_width
        p_h = self.player_height

        # Ball
        rad = self.radius
        b_x = self.xcor()
        b_y = self.ycor()
        if (
            (abs(p_x - b_x) < ((p_w / 2) + rad))
            and (b_y < (p_y + (p_h / 2) + rad))
            and (b_y > (p_y - (p_h / 2) - rad))
        ):
            self.speed += accel
            return True
        return False

    def start_position(self):
        self.goto(0, 0)
