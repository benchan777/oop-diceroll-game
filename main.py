import random
from enemy import Enemy
from player import Player

class Game:
    def __init__(self):
        ''' Instance properties:
            player: string
            enemy: int
        '''
        self.player = Player(input("Enter a name: "))
        self.enemy = Enemy(int(input("Enter what level enemy you want to fight: ")))

    def start_battle(self):
        self.player.battle(self.enemy)

if __name__ == "__main__":
    game = Game()
    game.start_battle()