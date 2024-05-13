import turtle as t
from random import randint
import os
os.system('cls' if os.name == 'nt' else 'clear')

game_is_on = False
screen = t.Screen()
screen.title("Turtle Race")
screen.setup(width=500, height=400)
colors = ["blue", "red", "green", "yellow", "orange"]
positions = [-60, -30, 0, 30, 60]
turtles = []

for i in range(5):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.pu()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=positions[i])
    turtles.append(new_turtle)

user_bet = screen.textinput(
    title="Make a bet", prompt="Which color would you pick?").lower()

if user_bet not in colors:
    while user_bet not in colors:
        user_bet = screen.textinput(
            title="Make a bet", prompt="No such color available!\nWhich color would you pick?").lower()

game_is_on = True

while game_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_is_on = False
            winning_color = turtle.pencolor()

            if user_bet == winning_color:
                print(
                    f"You win! {(winning_color.capitalize())} turtle won the race.")
            else:
                print(
                    f"You lose! {(winning_color.capitalize())} turtle won the race.")

        else:
            turtle.fd(randint(1, 10))

screen.exitonclick()
