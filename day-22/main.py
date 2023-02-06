from turtle import Screen
from level import Level
from player import Player
from time import sleep

# TODO debugging
SCREEN_SIZE = (1200, 800)
SCREEN_MARGIN = 60
PLAYER_LENGTH = 80
screen = Screen()
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.bgcolor("black")
screen.title("Pong")
level = Level(size=SCREEN_SIZE, margin=SCREEN_MARGIN)
level.create_border()
level.create_line(length=20, interval=50)
screen.tracer(0)


player_a = Player(
    length=PLAYER_LENGTH,
    screen_size=SCREEN_SIZE,
    screen_margin=SCREEN_MARGIN,
)

player_b = Player(
    length=PLAYER_LENGTH,
    screen_size=SCREEN_SIZE,
    screen_margin=SCREEN_MARGIN,
    location="right",
)
screen.listen()

screen.onkeypress(player_a.up, "w")
screen.onkeypress(player_a.down, "s")
screen.onkeypress(player_b.up, "Up")
screen.onkeypress(player_b.down, "Down")

while True:
    sleep(0.0000000001)
    # player_a.left(90)
    # sc
    screen.update()
    screen.exitonclick()
