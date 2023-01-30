# Blackjack
# For "infinite" deck as per instructions, set n_of_decks to 0.
# Deck is dynamic meaning it loses cards (as long as n_of_decks > 0)
# as you continue to play. If there are insufficient cards on draw,
# reshuffle (repopulate deck by creating same number of decks).
import random
from art import logo

print(logo)

# Create sets of decks. In the form of:
# [boolean, [deck_1], ..,[deck_n]]
# Boolean is True if infinite deck. Only true at n_decks == 0.
def create_deck(n_decks: int):
    """Creates n_decks number of decks. If n_decks = 0, create 1 infinite deck"""
    sets_deck = []

    # If user chooses 0, create an "infinite" deck. Denoted by True in sets_deck[0].
    if not n_decks:
        sets_deck.append(True)
        sets_deck.append([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4)
    # If user chooses n > 0, create a n number of decks.
    else:
        sets_deck.append(False)
        for _ in range(n_decks):
            sets_deck.append([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] * 4)
            # sets_deck.append([1, 2])

    return sets_deck


# Draw n cards.
def draw_cards(n: int, decks: list):
    """Returns a list of n cards, and remaining of the deck inputted."""
    drawed_cards = []
    n_decks = len(decks) - 1

    is_deck_infinite = None
    if decks[0] == True:
        is_deck_infinite = True
    else:
        is_deck_infinite = False

    # Draw n cards and remove from deck.
    for _ in range(n):
        # Select random index for choosing deck.
        # Starts at 1 since 0 is for determining deck is finite or not.
        random_deck_index = random.randint(1, n_decks)
        selected_deck = decks[random_deck_index]

        deck_size = len(selected_deck) - 1

        # Randomly select a deck from currently available decks.
        random_card_index = random.randint(0, deck_size)

        if is_deck_infinite:
            selected_card = random.sample(selected_deck, 1)[0]
        else:
            selected_card = selected_deck.pop(random_card_index)
            deck_size -= 1

        # Remove empty decks.
        if decks[random_deck_index] == []:  # Dont use deck == False to check for
            decks.pop(random_deck_index)  # empty lists since index 0 is a boolean.
            n_decks -= 1  # Update number of decks

        drawed_cards.append(selected_card)

    return drawed_cards, decks


# Sum of hand (blackjack)
def hand_score(hand: list):

    hand_sum = sum(hand)

    # Note that 11 can either be 1 or 11.
    for _ in range(hand.count(11)):
        if hand_sum > 21 and 11 in hand:
            for i, _ in enumerate(hand):
                if hand[i] == 11:
                    hand[i] = 1
                    break
            hand_sum = sum(hand)

    return sum(hand)


continue_playing = True

# Create a deck and deal
n_of_decks = 8
decks = create_deck(n_of_decks)
player_cards = []
dealer_cards = []

intro_once = True

while continue_playing:
    # Start with new hand.
    player_cards = []
    dealer_cards = []

    user_continue_choice = ""
    # Message at start.
    if intro_once:
        while user_continue_choice not in ["y", "n"]:
            user_continue_choice = input(
                "Welcome to Las Dolina! \
Do you want to play Black Jack? (y / n): "
            ).lower()
        intro_once = False

    # Message after 1st run.
    else:
        while user_continue_choice not in ["y", "n"]:
            user_continue_choice = input("Do you want to play again? (y / n): ").lower()

    if user_continue_choice == "n":
        break

    # Simulate 1 by 1 dealing (might be useful for future console display)
    for _ in range(2):
        try:
            drawed_card, decks = draw_cards(1, decks)
        except:  # Repopulate decks
            decks = create_deck(n_of_decks)
            drawed_card, decks = draw_cards(1, decks)
        player_cards.append(drawed_card[0])

        try:
            drawed_card, decks = draw_cards(1, decks)
        except:  # Repopulate decks
            decks = create_deck(n_of_decks)
            drawed_card, decks = draw_cards(1, decks)
        dealer_cards.append(drawed_card[0])

    user_draw_choice = "y"
    while user_draw_choice == "y":
        user_draw_choice = ""

        # Show player and dealer's card.
        player_score = hand_score(player_cards)

        # End draw cycle
        if player_score > 21 or player_score == 21:
            break

        print(f"You have: {player_cards}. Score: {player_score}.")
        print(f"Dealer has [{dealer_cards[0]}], Score: {dealer_cards[0]}.")

        while user_draw_choice not in ["y", "n"]:
            user_draw_choice = input("Draw a card? (y / n): ").lower()
            print("")

        if user_draw_choice == "y":
            try:
                drawed_card, decks = draw_cards(1, decks)
            except:
                decks = create_deck(n_of_decks)
                drawed_card, decks = draw_cards(1, decks)
            player_cards.append(drawed_card[0])

        else:
            dealer_score = hand_score(dealer_cards)

            while dealer_score < 17:
                try:
                    drawed_card, decks = draw_cards(1, decks)
                except:  # Repopulate decks
                    decks = create_deck(n_of_decks)
                    drawed_card, decks = draw_cards(1, decks)
                dealer_cards.append(drawed_card[0])
                dealer_score = hand_score(dealer_cards)

    dealer_score = hand_score(dealer_cards)
    player_score = hand_score(player_cards)

    print(f"You have: {player_cards}. Score: {player_score}.")
    print(f"Dealer has: {dealer_cards}, Score: {dealer_score}.")

    # Scoring logic
    if player_score == dealer_score and player_score < 22:
        print("It's a draw!")

    elif (player_score > dealer_score and player_score <= 21) or dealer_score > 21:
        if player_score == 21:
            print("BLACKJACK! You win!")
        else:
            print("You win!")

    else:
        if dealer_score == 21:
            print("Dealar BLACKJACK!")
        else:
            print("You lose")

    print("")
