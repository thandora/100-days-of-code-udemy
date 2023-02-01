from turtle import Screen
from snake import Snake
import time

# Screen setup
screen = Screen()
screen.setup(width=800, height=800)
screen.colormode(255)
screen.bgcolor("black")
screen.title("Snakey")
screen.listen()

# Initial setup
head_start_position = (0, 0)
segments = []
# Turn of automatic drawing animation
screen.tracer(0)

snek = Snake(start_pos=head_start_position)
snek.init_head(20, "white")
snek.make_segments(5, color="grey")
screen.update()
# Buffer to wait for the window to fully open
time.sleep(1)

for _ in range(25):
    snek.move(1)
    screen.onkey(fun=snek.right, key="Right")
    screen.onkey(fun=snek.left, key="Left")
    screen.update()


screen.exitonclick()
