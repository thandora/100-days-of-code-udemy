from turtle import Turtle
from player import FINISH_LINE_Y, STARTING_POSITION
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 1


class CarManager(Turtle):
    """Responsible for creating, deleting, and managing cars of game.

    Args:
        Turtle (_type_): turtleObject
    """

    def __init__(self) -> None:
        super().__init__()

        # Spawn probability of each car. Used for creating cars in random intervals.
        self.spawn_prob = 0.96

        self.penup()
        self.hideturtle()
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self) -> object:
        """Creates a car turtle object with a random color.

        Returns:
            object: returns car
        """
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
        """Create a car at random intervals.

        Returns:
            bool: returns True if succesful on creating car, False if not.
        """
        x = random.random()
        if x >= self.spawn_prob:
            self.create_car()
            return True
        return False

    def move_cars(self) -> None:
        """Move all cars in CarManager.all_cars that have not crossed the screen border."""
        for car in self.all_cars:
            car.forward(self.move_distance)

    def car_finish(self, car) -> bool:
        """Checks if car crossed left screen border.

        Args:
            car (_type_): car turtleObject

        Returns:
            bool: returns True if crossed border, False otherwise.
        """
        if car.xcor() <= -400:
            return True
        return False

    def remove_car(self, car) -> bool:
        """Removes car from CarManager.all_cars if it reaches left screen border.

        Args:
            car (_type_): car turtleObject

        Returns:
            bool: True if removed. False if car does not exist in list.
        """
        try:
            self.all_cars.remove(car)
            return True
        except ValueError:
            return False

    def start(self):
        """Handles movement and removing of cars."""
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
        """Increases cars' move distance per unit time (effectively increasing their speed),
        and probability of spawning."""
        self.move_distance += MOVE_INCREMENT
        if self.spawn_prob > 0.8:
            self.spawn_prob -= 0.011
