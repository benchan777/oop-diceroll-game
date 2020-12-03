import random

class Enemy:
    level = 1
    experience = 1

    def __init__(self, name, hp = 1):
        ''' Instance properties:
            hp: int
            name: string
            gold: int
            potions: int
        '''
        self.hp = hp * Enemy.level
        self.name = name

        # enemy loot, modified by level
        self.gold = random.randint(30, 50) * Enemy.level
        self.potions = random.randint(0, 3) * Enemy.level

    def attack(self):
        ''' Calculates damage done by opponent to player '''
        attack_damage = random.randint(1, 6)
        return attack_damage

    def revive(self, hp = 1):
        ''' Revives the enemy for the next round with newly generated loot '''
        self.hp = hp * Enemy.level
        self.gold = random.randint(30, 50) * Enemy.level
        self.potions = random.randint(0, 3) * Enemy.level
        print(f"hp:{self.hp}gold:{self.gold}potions:{self.potions}")

    def change_level(self):
        ''' Changes the level of the enemy '''
        level_input = int(input("Enter the level of the enemy you'd like to fight: "))
        Enemy.level = level_input

    def reset_loot(self):
        self.gold = 0
        self.potions = 0

    def get_name(self):
        ''' Retrieves the enemy's name '''
        name = self.name
        return name