# GameEngine.py
# Thorin Schmidt
# 11/15/2016

'''module that contains classes and functions to run a game'''
import random

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
        twoChoice = random.randint(1,3)
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

class Character(object):
    ''' Base player class'''
    def __init__(self, name = "Average Joe", maxHealth = 100):
        ''' all values represent the base, or average score '''
        self.name = name
        self.maxHealth = maxHealth
        self.health = 100
        self.speed = 25
        self.hunger = 100  # 100 = Full belly, 0 = starving
        self.stamina = 25
        self.strength = 10 
        self.intelligence = 10 
        self.dexterity = 10
        self.inventory = []

    def attack(self, enemy):
        ''' attack another Character'''
        if random.randint(1,2) == 2:
            print(self.name, "hits", enemy.name+".")
            damage = random.randint(1,10)+self.strength
            enemy.health -= damage
            print("and does", damage, "damage.")
        else:
            print(self.name, "misses", enemy.name+".")
        
    def heal(self):
        '''  randomly heal 1d8+1 health points'''
        heal = random.randint(2,9)
        self.health += heal
        print(self.name, "heals for", str(heal) + ".")
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def flee(self):
        if random.randint(1,4) == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    hero = Character()
    orc = Character(name = "Dorque da Orc")

    combat(hero, orc)
    print ("Combat is over, and", hero.name, "is...")
    if hero.health > 0:
        print("Alive")
    else:
        print("Dead.")
'''
    hero.attack(orc)
    orc.attack(hero)

    print(hero.health)
    print(orc.health)

    hero.heal()
    orc.heal()

    print(hero.health)
    print(orc.health)
   ''' 




    






    
