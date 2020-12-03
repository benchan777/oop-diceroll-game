from player import Player

class Shop:
    potion_price = 3
    armor_price = 10
    revives_price = 100

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
        print(f"1 - Potions: {self.potions} Price: 3 gold\n2 - Armor: {self.armor} Price: 10 gold\n3 - Revives: {self.revives} Price: 100 gold\n")
        shop_input = int(input(f"What would you like to purchase? "))

        while shop_input < 4:
            if shop_input == 1:
                if Player.gold < Shop.potion_price:
                    print("You have insufficient gold!")
                else:
                    self.potions -= 1
                    Player.gold - Shop.potion_price
                    print(f"You have purchased 1 potion! You have {Player.gold} gold remaining.")
        print("exiting shop\n")