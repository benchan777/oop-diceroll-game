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
        ''' Calculates damage done by opponent to player '''
        attack_damage = random.randint(1, 6)
        return attack_damage

    def revive(self, level, hp = 30):
        ''' Revives the enemy for the next round with newly generated loot '''
        self.hp = hp * level
        self.gold = random.randint(30, 50) * level
        self.potions = random.randint(0, 3) * level