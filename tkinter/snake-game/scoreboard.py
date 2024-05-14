from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 18)


class Scoreboard(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)

        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())

        self.pu()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()

    def inc_score(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}",
                   align=ALIGNMENT, font=FONT)

    def update_highscore(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
            self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
