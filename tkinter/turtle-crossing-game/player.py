from turtle import Turtle
import time

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.color("black")
        self.pu()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_turtle(self):
        self.fd(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.ycor() == FINISH_LINE_Y

    def turtle_hit(self):
        for _ in range(3):
            self.color("red")
            self.getscreen().update()
            time.sleep(0.2)
            self.color("black")
            self.getscreen().update()
            time.sleep(0.2)

    def reset_player(self):
        self.goto(STARTING_POSITION)

    def turtle_reached(self):
        for _ in range(3):
            self.color("green")
            self.getscreen().update()
            time.sleep(0.2)
            self.color("black")
            self.getscreen().update()
            time.sleep(0.2)
            self.reset_player()
