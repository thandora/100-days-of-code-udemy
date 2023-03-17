from turtle import Turtle, Screen

spark = Turtle()
screen = Screen()


class TurtleFuncs:
    def __init__(self, turtle_object):
        self.turtle = turtle_object

    def forward(self):
        self.turtle.forward(15)

    def backward(self):
        self.turtle.backward(15)

    def cw(self):
        self.turtle.right(12)

    def ccw(self):
        self.turtle.left(12)

    def reset(self):
        self.turtle.reset()


spark_control = TurtleFuncs(spark)
sc = spark_control
screen.listen()
# Controls
screen.onkeypress(fun=sc.forward, key="Up")
screen.onkeypress(fun=sc.backward, key="Down")
screen.onkeypress(fun=sc.cw, key="Right")
screen.onkeypress(fun=sc.ccw, key="Left")
screen.onkeypress(fun=sc.reset, key="space")

screen.exitonclick()
