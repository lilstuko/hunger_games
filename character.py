import random 

class Character():
    def __init__(self, name, district, special_ability):
        self.name = name
        self.district = district
        self.special_ability = special_ability
        self.strength = self._ability_roll()
        self.intelligence = self._ability_roll()
        self.wisdom = self._ability_roll()
        self.dexterity = self._ability_roll()
        self.constitution = self._ability_roll()
        self.charisma = self._ability_roll()
        self.hit_points = self._calculate_hit_points(2, 8)

    def display(self):
        print(f"Name: {self.name}")
        print(f"District: {self.district}")
        print(f"Special Ability: {self.special_ability}")
        print(f"Your strength is {self.strength}")
        print(f"Your intelligence is {self.intelligence}")
        print(f"Your wisdom is {self.wisdom}")
        print(f"Your dexterity is {self.dexterity}")
        print(f"Your constitution is {self.constitution}")
        print(f"Your charisma is {self.charisma}")
        print(f"You have {self.hit_points} hit points")

    def _roll_die(self, sides = 20):                
        roll = random.choice(range(1, sides + 1))
        return roll

    def _ability_roll(self):
        '''Roll 4 dice and keep the three highest rolls.'''
        rolls = [self._roll_die(6) for _ in range(4)]
        sorted_rolls = sorted(rolls,reverse = True)
        return sum(sorted_rolls[0:3])   
        
    def _modifier(self, ability_score): 
        return int((ability_score - 10) / 2)

    def _calculate_hit_points(self, number_of_dice, sides):
        points = 0
        for _ in range(number_of_dice):
            points += self._roll_die(sides)
            
        points += self._modifier(self.constitution)
    
        return points

    def ability_check(self, ability, difficulty):
        roll = self._roll_die()
        check = roll + self._modifier(getattr(self, ability))
        if check >= difficulty:
            return True
        else:
            return False
