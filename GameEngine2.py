# GameEngine.py
# Thorin Schmidt
# 11/15/2016

''' Module that contains classes and functions to run a game '''
from random import randint

def combat(one, two):
    ''' runs combat bewtween two Characters, one and two'''

    done = False
    while not done:
        # User Actions
        choice = input("""
                  YOU ARE IN COMBAT!
                  What do you want to do?
                  You can:
                     A)ttack
                     H)eal
                     F)lee
                Your Choice: [A/h/f]: """)
        if choice.lower() == "f":
            if one.flee():
                done = True
                print(one.name, "Flees in terror!")
            else:
                print(one.name, "cannot flee!")
        elif choice.lower() == "h":
            one.heal()
        else:
            one.attack(two)

        #Computer AI
        twoChoice = randint(1,3)
        if twoChoice == 1:
            if two.flee():
                done = True
                print(two.name, "Flees in terror!")
            else:
                print(two.name, "cannot flee!")
        elif twoChoice == 2:
            two.heal()
        else:
            two.attack(one)

        if one.health <= 0 or two.health <= 0:
            done = True
 


class Character(object):
    ''' Base Character Class '''
    def __init__(self, name = "Average Joe", maxHealth = 100):
        ''' All values represent the average score '''
        self.name = name
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.speed = 25
        self.hunger = 100 # 100 = Full, 0 = starving
        self.stamina = 25
        self.strength = 10
        self.intelligence = 10
        self.dexterity = 10
        self.inventory = []

    def heal(self):
        ''' randomly heal 1d8+1 points'''
        heal = randint(2,9)
        self.health += heal
        print(self.name, "heals for", heal, "points.")
        if self.health > self.maxHealth:
            self.health = self.maxHealth

    def flee(self):
        chance = randint(1,100)
        if chance <= self.speed:
            return True
        else:
            return False

    def attack(self, enemy):
        ''' attack another Character'''
        if randint(1,2) == 2: # 50% chance to hit
            print(self.name, "hits", enemy.name+",")
            damage = randint(1, 10) + self.strength
            enemy.health -= damage
            print("and does", damage, "damage.")
        else:
            print(self.name, "misses", enemy.name+".")























    
        

if __name__ == "__main__":
    hero = Character()
    orc = Character(name = "Dorque da Orc")
    
    combat(hero, orc)
    













        
        
