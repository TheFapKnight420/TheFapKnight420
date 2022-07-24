import random

import art

cards = {"ace": 11,
         "two": 2,
         "three": 3,
         "four": 4,
         "five": 5,
         "six": 6,
         "seven": 7,
         "eight": 8,
         "nine": 9,
         "ten": 10,
         "prince": 10,
         "queen": 10,
         "king": 10
         }


def print_cards(player_hand, dealer_hand):
    score = 0
    dealer_score = 0
    game_score = []
    for card in player_hand:
        print(f"Your card: {card}")
        score += cards[card]
    print(f"Your current score is: {score}")
    game_score.append(score)
    print(f"Dealer faced up card : {dealer_hand[0]}")
    for card in dealer_hand:
        dealer_score += cards[card]
    game_score.append(dealer_score)

    return game_score


def game_round(money, current_bid):  # Code for the round stage of the game
    print("Well giving you two cards!")
    player_hand = []
    dealer_hand = []
    player_hand.append(random.choice(list(cards)))  # adds a random card from cards dictionary to the player
    player_hand.append(random.choice(list(cards)))
    dealer_hand.append(random.choice(list(cards)))  # adds a random card from cards dictionary to the dealer
    game_score = print_cards(player_hand, dealer_hand)  # returns the score of the player and the dealer in a list form
    total_player_cards = game_score[0]  # adds score from list to the player score variable
    total_dealer_cards = game_score[1]   # adds score from list to the dealer score variable
    while total_player_cards < 21 and True:  # A loop for the take or hold actions
        print(f"Player score: {total_player_cards}")
        choice = input("So partner you wanna hold or take a card (h/t)?\n")
        if choice == "t":
            player_hand.append(random.choice(list(cards)))
            game_score = print_cards(player_hand, dealer_hand)
            total_player_cards = game_score[0]
            total_dealer_cards = game_score[1]
        else:
            break
    ace_dealt_with = False
    while total_dealer_cards < 17 and total_dealer_cards < 21:  # handles whether dealer has less than 17 score
        card = (random.choice(list(cards)))
        dealer_hand.append(card)
        total_dealer_cards += cards[card]
        if "ace" in dealer_hand and total_dealer_cards > 21 and ace_dealt_with is not False:  # checks if dealer has ace
            total_dealer_cards -= 10
            ace_dealt_with = True

    lost = False
    draw = False

    #  all of this section is to check if the player managed to draw win or lose

    if total_player_cards > 21:
        if "ace" in player_hand:
            total_player_cards -= 10
    if total_player_cards > 21 and total_dealer_cards <= 21:
        print(f"Bust! your hand value is {total_player_cards}")
        lost = True
    elif total_dealer_cards > 21 and total_player_cards > 21:
        draw = True
    elif total_dealer_cards > 21:
        print(f"You won the dealer had a hand of {total_dealer_cards} which is more than 21")
        lost = False
    elif total_dealer_cards == total_player_cards:
        draw = True
    elif total_dealer_cards < total_player_cards:
        lost = False
    elif total_dealer_cards > total_player_cards:
        lost = True

    # all of this section is to act according to the player loss/win/draw

    if draw:
        print(f"Well it's a draw partner you have {total_player_cards} and I have {total_dealer_cards}")
        print("Your hand:")
        for card in player_hand:
            print(card)
        print("Dealer's hand:")
        for card in dealer_hand:
            print(card)
        print("You don't loose money")
        return money
    elif lost:
        print(f"You lost you have {total_player_cards} and I have got {total_dealer_cards}")
        print("Your hand:")
        for card in player_hand:
            print(card)
        print("Dealer's hand:")
        for card in dealer_hand:
            print(card)
        print(f"You lost {current_bid}$")
        return money - current_bid
    elif not lost:
        print(f"You won! You have {total_player_cards} and I have got {total_dealer_cards}")
        print("Your hand:")
        for card in player_hand:
            print(card)
        print("Dealer's hand:")
        for card in dealer_hand:
            print(card)
        print(f"You won {current_bid}$")
        return money + current_bid


current_money = 500


def black_jack():  # the main interface
    global current_money
    while current_money > 0 and True:
        print(f"You have {current_money}$ in your pockets")
        choice = input("Hi player ready to deal? (y/n)\n").lower()
        if choice == "n":
            print("Shame to see you go!\n" +
                  f"You went out with {current_money}$ in your pocket")
            break
        else:
            bid = int(input("Well well, How much you want to bid partner?\n"))
            if bid > current_money:
                print("Hold on partner you don't have enough look somewhere else!")
                print("Looking for another dealer after getting yelled at...")
                black_jack()
                break
            else:
                current_money = game_round(current_money, bid)


print(art.logo)
black_jack()
print(f"You have {current_money}$ go home partner and see you tomorrow!")

# print(random.choice(list(cards)))
