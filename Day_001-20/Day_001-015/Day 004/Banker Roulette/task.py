import random

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
playing_lunch_roulette = True

rolling = input("Welcome to Who's Bill is it Today! \nType roll : ")

while playing_lunch_roulette:
    rng_number = random.randint(0, (len(friends) - 1))
    rng_friend = friends[rng_number]
    bill_total = random.uniform(10, 500)

    if rolling.lower() == "roll":
        print("Looks like its! : " + rng_friend + "\n"
        "Your the lucky winner that has to pay the bill of : $" + str(round(bill_total, 2)))
    else:
        print("Invalid option!")
    choose = input("Would you like to roll again? \nyes or no : ")
    if not choose.lower() == "yes":
        playing_lunch_roulette = False