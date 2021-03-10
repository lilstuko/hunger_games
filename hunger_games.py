import os
import time

from greeter import Greeter
from character_creator import CharacterCreator
from character import Character
import util

if __name__ == '__main__':
    os.system('clear')
    greeter = Greeter("Hello, resident of Panem. Do you want to play a game? ")
    if greeter.greet():
        print("Ok, next time!")
    else:
        creator = CharacterCreator()
        choose_player = input("Great! \nPress 1 to create a custom player.\nPress 2 to randomly generate a player.\n")
        if choose_player == "1":
            player_character = creator.make_custom_character() 
        else:
            player_character = creator.generate_random_character()

        os.system('clear')
        player_character.display()
        input("Press Enter to continue: ")
        os.system('clear')

        if player_character.district == 1 or player_character.district == 2 or player_character.district == 4:
            career = "lunge forward to volunteer."
        else:
            career = "turn pale as your name is called out."

        print("THE REAPING")
        time.sleep(2)
        os.system('clear')

        print("Being the 4th of July, the day of the reaping is crazy hot like every year.")
        time.sleep(3)
        print(f"When the escort from the capitol calls out the name on the slip of paper, you {career}")
        time.sleep(3)
        print("You shake hands with your district partner, and turn and face the crowds as they cheer for you.")
        time.sleep(3)
        print("\nAfter the reaping, you are taken to the Justice Building, where you say goodbye to your family and best friend.")
        time.sleep(3)
        print("You are given a token to wear, a necklace of leather with a jade pendant, by your mother.")
        time.sleep(3)
        input("\nPress Enter to continue: ")
        os.system('clear')

        print("THE TRAIN RIDE")
        time.sleep(2)
        os.system('clear')

        if player_character.district == 1 or player_character.district == 2 or player_character.district == 4:
            career = "team up with the other Careers"
        else:
            career = "run away from the bloodbath"

        print("After you have said your goodbyes, you are escorted to a train by Peacekeepers.")
        time.sleep(3)
        print("When you reach the train, you meet your mentor, Gray Jackson, who won the 47th Hunger Games when they were 16.")
        time.sleep(3)
        print("Gray instructs you and your district partner, Alex, on how to survive the games.")
        time.sleep(3)
        input(f"Gray advises you to {career}. Are you going to take Gray's advice? ")
#        input(f"Does Gray advise you to...\n1)Team up with the{career}Careers\n2)Run away from the bloodbath\n3)Grab one thing and run\n")

        os.system('clear')
        print("THE TRIBUTE PARADE pt 1")
        time.sleep(2)
        os.system('clear')

        if player_character.district == 1 or player_character.district == 2 or player_character.district == 4:
            career = "excited"
        else:
            career = "terrified"    

        os.system('clear')
        print(f"Your first night in the Capitol, you can't sleep. You are {career} about being in the Arena in a few days.")
        time.sleep(3)
        print("The next morning you wake up when a trio of Capitol people, who you assume are your prep team, barge in.")
        time.sleep(3)
        print("They prep you and get you ready for the tribute parade.")
        time.sleep(3)
        
        possible_costume_theme = Character.chariot_costume_theme[player_character.district - 1]
        costume = util.choose_from_menu(possible_costume_theme, "Choose your costume theme: ")

        possible_costume_style = Character.costume_style
        costume_style = util.choose_from_menu(possible_costume_style, "Choose your costume style: ")
        
        print(f"Your stylist dressed you up in a {costume.lower()}-themed {costume_style.lower()}.")

        ### NEW SCENE ###
        os.system('clear')
        print("THE TRIBUTE PARADE pt 2")
        time.sleep(2)
        os.system('clear')

        print(f"During the parade,")
        time.sleep(3)
        print("stuff happens")
        time.sleep(3)
        print("They throw flowers at you.")
        time.sleep(3)        
