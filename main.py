from replit import clear
from art import logo

print(logo)
bids = {}
is_finish = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if highest_bid < bid_amount:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of $ {highest_bid}")


while not is_finish:
    name = input("What is your name?")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    finish = input("Is there any one t attempt or not?").lower()
    if finish == "no":
        is_finish = True
        highest_bidder(bids)
    elif finish == "yes":
        clear()
