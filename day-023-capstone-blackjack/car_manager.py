from turtle import Turtle
from player import FINISH_LINE_Y, STARTING_POSITION
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 1


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.spawn_prob = 0.96
        self.penup()
        self.hideturtle()
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self) -> object:
        car = Turtle()
        car.penup()
        car.color(random.choice(COLORS))
        car.shape("square")
        car.setheading(180)
        y_start = STARTING_POSITION[1] + 50
        y_stop = FINISH_LINE_Y - 40
        y_rand = random.randrange(y_start, y_stop)

        car.goto(330, y_rand)
        car.turtlesize(stretch_len=2)
        self.all_cars.append(car)
        return car

    def rand_create_car(self) -> bool:
        x = random.random()
        if x >= self.spawn_prob:
            self.create_car()
            return True
        return False

    def move_cars(self) -> None:
        for car in self.all_cars:
            car.forward(self.move_distance)

    def car_finish(self, car) -> bool:
        if car.xcor() <= -400:
            return True
        return False

    def remove_car(self, car) -> bool:
        try:
            self.all_cars.remove(car)
            return True
        except ValueError:
            return False

    def start(self):
        self.move_cars()
        finished_cars = []
        for car in self.all_cars:
            if self.car_finish(car):
                finished_cars.append(car)

        for finished_car in finished_cars:
            finished_car.clear()
            finished_car.hideturtle()
            self.remove_car(finished_car)

        finished_cars = []

    def level_up(self) -> None:
        self.move_distance += MOVE_INCREMENT
        if self.spawn_prob > 0.8:
            self.spawn_prob -= 0.011
