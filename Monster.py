# Monster.py
# Thorin Schmidt
# 11/16/2016

''' Monster Package '''
import Character
from random import randint

class Monster(Character):
    ''' generic monster class '''
    def __init__(self, name = "Generic Foe", maxHealth = 100,
                 speed = 25, stamina = 25, strength = 10,
                 intelligence = 10, dexterity = 10,
                 inventory = [["potion", 2],["Leather", 1]]):
