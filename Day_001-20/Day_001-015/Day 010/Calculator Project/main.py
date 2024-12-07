import art
calc_logo = art.logo
running = True
loop_count = 0

print(calc_logo)
while running:
    user_input = input(f'Write out a math problem\n'
                       f'use numbers only and these symbols.\n'
                       f'[ * multiplication ],[ / division, + addition],[ - subtraction],[ % modulo],[ () parentheses]\n'
                       f' ')
    problem = eval(user_input)
    print(f"{user_input} = {problem:,}")
    yes_or_no = input("Would you like to run another calculation?\nType yes or no : ").lower()
    if yes_or_no == "yes":
        running = True
    else:
        running = False
while True:
    loop_count += 1
    if running:
        print("Run loop RUN!!!")
    if loop_count >= 500:
        print("Entered a endless loop or user really loved this loop so much they reach 500 loops. closing")
        break

exit()

