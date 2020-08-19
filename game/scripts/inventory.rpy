init python:

    class Item:
        def __init__(self, name, ability, bonus, description, icon, type):
            self.name = name
            self.ability = ability
            self.bonus = bonus
            self.description = description
            self.icon = '../images/items/' + icon
            self.type = type

            #self.setStats(name, ability, bonus, description)

        def setStats(self, name, ability, bonus, description):
            self.name = name
            self.ability = ability
            self.bonus = bonus
            self.description = description


    class Inventory:
        def __init__(self):
            self.inventory = []

        def addItem(self, item):
            #TODO add item

        def removeItem(self, item):
            #TODO remove item

        def addItemBonus(self, ability):
            activeBonus = 0
            #TODO check abilities of all items
            #TODO return the bonus
