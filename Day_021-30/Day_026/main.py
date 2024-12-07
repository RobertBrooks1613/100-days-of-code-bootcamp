# import random
#
# names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack"]
#
# students_score = {student:random.randint(1,100) for student in names}
#
# passed_students = {student for student,score in students_score.items() if score > 60}
# print(students_score)
# print(", ".join(f"{student}: {students_score[student]}" for student in passed_students))
from os.path import split



# data = pandas.read_csv("nato_phonetic_alphabet.csv").to_dict(orient="dict")
# data_letters = [letter for letter in data.items()]

import pandas
# input("Enter come text\n").upper()
# below works too to make data 1 line vs 2 dicts
# data = pandas.read_csv("nato_phonetic_alphabet.csv").set_index("letter").to_dict()["code"]

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter:row.code for (index, row) in data.iterrows()}

user_input = input("Enter come text\n").upper()

print(", ".join(f"{letter} : {phonetic_dict[letter]}" for letter in user_input))


