# Functions with input

# def greet_with_name(name, location):
#     print(f"Hello {name} from {location}")
#     print(f"How do you do {name}?")
#
# name_input = input("Hello what is your name? : ")
# location_input = input("Where are you from? : ")
#
# greet_with_name(name=name_input, location=location_input)

def calculate_love_score(name1, name2):
    name_to_check = name1.lower() + name2.lower()
    score1 = 0
    score2 = 0
    for char in name_to_check:
        if char in 'true':
            score1 += 1
    for char in name_to_check:
        if char in 'love':
            score2 += 1

    return print(f"{score1}{score2}")

name_1 = (input("What is your name? : "))
name_2 = (input("What is your partners name? : "))
calculate_love_score(name1=name_1, name2=name_2)