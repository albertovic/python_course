"""

- If the dealer ends with a total less than 17, they need to pick another card
- Infinite card deck.
- No jokers.
- The figures all count as 10.
- The Ace can count as 11 or 1.
- The cards in the list have equal probability of being drawn.

"""
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Quiero hacer que si es más de 20 la suma el as sea 1 e vez de 11
def add_card(list):
    new_card = random.randint(0,12)
    if new_card != 0:
        list.append(cards[new_card])
    elif sum(list) > 20:
        list.append(1)
    else:
        list.append(cards[new_card])

def compare_hands(player_list, computer_list):
    
    player_total = sum(player_list)
    computer_total = sum(computer_list)

    print(f"\n    Your final hand: {player_list}, final score: {player_total}")
    print(f"    Computer's final hand: {computer_list}, final score: {computer_total}\n")

    if player_total > 21:
        return -1
    elif computer_total > 21:
        return 1
    elif player_total > computer_total:
        return 1
    elif player_total == computer_total:
        return 0
    else:
        return -1


keep_playing = True

while keep_playing:
    player_hand = random.choices(cards, k = 2)
    computer_hand = random.choices(cards, k = 2)

    print(f"\n    Your cards: {player_hand}, current score: {sum(player_hand)}\n")
    print(f"    Computer's first card: {computer_hand[0]}\n")

    while sum(computer_hand) < 17:
        add_card(computer_hand)

    if sum(player_hand) < 21:
        other_card_flag = True
        other_card = input("Type 'y' to get another card, or 'n' to pass: ").lower()
    else:
        other_card_flag = False

    while other_card_flag:
        if other_card == 'y':
            add_card(player_hand)
            player_total = sum(player_hand)
            print(f"\n    Your cards: {player_hand}, current score: {player_total}")
            print(f"    Computer's first card: {computer_hand[0]}\n")
            if player_total < 21:
                other_card = input("Type 'y' to get another card, or 'n' to pass: ").lower()
            else:
                other_card_flag = False                
        elif other_card == 'n':
            other_card_flag = False
        #clear()
    
    comparison = compare_hands(player_list=player_hand, computer_list=computer_hand)

    if comparison == 0:
        print("It's a draw!")
    elif comparison == -1:
        print("The computer won. You lose :(")
    elif comparison == 1:
        print("You won. Congratulations :D")

    response = input("\nDo you want to continue playing? Type 'y' or 'n': ").lower()
    if response == "n":
        keep_playing = False


        

