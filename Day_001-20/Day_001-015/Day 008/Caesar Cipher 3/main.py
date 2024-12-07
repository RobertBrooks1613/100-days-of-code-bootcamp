import art
import sys

def get_input(prompt):
    try:
        return input(prompt)
    except RuntimeError:
        print("Standard input is not available. Using default values for testing.")
        return "default"

text_art = art.logo
encoding_or_decoding = True
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

print(text_art)

while encoding_or_decoding:
    direction = get_input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = get_input("Type your message:\n").lower()
    shift_input = get_input("Type the shift number:\n")

    if shift_input.isdigit():
        shift = int(shift_input)
    else:
        print("Invalid shift number. Using default value of 0.")
        shift = 0

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    yes_or_no = get_input("Would you like to encode or decode again?\nYes or No : ").lower()
    if yes_or_no == "yes":
        encoding_or_decoding = True
    elif yes_or_no == "no":
        encoding_or_decoding = False
    else:
        print(f"{yes_or_no} is an incorrect option. Exiting program now.")
        encoding_or_decoding = False
exit()