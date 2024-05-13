from turtle import Turtle
import random as r


class Food(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.shape("circle")
        self.pu()
        self.color("orange")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        rand_x = r.randint(-270, 270)
        rand_y = r.randint(-270, 250)
        self.goto(rand_x, rand_y)

    def refresh(self):
        rand_x = r.randint(-270, 270)
        rand_y = r.randint(-270, 270)
        self.goto(rand_x, rand_y)
