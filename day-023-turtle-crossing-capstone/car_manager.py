from turtle import Turtle
import random
from player import FINISH_LINE_Y, STARTING_POSITION
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.hideturtle()
        self.car_list = []
        self.move_distance = STARTING_MOVE_DISTANCE


    def create_car(self) -> object:
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.setheading(180)
        y_start = STARTING_POSITION[1] + 50
        y_stop = FINISH_LINE_Y - 10
        y_rand = random.randrange(y_start, y_stop)

        # Debug
        car.goto(0, y_rand)
        # Uncomment next line
        # car.goto(330, y_rand)
        car.turtlesize(stretch_len=3)
        self.car_list.append(car)
        return car

    def move_cars(self) -> None:
        for car in self.car_list:
            car.forward(self.move_distance)
