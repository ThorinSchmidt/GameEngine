# items.py
# Thorin Schmidt
# 11/17/2016

''' base items for the game environment'''
from random import randint

class Item(object):
    '''generic base class'''
    def __init__(self, name = "nameless thing", base = 0, bonus = 0):
        self.name = name
        self.base = base
        self.bonus = bonus

class Weapon(Item):
    '''generic weapon class'''
    def __init__(self, name = "Fists", base = 6, bonus = 0):
        super(Weapon, self).__init__(name, base, bonus)

    @property
    def attack(self):
        return self.bonus

    @property
    def damage(self):
        return randint(1, self.base) + self.bonus

class Armor(Item):
    '''generic armor class'''
    def __init__(self, name = "Leather", base = 1, bonus = 0):
        super(Armor, self).__init__(name, base, bonus)

    @property
    def defense(self):
        return self.base + self.bonus

class Potion(Item):
    '''generic healing potion class'''
    def __init__(self, name = "Cure Light", base = 8, bonus = 1):
        super(Potion, self).__init__(name, base, bonus)

    def use(self):
        return randint(1, self.base) + self.bonus

if __name__ == "__main__":
    weapon = Weapon()
    print("Weapon creation test:")
    print("---------------------")
    print("name  :", weapon.name)
    print("base  :", weapon.base)
    print("bonus :", weapon.bonus)
    print("---------------------")
    print("attack:", weapon.attack)
    print("damage:", weapon.damage)
    print()
    
    armor = Armor()
    print("Armor creation test:")
    print("--------------------")
    print("name   :", armor.name)
    print("base   :", armor.base)
    print("bonus  :", armor.bonus)
    print("---------------------")
    print("defense:", armor.defense)
    print()
    
    potion = Potion()
    print("Potion creation test:")
    print("---------------------")
    print("name   :", potion.name)
    print("base   :", potion.base)
    print("bonus  :", potion.bonus)
    print("---------------------")
    print("heal   :", potion.use())

    

    
