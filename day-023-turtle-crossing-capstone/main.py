import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import sys

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("grey")
sparky = Player()
car_dealer = CarManager()

screen.listen()
screen.onkeypress(sparky.up, "Up")
car_dealer.create_car()

game_is_on = True
for _ in range(100):
    time.sleep(1/14)
    car_dealer.move_cars() 



    screen.update()

#debug\def
screen.update()
screen.exitonclick()