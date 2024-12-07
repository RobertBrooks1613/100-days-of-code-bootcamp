import random

from game_data import data
import art
GAME_OVER = False
CHECKING = True


name = 'name'
followers = 'follower_count'
description = 'description'
country = 'country'
idles_already_picked = []

def format_data(data_to_format):
    """Takes in passed in data from the data list and returns the formated version"""
    account_name = data_to_format[name]
    account_descr = data_to_format[description]
    account_country = data_to_format[country]
    return f"{account_name}, A {account_descr}\nFrom {account_country}"

def check_for_repeats(name_input):
    """Checks for any repeats to make sure we don't get the same entry or repeats"""
    if name_input in idles_already_picked:
        return True
    else:
        idles_already_picked.append(name_input)

def random_idle_picker():
    """Returns a random Idle and will check to make sure it's not a repeat.
        As well as if it hit the end of the list."""
    while CHECKING:
        random_choice = random.choice(data)
        if not check_for_repeats(random_choice):
            return random_choice
        elif len(idles_already_picked) >= 50:
            print(f"Ran out of Idles to pick from")
            break

def who_has_more_followers(user_pick_a, user_pick_b):
    """Compares followers and Returns A or B as the higher value"""
    a_follower_count = int(user_pick_a[followers])
    b_follower_count = int(user_pick_b[followers])
    if a_follower_count > b_follower_count:
        return "a"
    else:
        return "b"


def game():
    game_score = 0
    global GAME_OVER
    while not GAME_OVER:
        ran_a = random_idle_picker()
        ran_b = random_idle_picker()
        print(f"A: {format_data(ran_a)} "
              f"{art.vs} \nB: "
              f"{format_data(ran_b)}\n")
        higher_followers_is = who_has_more_followers(ran_a, ran_b)
        while True:
            try:
                choice_a_or_b = input("Who do you think has more followers?\nA or B? : ").lower()
                if choice_a_or_b != "a" or choice_a_or_b != "b":
                    print("A or B only\n")
                if choice_a_or_b == "a" or choice_a_or_b == "b":
                    break
            except ValueError:
                print("Value Error was Thrown\n")

        if choice_a_or_b == higher_followers_is:
            game_score += 1
            print(f"{art.correct}\nYour Score is {game_score}\n")
            print(f"{ran_a[name]} has {ran_a[followers]} Million\n{ran_b[name]} has {ran_b[followers]} Million\n{art.line_line}")
        else:
            print(f"{art.incorrect}\n Your Final score is {game_score}\n")
            print(f"{ran_a[name]} has {ran_a[followers]} Million\n{ran_b[name]} has {ran_b[followers]} Million\n{art.line_line}")
            GAME_OVER = True


while True:
    print(art.logo)
    game()
    yes_or_no = input("Try again? \nyes or no? : ")
    if yes_or_no == "yes":
        GAME_OVER = False
    else:
        break
exit()
