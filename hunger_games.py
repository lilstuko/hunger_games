import random
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

            while True:
                try:
                    special_ability = int(input("Are you good at: (Choose 1) \n1)reconizing and memorizing plants \n2)camoflauge \n3)snares\n"))
                    if special_ability >= 1 and special_ability <= 3:
                        break
                except ValueError:
                    print("Sorry! Please type the number of the option you wish to select!")

            player_character = Character(name, district, special_ability)
            player_character.display()
        
        else:    
            pass
                      
