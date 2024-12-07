import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_count = len(letters) - 1
symbol_count = len(symbols) - 1
number_count = len(numbers) - 1
password_total_length = nr_letters + nr_symbols + nr_numbers

rng_password = []
final_password = ''
# other option is random.choice() which will choose a random item from the list and put it straight into a string.
for letter in range(0, nr_letters):
    rng = random.randint(0, letter_count)
    rng_letter = letters[rng]
    rng_password.append(random.choice(letters))

for symbol in range(0, nr_symbols):
    rng = random.randint(0, symbol_count)
    rng_symbol = symbols[rng]
    rng_password.append(rng_symbol)

for number in range(0, nr_numbers):
    rng = random.randint(0, number_count)
    rng_number = numbers[rng]
    rng_password.append(rng_number)


random.shuffle(rng_password)

final_password = rng_password

print(''.join(final_password))

