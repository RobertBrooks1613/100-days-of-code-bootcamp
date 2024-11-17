import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
rps_list = [rock, paper, scissors]
scissors_int = 2
paper_int = 1
rock_int = 0

play_again = True

while play_again:
    choose = int(input("Lets play rock paper scissors!! 0 = rock 1 = paper 2 = scissors\nEnter your choose : "))
    rng_rps = random.randint(0, 2)
    if choose >= 3 or choose < 0:
        print("not a valid option")

    elif choose == scissors_int and rng_rps == rock_int:
        print("Player loses!\n" + rps_list[choose] + "\nNPC picked\n" + rps_list[rng_rps])

    elif choose == rock_int and rng_rps == scissors_int:
        print("Player wins!\n" + rps_list[choose] + "\nNPC picked\n" + rps_list[rng_rps])

    elif choose < rng_rps:
        print("Player loses!\n" + rps_list[choose] + "\nNPC picked\n" + rps_list[rng_rps])

    elif choose > rng_rps:
        print("Player wins!\n" + rps_list[choose] + "\nNPC picked\n" + rps_list[rng_rps])

    elif choose == rng_rps:
        print("ITS A DRAW!\n" + rps_list[choose] + "\nNPC picked\n" + rps_list[rng_rps])
    else:
        print("not listed!\n" + rps_list[choose] + "\nNPC picked\n" + rps_list[rng_rps])

    yes_or_no = input("Play again?\nyes or no : ")
    if yes_or_no == "yes":
        play_again = True
    else:
        yes_or_no = False
        exit()