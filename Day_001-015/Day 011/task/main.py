import random
import art
import os

def clear_console():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux (os.name is 'posix')
    else:
        os.system('clear')
logo = art.logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playing_game = True
game_started = True
player_hand = []
npc_hand = []
npc_chooses = ["hit", "hold"]
GAME_OVER = False

def deal_card():
    random_card = random.choice(cards)
    return random_card


def userinput_yes_or_no(yes_or_no):
    yes_or_no.lower()
    if yes_or_no == "yes":
        return True
    else:
        return False

def card_counter(card_input):
    if sum(card_input) == 21 and len(card_input) == 2:
        return "Black Jack"
    if sum(card_input) > 21 and 11 in card_input:
        card_input.remove(11)
        card_input.append(1)
        return sum(card_input)
    elif sum(card_input) <= 21:
        return sum(card_input)
    else:
        card_input = [0]
        return sum(card_input)


while playing_game:
    if game_started and not GAME_OVER:
        print(f"{logo}")
        player_hand += deal_card(), deal_card()
        npc_hand += deal_card(), deal_card()
        game_started = False
        if card_counter(player_hand) == "Black Jack" or card_counter(npc_hand) == "Black Jack":
            GAME_OVER = True
    if not GAME_OVER:
        print(f"\nplayer: {player_hand} computer: [?]{npc_hand[1:]}")
        player_input = input("Hit or hold? : ").lower()
        if player_input == "hit" and not GAME_OVER:
            player_hand.append(deal_card())
            if card_counter(player_hand) == 0:
                GAME_OVER = True

        if card_counter(npc_hand) >= 17 :
            if card_counter(npc_hand) >= 19:
                npc_choose = "hold"
            else:
                npc_choose = random.choice(npc_chooses)
        else:
            npc_choose = "hit"

        if npc_choose == "hit" and not GAME_OVER:
            npc_hand.append(deal_card())
            if card_counter(npc_hand) == 0:
                GAME_OVER = True

        if card_counter(player_hand) == 0 or card_counter(npc_hand) == 0:
            GAME_OVER = True

        if player_input != "hit" and npc_choose != "hit":
            GAME_OVER = True

    if GAME_OVER:
        if card_counter(player_hand) == "Black Jack" or card_counter(npc_hand) == "Black Jack":
            print(art.black_jack + '\n')
            if card_counter(player_hand) == "Black Jack":
                print(f"\nPlayer Won!\nPlayer's Hand {player_hand} : {card_counter(player_hand)}" )
            if card_counter(npc_hand) == "Black Jack":
                print(f"\nComputer Won!\nComputer's Hand {npc_hand} : {card_counter(npc_hand)}" )

        elif card_counter(player_hand) > card_counter(npc_hand):
            print(f"\nPlayer Wins!\nPlayer's hand was: {player_hand} : {sum(player_hand)}\nComputer's hand was: {npc_hand} : {sum(npc_hand)}")
        elif card_counter(npc_hand) > card_counter(player_hand):
            print(f"\nPlayer Loses!\nPlayer's hand was: {player_hand} : {sum(player_hand)}\nComputer's hand was: {npc_hand} : {sum(npc_hand)}")
        elif card_counter(npc_hand) == card_counter(player_hand):
            print(f"\nDraw!!\nPlayer's hand was: {player_hand} : {sum(player_hand)}\nComputer's hand was: {npc_hand} : {sum(npc_hand)}")

        playing_game = userinput_yes_or_no(input("\nKeep playing? yes or no: " + '\n'))
        player_hand = []
        npc_hand = []
        GAME_OVER = False
        game_started = True
        clear_console()
