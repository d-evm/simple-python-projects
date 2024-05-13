import random
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
""")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = random.sample(cards, 2)
dealer_cards = random.sample(cards, 1)

print(f"\nYour hand: {player_cards}")
print(f"Dealer's first card: {dealer_cards}")

play = True

while play != False:
    dealer_sum = sum(dealer_cards)
    player_sum = sum(player_cards)

    print("\nYour score: ", player_sum)
    print("Dealer's score: ", dealer_sum)
    print()

    if sum(player_cards) == 21:

        print("Congrats! You won!")
        play = False

    elif sum(player_cards) > 21:

        print("Ohh you lose! Dealer wins.")
        play = False

    else:
        move = input(
            "Type 'y' to get another card(Hit), type 'n' to pass(Stand): ")
        new_cards = random.choice(cards)

        print()

        if move == "y":
            player_cards.append(new_cards)

            print(
                f"Your hand: {player_cards}")
            print(f"Dealer's hand: {dealer_cards}")

        else:
            while sum(dealer_cards) < 17:
                new_cards = random.choice(cards)
                dealer_cards.append(new_cards)
                print(
                    f"\nYour hand: {player_cards}")
                print(f"Dealer's hand: {dealer_cards}")

            dealer_sum = sum(dealer_cards)
            player_sum = sum(player_cards)

            print("Your score: ", player_sum)
            print("Dealer's score: ", dealer_sum, "\n")

            if dealer_sum == 21:
                print("Ohh you lose! Dealer wins.")
                play = False

            elif dealer_sum > 21:
                print("Congrats! You won!")
                play = False

            else:
                if dealer_sum == player_sum:
                    print("Ohh! You draw.")

                elif dealer_sum > player_sum:
                    print("Ohh you lose! Dealer wins.")

                else:
                    print("Congrats! You won!")

                play = False
