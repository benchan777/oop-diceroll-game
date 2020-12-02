import random
from enemy import Enemy

class Player:
    def __init__(self, name, hp = 30, armor = 0):
        ''' Instantiates the player class with the following properties:
            name: string
            hp: int
            armor: int
            potions: int
            revives: int
            gold: int
        '''
        self.name = name
        self.hp = hp
        self.armor = armor

        # inventory
        self.potions = 3
        self.revives = 0
        self.gold = 0

    def attack(self):
        ''' Calculates damage done by player to opponent '''
        attack_damage = random.randint(1, 6)
        print(f"You deal {attack_damage} damage to your opponent!")
        return attack_damage

    def take_damage(self, enemy):
        ''' Modifies damage done by enemy to player based on player armor '''
        damage_taken = enemy.attack() * ((100-self.armor)/100)
        print(f"Enemy deals {damage_taken} damage to {self.name}!")
        return damage_taken

    def battle(self, enemy):
        ''' Player and opponent take turns attacking each other '''
        while self.hp > 0 and enemy.hp > 0:
            print(f"{self.name} attacks the enemy!")
            enemy.hp -= self.attack()
            print(f"The enemy has {enemy.hp}hp remaining.\n")
            
            if self.hp < 5 and self.potions > 0:
                self.potions -= 1
                self.hp += 5
                print(f"{self.name} uses a potion and gains 5 hp.")


            print(f"The enemy attacks {self.name}!")
            self.hp -= self.take_damage(enemy)
            print(f"{self.name} has {self.hp}hp remaining.\n")

        if self.hp > enemy.hp:
            print(f"{self.name} won!")
            self.take_loot(enemy)
        else:
            print(f"Oh no, you've lost")

    def take_loot(self, enemy):
        ''' If player wins, adds loot from the enemy to player's inventory '''
        self.gold += enemy.gold
        self.potions += enemy.potions
        print(f"You have picked up {self.gold} gold and {self.potions} potions!")