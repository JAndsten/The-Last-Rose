init python:

    class Item:
        def __init__(self, id, name, ability, bonus, description, icon, type):
            self.name = name
            self.ability = ability
            self.bonus = bonus
            self.description = description
            self.icon = '../images/items/' + icon
            self.type = type

            self.setStats(name, id, ability, bonus, description, icon, type)

        def setStats(self, id, name, ability, bonus, description, icon, type):
            self.name = name
            self.id = id
            self.ability = ability
            self.bonus = bonus
            self.description = description
            self.icon = icon
            self.type = type

###############################
## List of items in the game ##
###############################

    #Key items

    #Weapons
    noble_sword = Item('Noble\'s Sword', 'noble_sword', 'fencing', 1, 'A slender and well balanced sword for an up and coming duelist. +1 Fencing', 'noble_sword.png', 'weapon')
    flint_pistol = Item('Courtier\'s Pistol', 'flint_pistol', 'marksmanship', 1, 'A well crafted flintlock pistol, made for courtiers. Easy to handle and reasonably accurate. +1 Marksmanship', 'flintlock_pistol.png', 'weapon')

    #Accessories
    lore_tome = Item('Religious Tome', 'lore_tome', 'lore', 1, 'A tome of religious lore and symbology. It\'s a bit dense, but could come in handy later.', 'lore_tome.png', 'accessory')

    #Consumables
    coins = Item('Pouch of Coins', 'coins', '', '', 'A weighty pouch full of coins. Most people need these to get by. Can be exchanged for goods and services.', 'purse.png', 'money')
