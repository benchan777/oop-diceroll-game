import random
from enemy import Enemy
from player import Player
from shop import Shop

class Game:
    win_count = 0

    def __init__(self, player, enemy):
        ''' Instance properties:
            player: string
            enemy: int
        '''
        # self.player = Player(input("Enter a name: "))
        # self.enemy = Enemy(int(input("Enter what level enemy you want to fight: ")))
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        ''' Starts the battle between the player and enemy '''
        self.player.battle(self.enemy)

    def display_options(self):
        ''' Displays options to choose from after a battle '''
        print("What would you like to do now?\n1: Enter a new battle\n2: Display your current HP and inventory\n3: Open the shop\n4: Restore HP\n5: Exit game\n")
        user_selection = input("Choose an option: ")

        if user_selection == "1":
            opponent.change_level()
            # enemy_level = int(input("Input what level enemy you'd like to fight: "))
            opponent.revive()
            player.battle(opponent)
        elif user_selection == "2":
            player.display_inventory()
        elif user_selection == "3":
            shop.display_shop()
        elif user_selection == "4":
            player.restore_hp(Game.win_count)
        else:
            return "You have exited the game."

shop = Shop()
player = Player(input("Enter a name: "))
opponent = Enemy(input("Enter enemy's name: "))
opponent.change_level()
game = Game(player, opponent)
game.start_battle()
player.is_dead()

while player.is_dead() != True:
    game.display_options()
    player.is_dead()
    Game.win_count += 1

print("You have died. Game over")