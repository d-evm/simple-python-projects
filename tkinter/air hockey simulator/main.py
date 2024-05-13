from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score

import time
import os
os.system('cls' if os.name == 'nt' else 'clear')

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)
paddle1 = Paddle(350)
paddle2 = Paddle(-350)
ball = Ball()
score = Score()


screen.listen()
screen.onkeypress(paddle1.move_up, "Up")
screen.onkeypress(paddle1.move_down, "Down")
screen.onkeypress(paddle2.move_up, "w")
screen.onkeypress(paddle2.move_down, "s")

game_is_on = True


score.display_score()

while game_is_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.xcor() > 410:
        ball.reset()
        score.update_score(2)

    if ball.xcor() < -410:
        ball.reset()
        score.update_score(1)

    if ball.xcor() > 330 or ball.xcor() < -330:
        if ball.ycor() <= paddle1.ycor() + 50 and ball.ycor() >= paddle1.ycor() - 50:
            ball.bounce()

        elif ball.ycor() <= paddle2.ycor() + 50 and ball.ycor() >= paddle2.ycor() - 50:
            ball.bounce()


screen.clearscreen()
score.display_final_score()


screen.exitonclick()
