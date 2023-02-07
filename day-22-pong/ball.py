from turtle import Turtle
from random import random


class Ball(Turtle):
    """Responsible for creating the ball and its movement and collisions.

    Args:
        Turtle (turtleObject): Turtle object
    """

    def __init__(
        self, screen_size: tuple, margin: int, player_size: tuple, radius: int = 10
    ) -> None:
        """Initialise ball parameters.

        Args:
            screen_size (tuple): size of game screen in pixels (x, y)
            margin (int): offset from screen edge
            player_size (tuple): width and height of player paddle in pixels (width, height)
            radius (int, optional): radius of ball. Defaults to 10.
        """
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.current_speed = 3
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

    def move(self) -> None:
        """Moves the ball"""
        x = self.xcor()
        y = self.ycor()
        self.setx(x + (self.current_speed * self.x_mult))
        self.sety(y + (self.current_speed * self.y_mult))

    def bounce_y(self) -> None:
        self.y_mult *= -1

    def bounce_x(self) -> None:
        self.x_mult *= -1

    def wall_collision(self) -> bool:
        """Checks for TOP and BOTTOM wall collision with the ball

        Returns:
            bool: return True if ball hits top or bottom wall. False otherwise
        """
        top_border_pos = (self.screen_size[1] / 2) - (self.margin + 15)
        bot_border_pos = -top_border_pos
        if self.ycor() >= top_border_pos or self.ycor() <= bot_border_pos:
            return True
        False

    def player_horizontal_collision(
        self, player_position: tuple, accel: float = 0.75
    ) -> bool:
        """Checks if ball collides with player

        Args:
            player_position (tuple): player's current x and y coordinates (x, y)
            accel (float, optional): adds to the current speed of the ball per unit. Defaults to 0.75.

        Returns:
            bool: returns True if ball hits player. False otherwise
        """
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
            self.current_speed += accel
            return True
        return False

    def start_position(self) -> None:
        self.goto(0, 0)
        self.current_speed = 3
