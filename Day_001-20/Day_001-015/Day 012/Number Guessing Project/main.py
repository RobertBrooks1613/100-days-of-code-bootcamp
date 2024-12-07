from art import logo
from art import you_win
from art import you_lose
import random
import os

EASY = 11
NORMAL = 7
HARD = 5

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

playing_game = True
MATCH_FOUND = False
GAME_OVER = False

def guesses_to_check(attempts_allowed):
    global MATCH_FOUND
    global GAME_OVER

    while not MATCH_FOUND:
        guess = int(input("Guess a number 1 - 100\n"))
        if guess == int:
            print("Invalid option. Numbers only")
            break
        else:
            if number_to_guess > guess:
                print("To low")
            elif number_to_guess < guess:
                print("To high")
            elif number_to_guess == guess:
                print("Match!!")
                MATCH_FOUND = True
                break
        attempts_allowed -= 1
        if attempts_allowed == 0:
            GAME_OVER = True
            break
        print(f"Attempts left : {attempts_allowed}")

def set_attempts(dif_level):
    if dif_level == "easy":
        return EASY
    elif dif_level == "normal":
        return NORMAL
    elif dif_level == "hard":
        return HARD
    else:
        return 0


while playing_game:
    print(logo)
    print("Welcome to the Number guessing game!!")
    number_to_guess = random.randint(1,100)
    difficulty_level = input("What difficulty Level would you like?\neasy : 11 attempts \nnormal : 7 attempts \nhard : 5 attempts\n-> ").lower()
    attempts = set_attempts(difficulty_level)
    if attempts == 0:
        print("Invalid option")
        break

    if attempts != 0:
        print(f"You have {attempts} attempts!\nGood Luck!")
        while not MATCH_FOUND and not GAME_OVER:
            guesses_to_check(attempts)
    if MATCH_FOUND:
        print(you_win)
    else:
        print(you_lose)

    yes_or_no = input("\nPlay again? yes or no : ").lower()
    if yes_or_no == "yes":
        playing_game = True
        MATCH_FOUND = False
        GAME_OVER = False
        clear_console()
    else:
        playing_game = False
        exit()