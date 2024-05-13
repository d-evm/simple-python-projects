from turtle import Turtle


class Score(Turtle):
    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.color("#808080")
        self.pu()
        self.hideturtle()

        self.player1 = 0
        self.player2 = 0
        self.display_score()

    def display_score(self):
        self.clear()
        self.goto(100, 150)
        self.write(self.player1, align="center", font=("Arial", 100))

        self.goto(-100, 150)
        self.write(self.player2, align="center", font=("Arial", 100))

    def update_score(self, player):
        if player == 1:
            self.player1 += 1

        else:
            self.player2 += 1

        self.display_score()

    def display_final_score(self):
        self.clear()
        self.color("white")
        self.goto(100, 0)
        self.write(self.player1, align="center", font=("Arial", 300))

        self.goto(-100, 0)
        self.write(self.player2, align="center", font=("Arial", 300))
