import random
from hangman_words import word_list as wl
from hangman_art import stages, logo

print(logo)
print()

chosen_word = random.choice(wl)
word_len = len(chosen_word)
EOG = False
lives = 6

word = ["_"] * word_len
print(word)


while not EOG:
    guess = input("Guess a letter: ").lower()

    if guess == "xxx":
        break

    if guess in word:
        print("You have already guessed that letter.")
        continue

    found = False
    for i in range(word_len):
        if guess == chosen_word[i]:
            word[i] = guess
            found = True

    if not found:
        lives -= 1
        print(
            f"You guessed {guess}, which is not present in the word. You lose a life. (Lives = {lives})")

        if lives == 0:
            print("You lose.")
            EOG = True

    print(" ".join(word))

    if "_" not in word:
        print("Congratulations! You win.")
        EOG = True

    print(stages[lives])
