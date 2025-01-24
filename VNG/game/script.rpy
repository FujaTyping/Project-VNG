# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define n = Character("Naaa")
define you = Character("[player_name]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Choose your name"

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Film"

    e "Very nice name"

    you "Thanks !"

    show eileen happy with dissolve 

    # These display lines of dialogue.

    e "สวัสดี!, นี่คือเกม DEMO"

    e "Hello this is a test game"

    show eileen happy with hpunch

    e "Here is the shake"

    show eileen happy:
        parallel:
            ease 1.0 zoom 1.5
        parallel:
            yalign 0.0
            linear 0.5 yalign 0.125

    e "Here is the zoom"

    show eileen happy:
        parallel:
            ease 1.0 zoom 1
        parallel:
            linear 0.5 yalign 0.125

    show eileen happy:
        linear 1.0 xpos 0.225

    e "Here is the movement"

    menu:
        e "Choose the choice"
        "Yes":
            jump yesC
        "No":
            jump noC
        "Up to you":
            jump utyC

    # This ends the game.

    #return

label yesC:
    e "You selected Yes"

    window hide
    pause

    e "That is the pause"
    
    return

label noC:
    e "You selected No"

    show naaa with dissolve 
    
    n "I love haniff <3"

    return

label utyC:
    e "You selected Up to you"
    
    return
