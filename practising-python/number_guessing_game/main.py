import random
import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def play_game(number, difficulty):
    game_over = False

    if difficulty == "easy":
        chances = 10
    else:
        chances = 5

    print(f"You get {chances} chances.")
    while not game_over and chances != 0:
        guess = int(input("\nGuess a number: "))

        if guess == number:
            print("Correct guess! You win.")
            game_over = True

        else:
            chances -= 1
            if guess > number:
                print("Wrong! You guessed too high.")
            else:
                print("Wrong! You guessed too low.")
            print("Remaining chances:", chances)


clear_console()

print("Welcome to the number guessing game!")
difficulty = input("Enter difficulty level (easy/hard): ").lower()

while difficulty != "easy" and difficulty != "hard":
    print("Invalid input. Please enter a valid difficulty level.")
    difficulty = input("Enter difficulty level (easy/hard): ").lower()

number = random.randint(1, 50)
play_game(number, difficulty)
