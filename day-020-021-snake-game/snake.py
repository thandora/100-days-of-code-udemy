from turtle import Turtle
import time
import random

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, size: int = 20, start_pos: tuple = (0, 0)) -> None:
        """Snake.segments is ordered in where the head is at index 0.

        Args:
            size (int): default size of segments in pixels. Defaults to 20 pixels
            start_pos (tuple): set of coordinates of where the head will be placed. Defaults to (0, 0)
        """
        self.segments = []
        self.segment_size = size
        self.start_pos = start_pos
        self.head = None
        self.length = len(self.segments)

    def make_segments(
        self,
        n: int,
        size: int = 20,
        color: str = "white",
        rand_color: bool = False,
    ) -> None:
        """Appends n segments to Snake.segments. A snake head is required to make segments.
        To create snake head, use Snake.init_head.

        Args:
            n (int): number of segments to be generated
            size (int): number in pixels. Defaults to 20 pixels
            color (str, optional): Color of head. Color types input is according
            to turtle module. Defaults to "red"
            color_rand (see color): Randomizes color of each segment if True. Defaults to False
        """
        for i in range(n):
            if rand_color:
                color = self.random_rgb()

            segment = Turtle("square")

            # Take coordinates of last segment
            x_start = self.segments[-1].xcor()
            y_start = self.segments[-1].ycor()

            # Segment properties
            segment.penup()
            segment.color(color)
            segment.turtlesize(size / 20, size / 20)

            # Set coordinates size pixels away (measured center to center)
            segment.goto(x_start - size, y_start)
            self.segments.append(segment)
        self.length += n

    def extend(self, color: str = "grey") -> None:
        self.make_segments(n=1, color="grey")

    def head_properties(self, size: int = 20, color: str = "red") -> None:
        """Change properties of head.

        Args:
        size (int, optional): Size of sides in pixels. Defaults to 20.
            color (str, optional): Color of head. Color types input is according
            to turtle module. Defaults to "red".
        """
        self.segments[0].color(color)
        self.segments[0].turtlesize(size / 20, size / 20)

    def init_head(self, size: int = 20, color: str = "white") -> None:
        """Creates the snake head at coordinates Snake.start_pos.

        Args:
            size (int, optional): Size of sides in pixels. Defaults to 20.
            color (str, optional): Color of head. Color types input is according
            to turtle module. Defaults to "red"
        """
        if len(self.segments) == 0:
            (x_coor, y_coor) = self.start_pos
            segment = Turtle("square", visible="False")
            segment.penup()
            segment.goto(x_coor, y_coor)
            self.segments.append(segment)

            self.head_properties(size, color)
            self.head = segment
            self.length += 1
        else:
            # TODO turn this into an error(?)
            print(
                "Head already exists. If you want to edit head properties, use Snake.head()"
            )

    # Generate random RGB for randomising color
    def random_rgb(self) -> tuple:
        """Generates a tuple of RGB values ranging from 0 to 255"""
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return (r, g, b)

    def move(self, steps: int = 1, speed: int = 15) -> tuple:
        """Move the snake n steps.

        Args:
            steps (int, optional): Number of steps taken Each step is equivalent to Snake.segment_size pixels.
            Defaults to 1.
        Returns:
            Tuple: coordinates of current head location
        """

        segments = self.segments
        head = self.head

        # Step steps times.
        for _ in range(steps):
            # Iterate over a range of indices of segments of the snake, excluding the head.
            # e.g if there are 4 segments of the snake (including head), this will iterate over
            # [3, 2, 1]; 3 elements.
            n_segments = self.length
            x = range(1, n_segments)

            indices = list(reversed(x))
            for i in indices:
                # Coordinates of front segment
                coor = segments[i - 1].position()

                # Move current segment to the one in front of it
                segments[i].goto(coor)

            head.forward(self.segment_size)
            time.sleep(1 / speed)
            return head.position()

    def rotate_head(self, direction: str = "right") -> None:
        """Rotates the head 90 degrees clockwise or counter clockwise.

        Args:
            direction (str, optional): "right" / "cw" or "left" / "ccw".
            Defaults to right.
        """
        head = self.head
        if direction.lower() in ["right", "cw"]:
            head.right(90)
        elif direction.lower() in ["left", "ccw"]:
            head.left(90)
        else:
            print('Enter valid direction. "right", "cw", "left", "ccw"')

    def left(self) -> None:
        """Turns Snake.head to the left of the screen only when it is
        already going up or down.
        """

        heading = self.head.heading()
        if heading in [90, 270]:
            self.head.setheading(LEFT)

    def right(self) -> None:
        """Turns Snake.head to the right of the screen only when it is
        already going up or down.
        """
        heading = self.head.heading()
        if heading in [90, 270]:
            self.head.setheading(RIGHT)

    def up(self) -> None:
        """Turns Snake.head up of the screen only when it is
        already going up or down.
        """
        heading = self.head.heading()
        if heading in [0, 180]:
            self.head.setheading(UP)

    def down(self) -> None:
        """Turns Snake.head down of the screen only when it is
        already going up or down.
        """
        heading = self.head.heading()
        if heading in [0, 180]:
            self.head.setheading(DOWN)

    def self_hit(self) -> bool:
        """Checks for snake.head collision with any of its segment.

        Returns:
            bool: True if collision happens. False otherwise
        """
        for part in self.segments[1:]:
            if self.head.distance(part) < 1:
                return True

        return False
