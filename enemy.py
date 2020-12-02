import random

class Enemy:
    def __init__(self):
        self.hp = 30
        self.name = "Enemy"

        # loot
        self.gold = random.randint(30, 50)
        self.potions = random.randint(0, 1)