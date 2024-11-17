# import re
#
# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(re.sub(r'\D', '', input("What percentage tip would you like to give? 10 12 15 "))) / 100 + 1  # Divide by 100 to get the percentage and add 1 to get the total
# people = int(input("How many people to split the bill? "))
#
# # round() function is used to round the value to 2 decimal places
# # IF after the math you add , 2 <- this is the number of decimal places
# print(f"Each person should pay: ${round(bill * tip / people , 2)} \n Total bill: ${round(bill * tip, 2)}")

def get_numeric_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Invalid input. Please enter numbers only.")

# Example usage
percentage = get_numeric_input("What percentage tip would you like to give? ")
print(f"You entered: {percentage}%")