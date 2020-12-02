import random

class Enemy:
    def __init__(self, level, hp = 30):
        ''' Instance properties:
            hp: int
            name: string
            gold: int
            potions: int
        '''
        self.hp = hp * level
        self.name = "Enemy"

        # enemy loot, modified by level
        self.gold = random.randint(30, 50) * level
        self.potions = random.randint(0, 3) * level

    def attack(self):
        ''' Calculates damage done by player to opponent '''
        attack_damage = random.randint(1, 6)
        # print(f"You deal {attack_damage} damage to your opponent!")
        return attack_damage