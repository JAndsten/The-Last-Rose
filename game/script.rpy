# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

#python:
#    def set_statblock(pc):
#        name = pc.name
#        statblock = "Name: [name]"
#        return statblock

# The game starts here.

label start:
    $ player = Player()
    #$ active_statblock = player.set_statblock2()
    #$ active_pc = player

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    e "Time to test inventory addition."

    $ player.addItem(noble_sword)
    $ player.addItem(coins)

    e "Your item bonus for Fencing is [player.itemBonus[fencing]]"

    e "Time to check item recognition."

    $ sword_exists = player.checkItem('noble_sword')

    e "The sword existing is [sword_exists]."

    e "Next up, we remove items."

    $ player.removeItem(noble_sword)
    $ sword_exists = player.checkItem('noble_sword')

    e "The sword existing is [sword_exists]."

    e "This is just to check rollback."

    # This ends the game.

    return
