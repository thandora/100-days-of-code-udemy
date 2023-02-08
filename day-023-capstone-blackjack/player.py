from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("square")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self) -> None:
        """Method used for turtleScreen object. It allows Player movement."""
        self.forward(MOVE_DISTANCE)

    def at_finish(self) -> bool:
        """bool to check if player has reached finsih line.

        Returns:
            bool: True if at finish, false otherwise.
        """
        if self.ycor() >= FINISH_LINE_Y:
            return True
        return False

    def to_start(self) -> None:
        self.goto(STARTING_POSITION)

    def car_collide(self, car) -> bool:
        """Checks if Player object collides with a rectangular car.

        Args:
            car (_type_): turtle object of car

        Returns:
            bool: returns True if the objects collide, False otherwise
        """
        car_x_width = car.shapesize()[1] * 21
        player_x_width = self.shapesize()[0] * 21
        width_correction = (car_x_width + player_x_width) / 2

        car_y_width = car.shapesize()[0] * 21
        player_y_width = self.shapesize()[1] * 21
        height_correction = (car_y_width + player_y_width) / 2

        x_distance = abs(car.xcor() - self.xcor())
        y_distance = abs(car.ycor() - self.ycor())

        if x_distance < width_correction and y_distance < height_correction:
            return True
        else:
            return False
