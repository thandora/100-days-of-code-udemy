from turtle import Turtle, Screen

spark = Turtle()
screen = Screen()


class TurtleFuncs:
    def __init__(self, turtle_object):
        self.turtle = turtle_object

    def forward(self):
        self.turtle.forward(10)

    def backward(self):
        self.turtle.backward(10)

    def cw(self):
        self.turtle.right(5)

    def ccw(self):
        self.turtle.left(5)


spark_control = TurtleFuncs(spark)
sc = spark_control
screen.listen()
screen.onkeypress(sc.forward, "Up")
screen.onkeypress(sc.backward, "Down")
screen.onkeypress(sc.cw, "Right")
screen.onkeypress(sc.ccw, "Left")
screen.exitonclick()
