import random
from enemy import Enemy
from player import Player
from shop import Shop

class User:
    def __init__(self, player = " ", enemy = " "):
        ''' Instance properties:
            player: string
            enemy: string
        '''
        self.player = Player(input("Enter a name: "))
        self.enemy = Enemy(input("Enter enemy's name: "))

    def run_game(self):
        self.enemy.change_level()
        game_start = Game(self.player, self.enemy)
        game_start.start_battle()
        self.player.is_dead()

        while self.player.is_dead() != True:
            game_start.display_options(self.player, self.enemy)
            self.player.is_dead()

        print("You have died. Game over")

class Game(User):
    win_count = 0

    def __init__(self, player, enemy):
        ''' Instance properties:
            player: string
            enemy: string
        '''
        self.player = player
        self.enemy = enemy

    def start_battle(self):
        ''' Starts the battle between the player and enemy '''
        self.player.battle(self.enemy)

    def display_options(self, player, opponent):
        ''' Displays options to choose from after a battle '''
        print("What would you like to do now?\n1: Enter a new battle\n2: Display your current HP and inventory\n3: Open the shop\n4: Restore HP\n5: Exit game\n")
        user_selection = input("Choose an option: ")

        if user_selection == "1":
            opponent.change_level()
            opponent.revive()
            player.battle(opponent)

            if player.is_dead() != True:
                Game.win_count += 1

        elif user_selection == "2":
            player.display_inventory()

        elif user_selection == "3":
            shop.display_options()

        elif user_selection == "4":
            player.restore_hp(Game.win_count)

        else:
            print("You have exited the game.")
            quit()

#------------------------------------------------
# Start game
#------------------------------------------------
shop = Shop()
user = User()
user.run_game()