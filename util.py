def choose_from_menu(possible_choices, prompt):
    while True:
        try:
            for index, option in enumerate(possible_choices):
                print(f"{index + 1}) {option}")
            choice = int(input(prompt))
            if choice >= 1 and choice <= len(possible_choices):
                choice = possible_choices[choice - 1]
                break
        except ValueError:
            print("Sorry! Please type the number of the option you wish to select!")        

    return choice