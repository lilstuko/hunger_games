import os

from greeter import Greeter
from character_creator import CharacterCreator

if __name__ == '__main__':
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