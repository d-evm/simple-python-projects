import random
import os
from art import logo, vs
from game_data import data


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def play_game():
    clear()
    gameover = False
    score = 0

    while not gameover:
        account_a = random.choice(data)
        account_b = random.choice(data)

        while account_b == account_a:
            account_b = random.choice(data)

        clear()
        print(logo)
        print("\nScore: ", score)
        print("Celeb-A: ", format_data(account_a))
        print("v/s")
        print("Celeb-B: ", format_data(account_b))
        guess = input(f"\nWho has more followers? Type 'A' or 'B': ").lower()
        print()

        if guess == "a":
            if account_a["follower_count"] > account_b["follower_count"]:
                score += 1
                print(f"Correct answer! \nScore: {score}")
            else:
                print("Oops! Wrong answer. You lose :(")
                print("Score: ", score)
                gameover = True
        elif guess == "b":
            if account_a["follower_count"] < account_b["follower_count"]:
                score += 1
                print(f"Correct answer! \nScore: {score}")
            else:
                clear()
                print(logo)
                print("\nOops! Wrong answer. You lose :(")
                print(
                    f"{account_a['name']}'s followers: {account_a['follower_count']}M")
                print(
                    f"{account_b['name']}'s followers: {account_b['follower_count']}M")

                print("\nScore: ", score)
                gameover = True
        else:
            print("Invalid input. Please enter 'A' or 'B'.")


play_game()
