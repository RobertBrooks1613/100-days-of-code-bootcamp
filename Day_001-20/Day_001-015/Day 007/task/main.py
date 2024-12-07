import random
import hangman_art
import hangman_words
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
stages = hangman_art.stages
lives = len(stages) - 1
max_lives = len(stages) - 1


# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

GAME_OVER = False
correct_letters = []
already_guessed = []

while not GAME_OVER:

    # TODO-6: - Update the code below to tell the user how many lives they have left.
    print(f"****************************{lives}/{max_lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in already_guessed:
        print("You Already guessed that letter..")
    if len(guess) > 1:
        print("To many letters. Please only guess 1 letter")
    else:
        if guess not in already_guessed:
            already_guessed.append(guess)
            display = ""

            for letter in chosen_word:
                if letter == guess:
                    display += letter
                    correct_letters.append(guess)
                elif letter in correct_letters:
                    display += letter
                else:
                    display += "_"

            print("Word to guess: " + display)

            # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
            #  e.g. You guessed d, that's not in the word. You lose a life.

            if guess not in chosen_word:
                lives -= 1

                if lives == 0:
                    GAME_OVER = True

                    # TODO 7: - Update the print statement below to give the user the correct word they were trying to guess.
                    print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

            if "_" not in display:
                GAME_OVER = True
                print("****************************YOU WIN****************************")

            # TODO-2: - Update the code below to use the stages List from the file hangman_art.py
            print(stages[lives])
