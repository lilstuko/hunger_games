import os
import random

from character import Character
import util

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
        special_ability = util.choose_from_menu(possible_sa, "Are you good at: (Choose 1) \n")

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