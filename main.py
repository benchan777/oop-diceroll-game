import player
import enemy

class Game:
    def __init__(self):
        name = input("Welcome to the game! Please enter your player's name: ")
        self.name = player(name)