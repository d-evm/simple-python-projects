from turtle import Turtle

UP = 10
DOWN = -10


class Ball(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.pu()
        self.color("red")
        self.y_direction = UP
        self.x_direction = 10
        self.move_speed = 0.1

    def move(self):
        if self.ycor() >= 285:
            self.goto(self.xcor() + self.x_direction, self.ycor() - 10)
            self.y_direction = DOWN

        elif self.ycor() <= -285:
            self.goto(self.xcor() + self.x_direction, self.ycor() + 10)
            self.y_direction = UP

        else:
            self.goto(self.xcor() + self.x_direction,
                      self.ycor() + self.y_direction)

    def bounce(self):
        self.x_direction = -(self.x_direction)
        self.goto(self.xcor() + self.x_direction,
                  self.ycor() + self.y_direction)
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.x_direction = -(self.x_direction)
        self.move_speed = 0.1
