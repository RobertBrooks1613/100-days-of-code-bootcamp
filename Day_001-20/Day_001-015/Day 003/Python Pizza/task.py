print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
small = 15
medium = 20
large = 25
pepperoni_small = 2
pepperoni_medium_or_large = 3
extra_cheese_topping = 1
bill = 0

if size == "S" or size == "s":
    bill = small
    if pepperoni == "Y" or pepperoni == "y":
        bill += pepperoni_small
if size == "M" or size == "m":
    bill = medium
    if pepperoni == "Y" or pepperoni == "y":
        bill += pepperoni_medium_or_large
if size == "L" or size == "l":
    bill = large
    if pepperoni == "Y" or pepperoni == "y":
        bill += pepperoni_medium_or_large
if extra_cheese == "Y" or extra_cheese == "y":
    bill += extra_cheese_topping
else:
    print("Invalid input. Please try again.")
    exit()
print(f"Your final bill is: ${bill}.")