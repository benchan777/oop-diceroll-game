class Player:
    def __init__(self, name):
        self.hp = 30
        self.name = name

        # inventory
        self.potions = 3
        self.revives = 0
        self.gold = 0