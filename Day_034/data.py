
def get_data():
    import requests
    import html

    parameters = {
        "amount": 20,
        "type": "boolean"
    }

    response = requests.get("https://opentdb.com/api.php?", params=parameters)
    response.raise_for_status()
    question_data = response.json()["results"]
    return question_data

# question_data = [
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'Entertainment: Film',
#         'question': 'The word &quot;Inception&quot; came from the 2010 blockbuster hit &quot;Inception&quot;.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'Entertainment: Musicals &amp; Theatres',
#         'question': 'In the play Oedipus Rex, Oedipus kills his father due to jealousy in loving his mother.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'History',
#         'question': 'The French Kingdom helped the United States gain their independence over Great Britain during the Revolutionary War.',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'Entertainment: Film',
#         'question': 'In Alfred Hitchcock&#039;s film &#039;Psycho&#039; it is said he used chocolate syrup to simulate the blood in the famous shower scene from ',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'medium',
#         'category': 'Science &amp; Nature',
#         'question': 'The Doppler effect applies to light.',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'medium',
#         'category': 'Entertainment: Music',
#         'question': 'Ashley Frangipane performs under the stage name Halsey.',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'General Knowledge',
#         'question': 'A scientific study on peanuts in bars found traces of over 100 unique specimens of urine.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'Entertainment: Japanese Anime &amp; Manga',
#         'question': 'In the &quot;Toaru Kagaku no Railgun&quot; anime,  espers can only reach a maximum of level 6 in their abilities.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'medium',
#         'category': 'Geography',
#         'question': 'There are no roads in/out of Juneau, Alaska.',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'medium',
#         'category': 'General Knowledge',
#         'question': 'The term &quot;Spam&quot; came before the food product &quot;Spam&quot;.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'hard',
#         'category': 'Vehicles',
#         'question': 'In 1993 Swedish car manufacturer Saab experimented with replacing the steering wheel with a joystick in a Saab 9000.',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'Entertainment: Video Games',
#         'question': 'In Pok&eacute;mon, Arbok evolves into Seviper.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'Science &amp; Nature',
#         'question': 'Celiac Disease is a disease that effects the heart, causing those effected to be unable to eat meat.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'hard',
#         'category': 'Geography',
#         'question': 'Switzerland has four national languages, English being one of them.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'hard',
#         'category': 'Entertainment: Video Games',
#         'question': 'Unturned originally started as a Roblox game.',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'easy',
#         'category': 'Entertainment: Music',
#         'question': 'American rapper Dr. Dre actually has a Ph.D. doctorate.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'medium',
#         'category': 'Sports',
#         'question': 'Formula E is an auto racing series that uses hybrid electric race cars.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'hard',
#         'category': 'Entertainment: Video Games',
#         'question': 'In the game &quot;Melty Blood Actress Again Current Code&quot;, you can enter Blood Heat mode in Half Moon style.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'medium',
#         'category': 'Vehicles',
#         'question': 'The General Motors EV1 was the first street-legal production electric vehicle.',
#         'correct_answer': 'False',
#         'incorrect_answers': ['True']
#     },
#     {
#         'type': 'boolean',
#         'difficulty': 'medium',
#         'category': 'Entertainment: Video Games',
#         'question': 'Resident Evil 4 was originally meant to be a Nintendo GameCube exclusive.',
#         'correct_answer': 'True',
#         'incorrect_answers': ['False']
#     }
# ]