init python:

    class Difficulty:
        def __init__(self):
            self.easy = {'partial': 4, 'full': 7}
            self.medium = {'partial': 7, 'full': 10}
            self.hard = {'partial': 9, 'full': 12}
            self.heroic = {'partial': 11, 'full': 14}
            self.legendary = {'partial': 12, 'full': 16}
            self.godlike = { 'partial': 13, 'full': 18}

    class DiceBox:
        def __init__(self):
            self.dice1 = '1'
            self.dice2 = '2'
        def changeDice(self, d1, d2):
            self.dice1 = d1
            self.dice2 = d2

    class Player:
        def __init__(self):
            self.stats = {'flair':1, 'focus':1, 'force':1, 'guile':1, 'haste':1, 'smart':1}
            self.name = 'Philia'
            self.gender = 'female'
            self.pronouns = {'subject':'she', 'object':'her', 'dep_possessive':'her', 'indep_possessive':'hers', 'reflexive':'herself'}
            self.experience = {'experience':0, 'skillUp':0, 'levelUp':''}
            self.morale = {'morale':5}
            self.abilities = {'alchemy': 0, 'athletics': 0, 'courtesy': 0,
                    'deception': 0, 'empathy': 0, 'engineering': 0,
                    'fencing': 0, 'lore': 0, 'magicka': 0,
                    'marksmanship': 0, 'riding': 0, 'stealth': 0,
                    'thievery': 0, 'vigilance': 0, 'willpower': 0}
            self.inventory = []
            self.itemBonus = {'alchemy': 0, 'athletics': 0, 'courtesy': 0,
                    'deception': 0, 'empathy': 0, 'engineering': 0,
                    'fencing': 0, 'lore': 0, 'magicka': 0,
                    'marksmanship': 0, 'riding': 0, 'stealth': 0,
                    'thievery': 0, 'vigilance': 0, 'willpower': 0}

##########################
## Stat based functions ##
##########################
        def changeName(self, newName):
            self.name = newName
        def changeGender(self, newGender):
            self.gender = newGender
        def changePronouns(self, newPronouns):
            if newPronouns == 'he':
                self.pronouns['subject'] = 'he'
                self.pronouns['object'] = 'him'
                self.pronouns['dep_possessive'] = 'his'
                self.pronouns['indep_possessive'] = 'his'
                self.pronouns['reflexive'] = 'himself'
            elif newPronouns == 'she':
                self.pronouns['subject'] = 'she'
                self.pronouns['object'] = 'her'
                self.pronouns['dep_possessive'] = 'her'
                self.pronouns['indep_possessive'] = 'hers'
                self.pronouns['reflexive'] = 'herself'
            elif newPronouns == 'they':
                self.pronouns['subject'] = 'they'
                self.pronouns['object'] = 'them'
                self.pronouns['dep_possessive'] = 'their'
                self.pronouns['indep_possessive'] = 'theirs'
                self.pronouns['reflexive'] = 'themselves'
        def changeStat(self, stat, modifier):
            self.stats['stat'] += modifier
        def changeExperience(self, modifier):
            self.experience['experience'] += modifier
            if self.experience['experience'] > 9:
                self.experience['experience'] -= 10
                self.experience['skillUp'] += 1
                self.changeLevelup()
                #TODO: play jingle upon levelup.
        def changeLevelup(self):
            if self.experience['skillUp'] == 0:
                self.experience['levelUp'] = ''
            elif self.experience['skillUp'] == 1:
                self.experience['levelUp'] = '+'
            elif self.experience['skillUp'] == 2:
                self.experience['levelUp'] = '++'
            elif self.experience['skillUp'] >= 3:
                self.experience['levelUp'] = '+++'
        def changeMorale(self, modifier):
            self.morale['morale'] += modifier
            #TODO: play animation of morale loss.
        def changeAbility(self, ability, modifier):
            self.abilities['ability'] += modifier
            self.experience['skillUp'] -= 1
            self.changeLevelup()

##################
## Skill checks ##
##################
        def skillCheck(self, diff, stat, ability):
            dice1 = renpy.random.randint(1,6)
            dice2 = renpy.random.randint(1,6)

            #TODO: simplify this.
            if diff == "easy":
                full = difficulty.easy['full']
                partial = difficulty.easy['partial']
            elif diff == "medium":
                full = difficulty.medium['full']
                partial = difficulty.medium['partial']
            elif diff == "hard":
                full = difficulty.hard['full']
                partial = difficulty.hard['partial']
            elif diff == "heroic":
                full = difficulty.heroic['full']
                partial = difficulty.heroic['partial']
            elif diff == "legendary":
                full = difficulty.legendary['full']
                partial = difficulty.legendary['partial']
            elif diff == "godlike":
                full = difficulty.godlike['full']
                partial = difficulty.godlike['partial']

            #rollDice(dice1, dice2) #TODO: make dice get rolled in the box.
            roll = dice1 + dice2 + self.stats[stat] + self.abilities[ability]*2 + self.itemBonus[ability]
            dicebox.dice1 = dice1
            dicebox.dice2 = dice2

            if roll >= full:
                result = "full"
            elif roll >= partial:
                result = "partial"
            elif roll < partial:
                result = "fail"
            self.gainExperience(result)
            return result

        # def rollDice(die1, die2):
        def gainExperience(self, check):
            if check == "full":
                self.changeExperience(1)
            elif check == "partial":
                self.changeExperience(2)
            elif check == "fail":
                self.changeExperience(3)

##########################
## Inventory management ##
##########################
        def addItem(self, item):
            self.inventory.append(item)
            if item.ability != '':
                self.itemBonus[item.ability] += item.bonus

        def removeItem(self, item):
            self.inventory.remove(item)
            if item.ability != '':
                self.itemBonus[item.ability] -= item.bonus

        def checkItem(self, itemName):
            for item in self.inventory:
                if item.id == itemName:
                    return True
                else:
                    return False

####################
## Initialization ##
####################
    difficulty = Difficulty()
    dicebox = DiceBox()
