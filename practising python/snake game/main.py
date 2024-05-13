import turtle as t
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

screen_text = t.Turtle()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen_text.pu()
screen_text.hideturtle()
screen_text.goto(0, 0)
screen_text.color("white")

is_paused = False
game_is_on = True


def pause_game():
    global is_paused
    is_paused = not is_paused


def quit_game():
    global game_is_on
    screen_text.clear()
    game_is_on = False


def continue_game():
    global is_paused
    is_paused = False


screen.listen()
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")

screen.onkey(pause_game, "space")
screen.onkey(quit_game, "q")
screen.onkey(continue_game, "c")

while game_is_on:
    if not is_paused:
        screen_text.clear()
        screen.update()
        time.sleep(0.1)
        snake.move()

        # detect collison with food
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.blink("green")
            scoreboard.inc_score()
            scoreboard.update_highscore()
            scoreboard.update_scoreboard()
            snake.extend()

        # detect collison with wall
        if (
            snake.segments[0].xcor() > 290
            or snake.segments[0].xcor() < -290
            or snake.segments[0].ycor() > 290
            or snake.segments[0].ycor() < -290
        ):
            scoreboard.reset_score()
            snake.blink("red")
            snake.reset_position()

        # detect collison with tail
        for segment in snake.segments[2:]:
            if snake.segments[0].distance(segment) < 10:
                scoreboard.reset_score()
                snake.blink("red")
                snake.remove_segment(snake.segments.index(segment))

    else:
        screen_text.write(
            arg="   Press 'q' to quit.  \nPress 'c' to continue.",
            align="center",
            font=("Arial", 18, "normal"),
        )

    screen.update()

scoreboard.gameover()
screen.exitonclick()
