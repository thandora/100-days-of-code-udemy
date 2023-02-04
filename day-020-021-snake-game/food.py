import random
from turtle import Turtle


class Food:
    def __init__(
        self, screen_size: tuple, snake_size: int, color="blue", size: int = 10
    ) -> None:

        self.screen_size = screen_size
        self.size = size
        self.snake_size = snake_size
        self.collision_box = None
        # Initialise food
        self.food = Turtle(shape="circle")
        self.food.penup()
        self.food.turtlesize(size / 20, size / 20)
        self.food.color(color)

        rand_coordinates = self.rand_coordinates()
        self.coordinates = rand_coordinates

    def rand_coordinates(self) -> tuple:
        # Yes you can simplify the equation, but this is more intuitive
        x_limit = round(self.screen_size[0] / 2)
        y_limit = round(self.screen_size[1] / 2)
        x_limit_right = list(range(0, x_limit, self.snake_size))
        y_limit_up = list(range(0, y_limit, self.snake_size))
        x_limit_left = []
        y_limit_down = []
        for x in x_limit_right:
            x_limit_left.append(-x)
        for y in y_limit_up:
            y_limit_down.append(-y)

        x = set(x_limit_right + x_limit_left)
        y = set(y_limit_up + y_limit_down)

        x_rand = random.choice(list(x))
        y_rand = random.choice(list(y))

        return tuple([x_rand, y_rand])

    def spawn(self) -> tuple:
        """Creates food turtle object at a random coordinate on the screen

        Returns:
            tuple: random coordinate on the screen
        """
        coordinates = self.rand_coordinates()
        self.food.goto(coordinates)
        self.coordinates = coordinates
        return coordinates

    def collided(self, other_coordinate: tuple) -> True:
        """Returns if other_coordinate collides with Food object

        Args:
            snake_coordinate (tuple): coordinate of other object

        Returns:
            True: if hit
            False: if not hit
        """
        # Later found out that the turtle module has a distance() method
        # that makes this job way easier. This was good exercise exercise tho.
        x_lower = self.coordinates[0] - (self.size / 20)
        x_higher = self.coordinates[0] + (self.size / 20)
        y_lower = self.coordinates[1] - (self.size / 20)
        y_higher = self.coordinates[1] + (self.size / 20)
        x = other_coordinate[0]
        y = other_coordinate[1]

        if x >= x_lower and x <= x_higher:
            if y >= y_lower and y <= y_higher:
                return True

        return False
