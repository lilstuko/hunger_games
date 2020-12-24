import random
import os

from greeter import Greeter
from character import Character

if __name__ == '__main__':
    greeter = Greeter("Hello, resident of Panem. Do you want to play a game? ")
    if greeter.greet():
        print("Ok, next time!")
    else:
        choose_player = input("Great! \nPress 1 to create a custom player.\nPress 2 to randomly generate a player.\n")
        if choose_player == "1":
            while True:
                try:
                    district = int(input("What district do you want to be from? (1-12) "))
                    if district >= 1 and district <= 12:
                        break
                except ValueError:
                    print("Sorry! Please type a number between and including 1 and 12!") 

            name = input("What do you want your name to be? ").title()

            possible_sa = Character.special_abilities[district - 1]

            while True:
                try:
                    for index, ability in enumerate(possible_sa):
                        print(f"{index + 1}) {ability}")
                    special_ability = int(input(f"Are you good at: (Choose 1) \n"))
                    if special_ability >= 1 and special_ability <= 3:
                        special_ability = possible_sa[special_ability - 1]
                        break
                except ValueError:
                    print("Sorry! Please type the number of the option you wish to select!")

        else:
            reroll = True
            while reroll == True:
                district = random.choice(range(1, 13))
                district_names = [
                    ["Emerald", "Velvet", "Shine"],
                    ["Glaucia", "Vesta", "Leonine"],
                    ["Pixel", "Link", "Zinn"], 
                    ["Ocean", "Tethys", "Luna"],
                    ["Shaya", "Halo", "Everly"],
                    ["Linx", "Wren", "Atlas"],
                    ["Aspen", "Ash", "Arden"],
                    ["Penelope", "Weaver", "Dior"], 
                    ["Barric", "Senwe", "Fonio"],
                    ["Brandy", "Tanner", "Dalton"],
                    ["Rue", "Thresh", "Chaff"],
                    ["Katniss", "Peeta", "Lucy Gray"],
                ]
                
                possible_names = district_names[district - 1]
                name = random.choice(possible_names)

                possible_sa = Character.special_abilities[district - 1]
                special_ability = random.choice(possible_sa)

                os.system('clear')
                print(f"Name: {name}\nDistrict: {district}\nSpecial Ability: {special_ability}")
                new_character = input("\nIf you would like to generate a new character, press 'n' then hit Enter. Otherwise, press Enter. ")
                if new_character != 'n':
                    reroll = False

        player_character = Character(name, district, special_ability)
        os.system('clear')
        player_character.display()
        input("Press Enter to continue: ")
        os.system('clear')              