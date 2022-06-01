import random
from art import logo

print(logo)

cards_list = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
boo_choice = [True, False]


def player(x1, x2, comp=False):
    if x1 == 11 and x1 + x2 > 21:
        x1 = 1
    elif x2 == 11 and x1 + x2 > 21:
        x2 = 1
    in_hands = [x1, x2]
    if comp:
        print(f"Computer's cards are {x1} and X")
    else:
        print(f"Your cards are {x1} and {x2}")

    sum_of_cards = sum(in_hands)
    return sum_of_cards


def game(player1, player2):
    question = input("Do you want to open (o) your cards or take another(t): ").lower()
    if question == "o":
        print(f"Computer's cards sum was {player2}")
        if player1 > 21:
            return False
        elif player1 > player2:
            comp_choose = random.choice(boo_choice)
            if comp_choose:
                new_card = random.choice(cards_list)
                player2 += new_card
                print(f"New computer's cards sum wis {player2}")
                if 22 > player2 > player1:
                    return False
                elif 22 > player1 > player2:
                    return True
            else:
                return True

        elif player1 < player2 < 22:
            return False
        else:
            return True
    elif question == "t":
        new_card = random.choice(cards_list)
        print(f"The new card is {new_card}")
        player1 += new_card
        if player1 > 21:
            return False
        print(f"Computer's cards sum was {player2}")
        comp_choose = random.choice(boo_choice)
        if comp_choose:
            new_card = random.choice(cards_list)
            player2 += new_card
            print(f"New computer's cards sum wis {player2}")
            if 22 > player2 > player1:
                return False
            elif 22 > player1 > player2:
                return True
        else:
            return True


running = True

while running:
    print("\n")
    card1 = random.choice(cards_list)
    card2 = random.choice(cards_list)
    card3 = random.choice(cards_list)
    card4 = random.choice(cards_list)
    computer = True
    winning = game(player(card1, card2), player(card3, card4, comp=computer))
    if winning:
        print("You have won!")
    else:
        print("You have lost.")
    play_again = input("Do you want to continue? (y/n)").lower()
    if play_again == "y":
        running = True
    else:
        running = False

