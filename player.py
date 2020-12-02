import random

class Player:
    def __init__(self, name):
        self.hp = 30
        self.armor = 0
        self.name = name

        # inventory
        self.potions = 3
        self.revives = 0
        self.gold = 0

    def attack(self):
        attack_damage = random.randint(1, 6)
        return attack_damage