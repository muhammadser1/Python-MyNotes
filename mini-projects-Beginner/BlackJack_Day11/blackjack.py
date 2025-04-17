import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]


def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)


def calculate_score(hand):
    """Returns the total score of the hand, handling Aces as 1 or 11."""
    score = sum(hand)
    while 11 in hand and score > 21:
        hand[hand.index(11)] = 1
        score = sum(hand)
    return score


def display_hand(player, hand, score, show_all=True):
    """Prints the player's or computer's hand and score."""
    if player == "Computer" and not show_all:
        print(f"Computer's first card: {hand[0]}")
    else:
        print(f"{player}'s hand: {hand}, score: {score}")


def compare_scores(user_score, computer_score):
    """Compares final scores and prints the game result."""
    print("\n--- Result ---")
    if user_score > 21:
        print("You went over. You lose")
    elif computer_score > 21:
        print("Computer went over. You win")
    elif user_score > computer_score:
        print("You win")
    elif user_score < computer_score:
        print("You lose")
    else:
        print("It's a draw")


def play_round():
    """Plays one round of Blackjack."""
    user_hand = [deal_card(), deal_card()]
    computer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_hand)
        display_hand("Your", user_hand, user_score)
        display_hand("Computer", computer_hand, score=0, show_all=False)

        if user_score > 21:
            game_over = True
            break

        should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if should_continue == 'y':
            user_hand.append(deal_card())
        else:
            game_over = True

    computer_score = calculate_score(computer_hand)
    while computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calculate_score(computer_hand)

    display_hand("Your", user_hand, calculate_score(user_hand))
    display_hand("Computer", computer_hand, computer_score)
    compare_scores(calculate_score(user_hand), computer_score)


def blackjack():
    """Main game loop."""
    while True:
        play = input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play == 'y':
            play_round()
        else:
            print("Goodbye!")
            break


blackjack()
