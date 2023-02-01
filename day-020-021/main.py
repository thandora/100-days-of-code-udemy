from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snakey")

head_start_position = (150, 250)
x_start = head_start_position[0]
y_start = head_start_position[1]
turtles = []
for i in range(3):
    turtles.append(Turtle("square", visible="False"))
    turtles[i].penup()
    turtles[i].color("white")
    turtles[i].goto(x_start-(i * 20), y_start)
    turtles[i].tracer()


screen.exitonclick()
