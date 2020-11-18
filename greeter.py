import re

class Greeter():
    def __init__(self, prompt):
        self.prompt = prompt
        
    def greet(self):
        wanna_play_game = input(self.prompt).lower()
        return re.search(r'\bno\b', wanna_play_game)
       
