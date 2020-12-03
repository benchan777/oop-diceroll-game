class Shop:
    gold = 0

    def __init__(self, potions = 100, armor = 100, revives = 20):
        ''' Instantiates the Shop class with the following properties:
            potions: int
            armor: int
            revives: int
        '''
        self.potions = potions
        self.armor = armor
        self.revives = revives

    def display_shop(self):
        ''' Displays current shop inventory '''
        print(f"Potions: {self.potions} Price: 3 gold\nArmor: {self.armor} Price: 10 gold\nRevives: {self.revives} Price: 100 gold")