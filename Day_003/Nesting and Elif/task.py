print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
adultTicket = 12
childTicket = 5
teenTicket = 7
photoCost = 3
ticketCost = 0

if height >= 120:
    age = int(input("What is your age? "))
    print("You can ride the rollercoaster")
    if age <= 12:
        ticketCost = childTicket
        print(f"Child ticket cost ${ticketCost}.")
    elif age <= 18:
        ticketCost = teenTicket
        print(f"Teen Tickets cost ${ticketCost}.")
    else:
        ticketCost = adultTicket
        print(f"Adult Tickets cost ${ticketCost}.")

    option = str(input("Do you want a photo taken? yes or no: "))

    if option == "yes":
        ticketCost += photoCost

    print(f"Your total will be ${ticketCost}.")
else:
    print("Sorry you have to grow taller before you can ride.")


