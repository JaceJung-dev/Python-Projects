from art import logo

print(logo)

again = True
bids = {}


def find_highest_bidder(bidder_dict):
    winner = ""
    highest_bid = 0
    for key in bidder_dict:
        if bidder_dict[key] > highest_bid:
            highest_bid = bidder_dict[key]
            winner = key
        elif bidder_dict[key] == highest_bid:
            winner += f", {key}"

    print(f"The winner is {winner} with a bid of ${highest_bid}")


while again:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bids[name] = bid

    again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if again == "yes":
        print("\n" * 30)
    else:
        find_highest_bidder(bids)
        again = False
