#!/usr/bin/env python3

##========================================================================================##
## Day12: Python Dictionary: This script is to test out a secret auction game, where
## users can enter their name and a bid amount and the highest bidder is selected at the
## end. 
## I have tried to use Python dictionary and list as value for dictionary-key.
##=========================================================================================##
import os

print(f'Welcome to the secret aution program using Python dictionary !!')

bidders = {}
is_another_customer_in_queue = True
queue = 1

while (is_another_customer_in_queue == True):
    current_bidder = []
    bidder_name = input(f"What is your name? ")
    current_bidder.append(bidder_name)
    bid_amount = float(input(f'What is your bid? $'))
    current_bidder.append(bid_amount)
    # print(f'Current bidder: {current_bidder}')
    current_bidder_seq = "bidder"+str(queue)
    bidders[current_bidder_seq] = current_bidder
    next_bidder = input(f"Are there any other bidders? Type 'yes' or 'no': ")
    if next_bidder == "yes":
        queue += 1
        os.system('clear')
    elif next_bidder == "no":
        is_another_customer_in_queue = False


# print(f'{bidders}')

## Check who has made the highest bid

highest_bid = 0

for bid_amt in bidders:
    if(bidders[bid_amt][1] > highest_bid):
        highest_bid = bidders[bid_amt][1]
        higest_bidder = bidders[bid_amt][0]
    

os.system('clear')
print(f'The winner is {bidders[bid_amt][0]} with a bid of ${bidders[bid_amt][1]}')