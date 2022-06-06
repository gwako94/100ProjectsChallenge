import os
from art import logo


print(logo)

clear = lambda:os.system('clear')
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ''
  for bidder in bidding_record:
    bid_amount = int(bidding_record[bidder])
    if bid_amount > highest_bid:
      highest_bid = int(bidding_record[bidder])
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
  name = input("What's your name?:  ")
  bid = input("What's is your bid?: $")
  bidders = input("Are there any other bidders, type 'yes' or 'no'.\n")

  bids[name] = bid
  
  if bidders == "no":
    bidding_finished = True
    find_highest_bidder(bids)
  elif bidders == "yes":
    clear()
