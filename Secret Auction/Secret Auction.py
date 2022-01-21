from replit import clear
bids = {}
keep_going = False

def no_name(bidding_record):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_record:
      current_bid = bidding_record[bidder]
      if current_bid > highest_bidder:
        highest_bidder = current_bid
        winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")


while not keep_going:
    name = input("What is your name?\n")
    price = int(input("What is your bid price? $\n"))
    bids[name] = price
    more_bids = input("Are there more bidders? please select 'yes' or 'no'.\n")
    if more_bids == "no":
        keep_going = True
        clear()
        no_name(bids)
    elif more_bids == "yes":
        clear()
    else:
        print('You have inputted an invalid selection, try again')
        keep_going = True