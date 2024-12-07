import Check_Number_Rand

# userInput = input("Would you like me to give you a random number? yes or no\n").lower()
# max_number = int(input("What is the max number you want? : \n"))
# min_number = int(input("What is the minimum number you want? :\n"))
# keep_playing = True
#
# while userInput == "yes" and keep_playing:
#     number = Check_Number_Rand.get_number_int(min_number, max_number)
#     print(f"Your random number is! : {number}")
#     option = input("Would you like to roll again? \nyes or no : \n").lower()
#     if option == "yes":
#         keep_playing = True
#     else:
#         keep_playing = False
#     if not keep_playing:
#         exit()

playing_still = True

print("Lets Flip a coin!!")

while playing_still:
    choose = str(input("\nHeads or Tails?").lower())
    if choose == "heads" or choose == "tails":
        result = str(Check_Number_Rand.head_or_tails())
        print("coin landed : " + result)
        if choose == result.lower():
            print("You win!!")
        else:
            print("You Lose!")
    elif not choose == "heads" or "tails":
        print("invalid option\n")
    keep_playing = input("Play again?\n yes or no : ")
    if keep_playing == "yes":
        playing_still = True
    else:
        exit()
