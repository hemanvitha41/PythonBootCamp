from art import logo
import random

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def blackJack():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = [random.choice(cards),random.choice(cards)]
    computer_cards = [random.choice(cards)]
    print(f"Your cards:{user_cards}, current score = {sum(user_cards)}")
    print(f"Computer's first cards: {computer_cards}")

    #User's Turn
    while True:

        choice = input("Type 'y' to get another card, type 'n' to pass: ")

        if choice == "y":
            user_cards.append(random.choice(cards))
            current_score = calculate_score(user_cards)
            print(f"Your cards:{user_cards}, current score = {sum(user_cards)}")
            print(f"Computer's first card:{computer_cards}")

            if current_score > 21:
                print("Busted!, You lose")
                print(f"Your final hand: {user_cards} Your final score: {current_score}")
                print(f"Computer final hand: {computer_cards} Computer final score: {sum(computer_cards)}")
                return


        elif choice == "n":
            break
        else:
            print("Invalid input")

    #Computer's turn
    while sum(computer_cards) < 17:
            computer_cards.append(random.choice(cards))

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards} Your final score: {user_score}")
    print(f"Computer final hand: {computer_cards} Computer final score: {computer_score}")

    #To determine the Winner
    if computer_score > 21:
               print("Computer went over 21!, You win")
    elif user_score > computer_score and user_score < 21:
        print("You win!")
    elif computer_score > user_score and computer_score < 21:
        print("Computer Wins!")
    else:
        print("It's a draw!")


# Main game loop
while True:
    choice = input("Do you want to play Blackjack? Type 'yes' or 'no' ")
    if choice.lower() == "yes":
        blackJack()
    elif choice.lower() == "no":
        print("\n"*100)
        break
    else:
        print("Enter Valid Input")
