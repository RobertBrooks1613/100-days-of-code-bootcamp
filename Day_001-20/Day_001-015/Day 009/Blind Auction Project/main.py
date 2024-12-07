import art
def clear_console():
    print("\n" * 100)
asking_bidders = True
# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
dict_of_bidders = {}
# TODO-3: Whether if new bids need to be added
def check_for_highest_bid():
    last_bid = 0
    bidders_name = ''
    for bidders in dict_of_bidders:
        if int(dict_of_bidders[bidders]) > last_bid:
            last_bid = int(dict_of_bidders[bidders])
            bidders_name = bidders
    return bidders_name, last_bid
# TODO-4: Compare bids in dictionary

while asking_bidders:
    print(art.logo + '\n' * 5)
    user_name = input("Whats your name?\n")
    user_bid_amount = int(input("How Much are you Bidding?\n$"))
    dict_of_bidders[user_name] = user_bid_amount
    if input("Any other bids? yes or no : ").lower() != "yes":
        asking_bidders = False
    clear_console()


print(art.logo + '\n' * 5)
winning_bidder, winning_bid = check_for_highest_bid()

print(f"The winner is! {winning_bidder} \nWith a bid amount of :${winning_bid}")
exit()