import turtle as t
import os
os.system('cls' if os.name == 'nt' else 'clear')


def move_fd():
    tim.fd(5)


def move_bd():
    tim.backward(5)


def turn_r():
    tim.right(5)


def turn_l():
    tim.left(5)


def clear_screen():
    tim.reset()


tim = t.Turtle()
screen = t.Screen()

screen.listen()
screen.onkeypress(key="w", fun=move_fd)
screen.onkeypress(key="s", fun=move_bd)
screen.onkeypress(key="d", fun=turn_r)
screen.onkeypress(key="a", fun=turn_l)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
