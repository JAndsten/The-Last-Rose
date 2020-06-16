init python:
    class Roller(object):
        def __init__(self, dice1, dice2, roll, result):
            self.dice1 = dice1
            self.dice2 = dice2
            self.roll = roll
            self.result = result
        @property
        def diceRoll(self):
            return result
#TODO make the difficulties integrate into the results.
#TODO add in active character changing.

#TODO define rollDice function that turns the results of the dice on screen to the result.

        def skillCheck(diff, stat, ability):
            self.dice1 = random.randint(1,6)
            self.dice2 = random.randint(1,6)
            #rollDice(dice1, dice2)
            self.roll = self.dice1 + self.dice2 + character.main_pc["stats"[stat]] + character.main_pc["abilities"[ability]]

            if roll >= difficulty.diff["full"]:
                self.result = "full"
            elif roll >= difficulty.diff["partial"]:
                self.result = "partial"
            else:
                self.result = "noSuccess"
#            gainExperience(result)
#            return self.result

        # def rollDice(die1, die2):
#        def gainExperience(check):
#            if check == "full":
#                character.main_pc["experience"] =+ 1
#            elif check == "partial":
#                character.main_pc["experience"] =+ 2
#            elif check == "fail":
#                character.main_pc["experience"] =+ 3

#TODO add effect of experience gain + levelup indicator.
