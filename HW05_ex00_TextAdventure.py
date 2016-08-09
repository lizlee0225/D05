#!/usr/bin/env python3
# HW05_ex00_TextAdventure.py
##############################################################################
# Imports
from sys import exit

# Body
user_name = input('What is your name? ')

def infinite_stairway_room(count):
    print("{} walks through the door to see a dimly lit hallway.".format(user_name))
    print("At the end of the hallway is a", count * 'long ', 'staircase going towards some light')
    next = input("> ")
    
    # infinite stairs option
    if next == "take stairs":
        print('{} takes the stairs'.format(user_name))
        if (count > 0):
            print("but {} is not happy about it".format(user_name))
        gold_room()
    if "back" in next:
        main()
        pass


def gold_room():
    print("This room is full of gold.  How much does {} take?".format(user_name))

    next = input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, {} is not greedy, {} wins!".format(user_name, user_name))
        exit(0)
    else:
        dead("You greedy goose!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How is {} going to move the bear?".format(user_name))
    bear_moved = False

    while True:
        next = input("> ")

        if next == "take" or next == "honey":
            dead("The bear looks at {} then slaps {}'s face off.".format(user_name, user_name))
        elif next == "taunt" and not bear_moved:
            print("The bear has moved from the door. {} can go through it now.".format(user_name))
            bear_moved = True
        elif next == "taunt" and bear_moved:
            dead("The bear gets pissed off and chews {}'s leg off.".format(user_name))
        elif next == "open" or next == "door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here {} sees the great evil Cthulhu.".format(user_name))
    print("He, it, whatever stares at {} and {} goes insane.".format(user_name, user_name))
    print("Does {} flee for life or eat own head?".format(user_name))

    next = input("> ")

    if "flee" in next:
        main()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("{}\n Good job!".format(why))
    exit(0)


############################################################################
def main():
    # START the TextAdventure game
    print("{} is in a dark room.".format(user_name))
    print("There is a door to {}'s right and left, or there is a staircase in front.".format(user_name))
    print("Which one does {} take?".format(user_name))

    next = input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    elif next == "staircase":
        infinite_stairway_room(20)
    else:
        dead("You stumble around the room until you starve.")

if __name__ == '__main__':
    main()
