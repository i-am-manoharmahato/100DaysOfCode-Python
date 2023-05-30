#!/usr/bin/env python3

from art import logo 
import time
import random

print(logo)
print(f'Welcome to the blackjack game !!')


def shuffle_card(deck, cards_to_pick):
    selected_cards = random.choices(deck, k=cards_to_pick)
    return selected_cards



start = input('\nShall we start? y/n: ')

if start == "y":
    print(f'\nShuffling cards ......')
    time.sleep(1)
else:
    print(f'\nGood bye !!\n')
    exit(0)



cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
result = ""

player_cards = shuffle_card(cards, 2)

dealer_cards = shuffle_card(cards, 2)

print(f'\n>>> Player cards: {player_cards[0]}  {player_cards[1]}')
print(f'\n### Dealers card: X  {dealer_cards[0]}\n')

player_total = player_cards[0] + player_cards[1]
dealer_total = dealer_cards[0] + dealer_cards[1] 

player_won = False
dealer_won = False

proceed = input(">>> Player choice: Hit (h) or Stand(s): ")

## Check if the player won in the very first deal.

if (int(player_total)==21):
     player_won = True

## If the player's total is less than 21 but he/she still wants to HIT

while ((int(player_total) < 21) and (proceed != 's')):
        # proceed = input("\nPlayer choice: Hit (h) or Stand(s): ")
        temp_card = shuffle_card(cards, 1)
        player_cards.append(temp_card[0])
        print(f'\n>>> New card to the player: {temp_card[0]}')
        print(f'\n>>> Player cards: ')
        for card in player_cards:
            print(card, end="  ")
        player_total = int(player_total + int(temp_card[0]))
        print(f'\n>>> Player total: {player_total}')
        if int(player_total) > 21:
             dealer_won = True
             break
        else:
             proceed = input("\n>>> Player choice: Hit (h) or Stand(s): ")

if (int(player_total)==21):
     player_won = True

## If the player's total is less than 21 and he/she Stands

if ((int(player_total) < 21) and (proceed == 's')):
    print(f'\n*** Player has choosen to Stand. Over to the dealer now. ***')
    time.sleep(1)
    print(f'\n### Dealer cards: ')
    for card in dealer_cards:
        print(card, end="  ")

    ## Check if the dealer has already won at this stage.
    if (int(dealer_total) == 21):
            dealer_won = True
    

    while (int(dealer_total) <= 16):
        temp_card = shuffle_card(cards, 1)
        dealer_cards.append(temp_card[0])
        print(f'\n### New card to the dealer: {temp_card[0]}')
        print(f'\n### Dealer cards: ')
        for card in dealer_cards:
            print(card, end="  ")
        dealer_total = int(dealer_total + int(temp_card[0]))
        print(f'\n### Dealer total: {dealer_total}')
    
    if (int(dealer_total) > 16 and int(dealer_total) < 21):
         dealer_gap = 21 - int(dealer_total)
         player_gap = 21 - int(player_total)
         if (int(dealer_gap) < int(player_gap)):
              dealer_won = True
         else:
             player_won = True

    elif (int(dealer_total) > 21):
        player_won = True


## Check if the total score of both the players is same.

if (int(player_total) == int(dealer_total)):
     result = "Tie"



## At this point, check if the dealer has not dealt at all. And still sitting with the initial 2 cards.
dealer_cards_size = len(dealer_cards)
     

## Final check: Who has won based on the flags above:
print(f'\n\n**======================================**')

if (result == "Tie"):
    print(f'>>> Player total: {player_total}')
    print(f'### Dealer total: {dealer_total}')
    print(f'\n===> ITS A TIE <===')

elif (int(player_total > 21) and (dealer_won == True) and int(dealer_cards_size == 2)):
    print(f'>>> Player total: {player_total}')
    print(f'### Dealer cards: X {dealer_cards[0]}')
    print(f'\nYou lost .. Dealer won !!')

elif (int(player_total > 21) or (dealer_won == True)):
    print(f'>>> Player total: {player_total}')
    print(f'### Dealer total: {dealer_total}')
    print(f'\nYou lost .. Dealer won !!')

if (player_won == True):
    print(f'>>> Player total: {player_total}')
    print(f'### Dealer total: {dealer_total}')
    print(f'\n$$$ You won .. Congratulations !! $$$')

print(f'**======================================**\n')
