# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Film")
define n = Character("Naaa")
define you = Character("[player_name]")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    stop music fadeout 1.0

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Choose your name"

    $ player_name = renpy.input("What is your name?")
    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="FilmZz"

    e "Very nice name"

    you "Thanks !"

    scene bg black with fade

    window hide

    show text Text("This is film", size=60) as centered_text:
        xalign 0.5
        yalign 0.5
    with dissolve
    pause 1

    hide centered_text

    show text Text("500 years ago", size=60) as centered_text_2:
        xalign 0.5
        yalign 0.5
    with dissolve
    pause 1

    hide centered_text_2 with dissolve

    scene bg room with fade

    play music "share/sence.ogg"

    show film rabbit with dissolve:
        xalign 0.5
        yalign 0.125

    # These display lines of dialogue.

    e "สวัสดี!, นี่คือเกม DEMO"

    e "Hello this is a test game"

    play sound "share/punch.mp3" volume 0.5

    show film rabbit with hpunch

    e "Here is the shake"

    show film rabbit:
        yalign 0.125
        parallel:
            ease 1.0 zoom 1.5

    e "Here is the zoom"

    show film rabbit:
        parallel:
            ease 1.0 zoom 1
        parallel:
            linear 0.5 yalign 0.125

    show film rabbit:
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
    stop music fadeout 1.0
    pause

    e "That is the pause"
    
    return

image Note = "share/Note.png"

label noC:
    e "You selected No" 
    
    show Note with dissolve :
        xpos 880
        ypos 220

    n "You got a note"

    return

label utyC:
    e "You selected Up to you"
    
    e "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s"

    return
