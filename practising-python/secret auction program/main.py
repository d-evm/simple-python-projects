import os

bids = {}
another_bidder = True

while another_bidder:
    os.system('cls')

    name = input("Enter the name of the bidder: ")
    bid = int(input("Enter the bid amount: $"))

    bids[name] = bid

    next_bid = input("Is there any other bidder? (yes/no): ").lower()

    if next_bid == "no":
        another_bidder = False

os.system('cls')
max_value = max(bids.values())
highest_bidder = next(key for key, value in bids.items() if value == max_value)

print(f"{highest_bidder} placed the highest bid of ${max_value}.")
