# Secret Bidder

from os import system
from auction_ascii import auction
print(auction)

print("Welcome to the secret auction program.")
bidder_dict = {}

def bidder_max(bidders_details):
    max_bid = 0
    max_bidder = ''
    for bidder in bidders_details:
        amount = bidders_details[bidder]
        if amount > max_bid:
            max_bid = amount
            max_bidder = bidder
    print(f"The winner of the bidder is {max_bidder} with bid of ${max_bid}")


while True:
    name = input("What is your name: ").capitalize()
    bid = int(input("What's your biding amount: $"))
    bidder_dict[name] = bid

    again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if again == "no":
        bidder_max(bidder_dict)
        break
    else:
        # Clear screen in terminal
        system('cls')
        print("Pass the system to other bidder")

