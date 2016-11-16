# GameEngine.py
# Thorin Schmidt
# 11/15/2016

'''module that contains classes and functions to run a game'''
from random import randint
import Character

def combat(one, two):
    ''' runs combat between two Characters, named one and two'''
    combatIsOver = False
    while not combatIsOver:
        print("""
                  YOU ARE IN COMBAT!
                  What do you want to do?
                  You can:
                     A)ttack
                     H)eal
                     F)lee""")
        choice = input("              Your Choice [A/h/f]: ")
        if choice.lower() == "f":
            if one.flee():
                print(one.name, "flees in terror!")
                combatIsOver = True
            else:
                print(one.name, "cannot flee!")
        elif choice.lower() == "h":
            one.heal()
        else:
            one.attack(two)

        #enemy AI
        twoChoice = randint(1,3)
        if twoChoice == 1:
            if two.flee():
                print(two.name, "flees in terror!")
                combatIsOver = True
            else:
                print(two.name, "cannot flee!")
        elif twoChoice == 2:
            two.heal()
        else:
            two.attack(one)

        if one.health < 0 or two.health < 0:
            combatIsOver = True

if __name__ == "__main__":
    hero = Character.Character()
    orc = Character.Character(name = "Dorque da Orc")

    combat(hero, orc)

    
