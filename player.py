import random
import time
from enemy import Enemy

class Player:
    potions = 3
    revives = 0
    gold = 0
    armor = 0

    def __init__(self, name, hp = 30):
        ''' Instantiates the player class with the following properties:
            name: string
            hp: int
            armor: int
        '''
        self.name = name
        self.hp = hp
        # self.armor = armor
    
    @classmethod
    def remove_gold(cls, amount):
        ''' Removes gold from player class '''
        cls.gold -= amount

    @classmethod
    def add_potions(cls, amount):
        ''' Add potions to player inventory '''
        cls.potions += amount

    @classmethod
    def add_revives(cls, amount):
        ''' Add revives to player inventory '''
        cls.revives += amount
    
    @classmethod
    def add_armor(cls, amount):
        ''' Increase base hp of player '''
        cls.armor += amount

    def attack(self):
        ''' Override enemy's attack method '''
        attack_damage = random.randint(1, 6)
        print(f"You deal {attack_damage} damage to your opponent!")
        return attack_damage

    def take_damage(self, enemy):
        ''' Modifies damage done by enemy to player based on player armor '''
        damage_taken = enemy.attack() * ((100-Player.armor)/100)
        print(f"{enemy.get_name()} deals {damage_taken} damage to {self.name}!")
        return damage_taken

    def is_dead(self):
        ''' Checks if the player is alive or dead '''
        if self.hp < 1:
            return True
        else:
            return False

    def restore_hp(self, win_count):
        ''' Fully restores the player's hp '''
        self.hp = 30 + Enemy.experience * win_count + Player.armor

    def battle(self, enemy):
        ''' Player and opponent take turns attacking each other '''
        while self.hp > 0 and enemy.hp > 0:
            print(f"{self.name} attacks {enemy.get_name()}!")
            enemy.hp -= self.attack()
            print(f"{enemy.get_name()} has {enemy.hp}hp remaining.\n")
            
            if self.hp < 5 and Player.potions > 0:
                Player.potions -= 1
                self.hp += 5
                print(f"{self.name} uses a potion and gains 5 hp.")
            # time.sleep(1)
            if enemy.hp < 1:
                break

            print(f"{enemy.get_name()} attacks {self.name}!")
            self.hp -= self.take_damage(enemy)
            print(f"{self.name} has {self.hp}hp remaining.\n")
            # time.sleep(1)
            if self.hp < 1:
                break

        if self.hp > enemy.hp:
            print(f"{self.name} won!")
            self.take_loot(enemy)
        else:
            print(f"You have been defeated by {enemy.get_name()}")

    def take_loot(self, enemy):
        ''' If player wins, adds loot from the enemy to player's inventory '''
        Player.gold += enemy.gold
        Player.potions += enemy.potions
        print(f"You have picked up {enemy.gold} gold and {enemy.potions} potions!\n")
        enemy.reset_loot()

    def display_inventory(self):
        ''' Prints out items currently in the inventory '''
        print(f"Current HP: {self.hp}\nGold: {self.gold}\nPotions: {self.potions}\nArmor: {self.armor}\n")