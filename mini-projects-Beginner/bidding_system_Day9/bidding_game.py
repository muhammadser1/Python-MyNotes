def find_max_bidder(bids_dict):
    max_bid = 0
    highest_bidder = ""
    for name, bid in bids_dict.items():
        if bid > max_bid:
            highest_bidder = name
            max_bid = bid
    return highest_bidder, max_bid


def bidding():
    continue_bidding = True
    bids = {}

    while continue_bidding:
        name = input("What is your name? ")
        bid = int(input("What is your bidding_system_Day9? $"))
        bids[name] = bid

        should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
        if should_continue == "no":
            continue_bidding = False

    winner_name, max_bid = find_max_bidder(bids)
    print(f"\nThe winner is {winner_name} with a bidding_system_Day9 of ${max_bid}!")


bidding()
