import random

class Player:
    def __init__(self, name):
        ''' Instantiates the player class '''
        self.hp = 30
        self.armor = 0
        self.name = name

        # inventory
        self.potions = 3
        self.revives = 0
        self.gold = 0

    # player attack function that deals random damage between 1 and 6
    def attack(self):
        attack_damage = random.randint(1, 6)
        return attack_damage

class Enemy:
    def __init__(self, level):
        self.hp = 30 * level
        self.name = "Enemy"

        # enemy loot, modified by level
        self.gold = random.randint(30, 50) * level
        self.potions = random.randint(0, 1) * level

    # enemy attack function that deals random damage between 1 and 6
    def attack(self):
        attack_damage = random.randint(1, 6)
        