import random

# this will take in the min and max and check the order incase
# someone makes the min bigger than the max to avoid errors
def get_number_int(min_number, max_number):
    if min_number >= max_number:
        number = random.randint(max_number, min_number)
        return number
    else:
        number = random.randint(min_number, max_number)
        return number

def get_number_float(min_number, max_number):
    if min_number >= max_number:
        number = random.uniform(max_number, min_number)
        return number
    else:
        number = random.uniform(min_number, max_number)
        return number

def head_or_tails():
    number = random.random()
    if number >= 0.5:
        result = str("Tails")
        return result
    else:
        result = str("Heads")
        return result