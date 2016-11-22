# GameEngine.py
# Thorin Schmidt
# 11/15/2016

'''module that contains classes and functions to run a game'''
from random import randint
from character import *
from monster import *
from items import *

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

def create_player():
    '''  generate a character based on user input

        This function contains several local functions, each using a different
        method of chaaracter creation:
            simple - the user is asked which stat(str, dex, con, int, wis, cha)
                is most important, and which is least.  most important gets
                a value of 17, least gets a 9, and the rest get 12. This method
                is suitable for a 20-point character build using Pathfinder d20
                rules.  This method has only a few choices, and results in
                moderate satisfaction for the user.
            hardcore - results are generated randomly using the 3d6 method, in
                standard stat block sequence: (str, dex, con, int, wis, cha).
                if none of the stats are over 12, then the entire set is re-
                rolled until it does. The user has no control over ability
                scores. This method is the easiest, but usually has the least
                satisfaction for the user.
            4d6, keep best three, arrange to suit - 6 sets of 4d6 are rolled,
                in each set, the top three dice are kept and added together.
                Then these scores are assigned by the user. This method usually
                has the highest satisfaction for the player, but is also the
                most complicated, due to the many choices required.'''

    def simple():
        return Character()

    def hardcore():
        ''' use 3d6, in order of stats, no rerolls unless all under 13

            hardcore - results are generated randomly using the 3d6 method, in
                standard stat block sequence: (str, dex, con, int, wis, cha).
                if none of the stats are over 12, then the entire set is re-
                rolled until it does. The user has no control over ability
                scores. This method is the easiest, but usually has the least
                satisfaction for the user.'''

        valid = False
        while not valid:

            gStrength = randint(3,18)
            gDexterity = randint(3,18)
            gConstitution = randint(3,18)
            gIntelligence = randint(3,18)
            gWisdom = randint(3,18)
            gCharisma = randint(3,18)
            if gStrength > 11 or gDexterity > 11 or\
               gConstitution > 11 or gIntelligence > 11 or\
               gWisdom > 11 or gCharisma > 11:
                valid = True
        gName = input("What is your character's name?: ")
        gPotionCount = 0
        gWeapon = Weapon(name = "Stick", base = 3, bonus = 0)
        gArmor = Armor(name = "Loincloth", base = 0, bonus = 0)
        gHealth = randint(1,8)
        if gConstitution > 12:
            gHealth += 1
        
        return Character(name = gName, strength = gStrength,
                         dexterity = gDexterity, constitution = gConstitution,
                         intelligence = gIntelligence, wisdom = gWisdom,
                         charisma = gCharisma, numberOfPotions = gPotionCount,
                         weapon = gWeapon, armor = gArmor, maxHealth = gHealth)

    def four_d_six():
        return Character()

    #main menu
    satisfied = False
    while not satisfied:
        valid = False
        while not valid:
            choice = input('''
                             Player Creation Menu
                            -------------------------
                               1) Hardcore
                               2) Simple
                               3) 4d6, Arrange to suit
                               4) Method Descriptions
                            --------------------------
                            Choose [1-4]: ''')
            if choice in ('1','2','3','4'):
                valid = True
            else:
                print("*** Invalid Input! ***\n\n")
        if choice == '4':
            help(create_player)
            continue
        elif choice == '3':
            player = four_d_six()
        elif choice == '2':
            player = simple()
        elif choice == '1':
            player = hardcore()
        else:
            print("***  ERROR - something went wrong here! ***")
        valid = False
        while not valid:
            print(player)
            happyNow = input("Do you wish to play this character?[y/n]? ")
            if happyNow.lower() in ('y', 'n'):
                valid = True
            else:
                print("*** y or n only! ***\n")
        if happyNow == 'y':
            satisfied = True

    return player

if __name__ == "__main__":
    hero = create_player()
    print(hero)
    #hero = Character()
    orc = Monster(name = "Dorque da Orc")

    combat(hero, orc)

    
