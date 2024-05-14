import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import os
os.system('cls' if os.name == 'nt' else 'clear')

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_turtle, "w")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect car collison
    for any_car in car_manager.all_cars:
        if any_car.distance(player) < 20:
            player.turtle_hit()
            scoreboard.gameover()
            game_is_on = False

    # detect successful crossing
    if player.is_at_finish_line():
        player.turtle_reached()
        car_manager.levelup()
        scoreboard.inc_level()


screen.exitonclick()
