import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")
sparky = Player()
car_dealer = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(sparky.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(1 / 30)
    car_dealer.rand_create_car()
    car_dealer.start()
    for car in car_dealer.all_cars:
        if sparky.car_collide(car):
            scoreboard.game_over()
            game_is_on = False

    if sparky.at_finish():
        scoreboard.update()
        sparky.to_start()
        car_dealer.level_up()

    screen.update()
 
screen.exitonclick()
