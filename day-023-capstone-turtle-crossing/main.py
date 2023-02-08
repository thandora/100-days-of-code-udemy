import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Game setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")
sparky = Player()
car_dealer = CarManager()
scoreboard = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(sparky.up, "Up")


game_is_on = True
while game_is_on:
    time.sleep(1 / 30)

    # Creates car in random interval.
    car_dealer.rand_create_car()

    # Moves all car
    car_dealer.start()

    # Player and car collision
    for car in car_dealer.all_cars:
        if sparky.car_collide(car):
            scoreboard.game_over()
            game_is_on = False

    # Player at finish line check.
    if sparky.at_finish():
        scoreboard.update()
        sparky.to_start()
        car_dealer.level_up()

    screen.update()

screen.exitonclick()
