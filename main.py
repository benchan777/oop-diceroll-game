import random
from characters import Enemy

class Player:
    def __init__(self, name, hp = 30, armor = 0):
        ''' Instantiates the player class '''
        self.name = name
        self.hp = hp
        self.armor = armor

        # inventory
        self.potions = 3
        self.revives = 0
        self.gold = 0

    def attack(self):
        attack_damage = random.randint(1, 6)
        print(f"You deal {attack_damage} damage to your opponent!")
        return attack_damage

    def enemy_attack(self):
        attack_damage = random.randint(1, 6) * ((100-self.armor)/100)
        print(f"Enemy deals {attack_damage} damage to {self.name}!")
        return attack_damage

    def battle(self, enemy):
        while self.hp > 0 and enemy.hp > 0:
            print(f"{self.name} attacks the enemy! The enemy has {enemy.hp}hp remaining.")
            enemy.hp -= self.attack()
            print(f"The enemy attacks {self.name}! {self.name} has {self.hp}hp remaining.")
            self.hp -= self.enemy_attack()

        if self.hp > enemy.hp:
            print(f"{self.name} won!")
        else:
            print(f"Oh no, you've lost =(")

class Game:
    def __init__(self):
        self.player = Player(input("Enter a name: "))
        self.enemy = Enemy(int(input("Enter what level enemy you want to fight: ")))

    def start_battle(self):
        self.player.battle(self.enemy)

if __name__ == "__main__":
    game = Game()
    game.start_battle()