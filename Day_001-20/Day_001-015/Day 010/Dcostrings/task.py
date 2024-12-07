def format_name(f_name, l_name):
    """Takes in a First and Last name and returns them together with a space.
    and makes the first letter capitalized and all others lowercase automatically """
    name_formated = f_name + ' ' + l_name
    return name_formated.title()


users_f_name = input("What is your first name?\n")
users_l_name = input("What is your last name?\n")
print(format_name(f_name=users_f_name, l_name=users_l_name))
user_input = input(f'Write out a math problem\n'
                   f'use numbers only and these symbols.\n'
                   f'[ * multiplication ],[ / division, + addition],[ - subtraction],[ % modulo],[ () parentheses]\n'
                   f' ')
problem = eval(user_input)
print(f"{user_input} = {problem}")



