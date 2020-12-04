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
        self._potions = potions
        self._armor = armor
        self._revives = revives

    def display_options(self):
        ''' Displays current shop inventory '''
        print(f"1 - Potions: {self._potions} Price: 3 gold\n2 - Armor: {self._armor} Price: 10 gold\n3 - Revives: {self._revives} Price: 100 gold\n")
        shop_input = input(f"What would you like to purchase? ")

        if shop_input == "1":

            if Player.gold < Shop.potion_price:
                print("You have insufficient gold!")

            else:
                self._potions -= 1
                Player.remove_gold(Shop.potion_price)
                Player.add_potions(1)
                print(f"You have purchased 1 potion! You have {Player.gold} gold remaining.\n")

        elif shop_input == "2":

            if Player.gold < Shop.armor_price:
                print("You have insufficient gold!")

            else:
                self._armor -= 1
                Player.remove_gold(Shop.armor_price)
                Player.add_armor(1)
                print(f"You have purchased 1 armor! You have {Player.gold} gold remaining.\n")

        elif shop_input == "3":

            if Player.gold < Shop.revives_price:
                print("You have insufficient gold!")

            else:
                self._revives -= 1
                Player.remove_gold(Shop.revives_price)
                Player.add_revives(1)
                print(f"You have purchased 1 revive! You have {Player.gold} gold remaining.\n")

        else:
            print("Exiting shop\n")