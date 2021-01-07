import os
import random

from character import Character

class CharacterCreator():
    def make_custom_character(self): 
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

        return Character(name, district, special_ability)

    def generate_random_character(self):
        reroll = True
        while reroll == True:
            district = random.choice(range(1, 13))
            
            possible_names = Character.district_names[district - 1]
            name = random.choice(possible_names)

            possible_sa = Character.special_abilities[district - 1]
            special_ability = random.choice(possible_sa)

            os.system('clear')
            print(f"Name: {name}\nDistrict: {district}\nSpecial Ability: {special_ability}")
            new_character = input("\nIf you would like to generate a new character, press 'n' then hit Enter. Otherwise, press Enter. ")
            if new_character != 'n':
                reroll = False
        
        return Character(name, district, special_ability)