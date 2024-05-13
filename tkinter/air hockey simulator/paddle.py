from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.goto(x=position, y=0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
