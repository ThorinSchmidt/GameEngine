# GameEngine.py
# Thorin Schmidt
# 11/15/2016

'''module that contains classes and functions to run a game'''
from random import randint
from character import *
from monster import *

def combat(one, two):
    ''' runs combat between two Characters, named one and two'''

    def take_action(current, target, choice):
        '''handle the current active character's choice

            current is the one doing the action, choice is the chosen action,
            target is the opponent who could be attacked. The function returns
            a Boolean, which indicates whether to end the combat loop.'''
        
        isOver = False
        
        if choice == "f":
            isOver, message = current.flee() #Fleeing ends combat
            
        elif choice == "h":
            success, message = current.heal() #This has no effect on the loop
            
        else:
            success, message = current.attack(target)
            if target.health <= 0:  #combat ends if the enemy dies
                isOver = True
                message += "\n" + target.name + " is Dead!"

        print(message)

        return isOver
        #end of internal function
    
    ''' combat function begins here'''    
    combatIsOver = False
    rounds = 0
    while not combatIsOver:
        rounds +=1
        print("\nRound", rounds, "begins...")
        # 'Init' is short for 'Initiative', got tired of typos - TMS
        oneInit = randint(1, 20) + one.speed
        twoInit = randint(1, 20) + two.speed
        if oneInit >= twoInit:
            combatIsOver = take_action(one, two, one.combat_choice())
            if combatIsOver:
                continue # go directly to beginning of loop
            combatIsOver = take_action(two, one, two.combat_choice())
        else:
            combatIsOver = take_action(two, one, two.combat_choice())
            if combatIsOver:
                continue # go directly to beginning of loop
            combatIsOver = take_action(one, two, one.combat_choice())



if __name__ == "__main__":
    hero = Character()
    orc = Monster(name = "Dorque da Orc")

    combat(hero, orc)

    
