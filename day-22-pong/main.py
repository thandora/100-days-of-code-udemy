from turtle import Screen
from level import Level
from player import Player
from time import sleep
from ball import Ball
from scoreboard import Scoreboard

# TODO
# 1. Add winner screen
# 2. Stop paddle from going out of bounds
# Game setup
SCREEN_SIZE = (1200, 800)
SCREEN_MARGIN = 60
PLAYER_SIZE = (20, 80)
PLAYER_LENGTH = PLAYER_SIZE[1]
ACCELERATION = 0.6
screen = Screen()
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard(screen_size=SCREEN_SIZE)
level = Level(size=SCREEN_SIZE, margin=SCREEN_MARGIN)
level.create_border()
level.create_line(length=20, interval=50)

ball = Ball(screen_size=SCREEN_SIZE, margin=SCREEN_MARGIN, player_size=PLAYER_SIZE)

# Player paddles setup
player_a = Player(
    length=PLAYER_LENGTH,
    screen_size=SCREEN_SIZE,
    screen_margin=SCREEN_MARGIN,
    location="left",
)
player_b = Player(
    length=PLAYER_LENGTH,
    screen_size=SCREEN_SIZE,
    screen_margin=SCREEN_MARGIN,
    location="right",
)
screen.listen()

# Controls
screen.onkeypress(player_a.up, "w")
screen.onkeypress(player_a.down, "s")
screen.onkeypress(player_b.up, "Up")
screen.onkeypress(player_b.down, "Down")

in_play = True
while in_play:
    sleep(1 / 144)
    ball.move()

    if ball.wall_collision():
        ball.bounce_y()

    if ball.player_horizontal_collision(player_b.position(), accel=ACCELERATION):
        ball.bounce_x()
    if ball.player_horizontal_collision(player_a.position(), accel=ACCELERATION):
        ball.bounce_x()

    if ball.xcor() > player_b.xcor():
        ball.start_position()
        scoreboard.add_score_a()

    if ball.xcor() < player_a.xcor():
        ball.start_position()
        scoreboard.add_score_b()

    if scoreboard.score_a >= 5 or scoreboard.score_b >= 5:
        in_play = False

    screen.update()

screen.exitonclick()
