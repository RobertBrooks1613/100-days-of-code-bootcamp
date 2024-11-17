def filter_states_by_letters(first_letter):
    states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                        "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                         "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                         "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
                         "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
                         "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
                         "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]
    if first_letter == "all" or first_letter == "All":
        return states_of_america
    else:
        filter_states = [(index, s) for index, s in enumerate(states_of_america) if s.startswith(str(first_letter))]
        return filter_states


looking_up = True

while looking_up:
    choose = input("Hello and welcome to state displayer, give me the first letter of the state you want. : ")
    result = filter_states_by_letters(choose.capitalize())
    if len(choose) <= 1:
        print(result)
    elif choose == "all" or choose == "All":
        items_per_line = 5
        for i, state in enumerate(filter_states_by_letters("all")):
            if i > 0 and i % items_per_line == 0:
                print()  # Print a new line
            print(state, end=", ")
        print()

    elif not result:
        print("No data found")
    yes_or_no = input("Do another lookup?\n yes or no : ").lower()
    if yes_or_no == "yes":
        looking_up = True
    else:
        looking_up = False


