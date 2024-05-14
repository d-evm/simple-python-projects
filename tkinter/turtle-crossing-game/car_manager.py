from turtle import Turtle
import random as r
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2
VER_ACTIVE_AREA = 300
HOR_ACTIVE_AREA = 300


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        i = r.randint(1, 6)
        if i == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(r.choice(COLORS))
            new_car.pu()
            new_car.goto(HOR_ACTIVE_AREA-20,
                         r.randrange(-VER_ACTIVE_AREA, VER_ACTIVE_AREA, 30))
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def levelup(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()
        self.car_speed += MOVE_INCREMENT
