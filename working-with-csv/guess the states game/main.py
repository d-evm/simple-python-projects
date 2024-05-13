import turtle
import pandas as pd

import os
os.system('cls' if os.name == 'nt' else 'clear')

image_path = "blank_states_img.png"
data_file_path = "50_states.csv"

screen = turtle.Screen()
screen.title("U.S. States Game")
image = image_path
screen.bgpic(image_path)

data = pd.read_csv(data_file_path)

states_data = data["state"].to_list()

game_is_on = True

guessed_states = []


def exit_game():
    global game_is_on

    missing_states = [
        state for state in states_data if state not in guessed_states]
    new_data = pd.DataFrame(missing_states)
    new_data.to_csv(
        "user_data.csv")

    print(missing_states)
    game_is_on = False


def take_input(prompt_text):
    global game_is_on

    answer = screen.textinput(title=f"{len(guessed_states)}/50 guessed.",
                              prompt=prompt_text)

    answer = str(answer)
    answer = answer.capitalize()

    if answer in guessed_states:
        take_input("The state you entered is already guessed. Enter a new state.")

    elif answer in states_data:
        state_details = data[data.state == answer]
        text = turtle.Turtle()
        text.hideturtle()
        text.pu()
        text.goto(float(state_details.x), float(state_details.y))
        text.write(answer)
        guessed_states.append(answer)

    elif answer == "End":
        exit_game()

    elif len(guessed_states) >= 50:
        print("Congrats! You've made all the guesses")
        game_is_on = False

    else:
        take_input(
            "The state you entered does not exist!\nRe-write the name of the state you were trying to enter.")


while game_is_on:
    prompt_text = "Write name of a state."
    take_input(prompt_text)


screen.mainloop()
