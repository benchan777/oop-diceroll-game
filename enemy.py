import random

class Enemy:
    level = 1
    experience = 1

    def __init__(self, name, hp = 30):
        ''' Instance properties:
            hp: int
            name: string
            gold: int
            potions: int
        '''
        self._hp = hp * Enemy.level
        self.name = name

        # enemy loot, modified by level
        self.gold = random.randint(30, 50) * Enemy.level
        self.potions = random.randint(0, 3) * Enemy.level

    @classmethod
    def change_level(cls):
        ''' Changes the level of the enemy '''
        level_input = int(input("Enter the level of the enemy you'd like to fight: "))
        cls.level = level_input
        cls.experience = 3 * level_input

    def attack(self):
        ''' Calculates damage done by opponent to player '''
        attack_damage = random.randint(1, 6)
        return attack_damage

    def revive(self, hp = 30):
        ''' Revives the enemy for the next round with newly generated loot '''
        self._hp = hp * Enemy.level
        self.gold = random.randint(30, 50) * Enemy.level
        self.potions = random.randint(0, 3) * Enemy.level
        print(f"hp:{self._hp}gold:{self.gold}potions:{self.potions}")

    def reset_loot(self):
        ''' Sets the amount of loot to 0 '''
        self.gold = 0
        self.potions = 0

    def get_name(self):
        ''' Retrieves the enemy's name '''
        name = self.name
        return name

    def get_hp(self):
        ''' Retrieves the enemy's hp '''
        hp = self._hp
        return hp

    def take_damage(self, amount):
        ''' Removes hp from self '''
        self._hp -= amount