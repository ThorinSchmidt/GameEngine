# Character.py
# Thorin Schmidt
# 11/16/2016

''' Module that contains our game's Character base class '''
from random import randint

class Character(object):
    ''' Base Character Class '''
    def __init__(self, name = "Average Joe", maxHealth = 100,
                 speed = 25, stamina = 25, strength = 10,
                 intelligence = 10, dexterity = 10,
                 inventory = [["potion", 2],["Leather", 1]]):
        ''' All values represent the average score '''
        self.name = name
        self.maxHealth = maxHealth
        self.health = maxHealth
        self.speed = speed
        self.hunger = 100 # 100 = Full, 0 = starving
        self.stamina = stamina
        self.strength = strength
        self.intelligence = intelligence
        self.dexterity = dexterity
        self.inventory = []
        for item in inventory:
            self.inventory.append(item)
        

    def heal(self):
        ''' randomly heal 1d8+1 points'''
        #first check if there is a potion in inventory
        healed = False
        for item in self.inventory:
            if item[0] == "potion":
                print(self.name, "drinks a potion.")
                heal = randint(2,9)
                self.health += heal
                print(self.name, "heals for", heal, "points.")
                if self.health > self.maxHealth:
                    self.health = self.maxHealth
                item[1] -= 1
                if item[1] == 0:
                    self.inventory.remove(item)
                healed = True
        if not healed:
            print(self.name, "Has no potions!")
            print(self.inventory)
                

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

    













        
        
