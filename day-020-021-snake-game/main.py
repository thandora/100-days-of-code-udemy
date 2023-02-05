from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from levels import Level1
import time

SCREEN_SIZE = (800, 800)
START_POSITION = (0, 0)
START_LENGTH = 3
SCREEN_MARGIN = 25
SNAKE_SPEED = 20
x = (SCREEN_SIZE[0] / 2) - SCREEN_MARGIN
y = (SCREEN_SIZE[1] / 2) - SCREEN_MARGIN
# This represents the coordinates of each of the border
LEVEL_BORDERS = [-x, x, -y, y]

# Setup
screen = Screen()
level = Level1(SCREEN_SIZE, margin=SCREEN_MARGIN)
# Turn off automatic drawing animation
screen.tracer(0)
screen.update()
level.create()
screen.setup(width=SCREEN_SIZE[0], height=SCREEN_SIZE[1])
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snakey")
screen.listen()

berry = Food(
    screen_size=SCREEN_SIZE, color="red", snake_size=20, size=10, margin=SCREEN_MARGIN
)
snek = Snake(start_pos=START_POSITION)
snek.init_head(20, "white")
snek.make_segments(START_LENGTH - 1, color="grey")

scoreboard = Scoreboard(snake=snek, food=berry, screen_size=SCREEN_SIZE)
scoreboard.color("white")
screen.update()

# Buffer to wait for the window to fully open
time.sleep(1)

berry.spawn()
scoreboard.show()

# Direction control
screen.onkeypress(fun=snek.up, key="Up")
screen.onkeypress(fun=snek.down, key="Down")
screen.onkeypress(fun=snek.left, key="Left")
screen.onkeypress(fun=snek.right, key="Right")

in_play = True
while in_play:
    screen.update()
    position = snek.move(1, speed=SNAKE_SPEED)

    if snek.self_hit():
        scoreboard.gameover()
        in_play = False
    if berry.collided(position):
        berry.spawn()
        scoreboard.scored()
        scoreboard.show()
        snek.extend()

    if (
        snek.head.xcor() < LEVEL_BORDERS[0]
        or snek.head.xcor() > LEVEL_BORDERS[1]
        or snek.head.ycor() < LEVEL_BORDERS[2]
        or snek.head.ycor() > LEVEL_BORDERS[3]
    ):
        scoreboard.gameover()
        in_play = False


screen.exitonclick()
