from entities import *
# from main import *
# from maps import *

class Items:
    def __init__(self):
        pass

class Consumable_Items(Items):
    def use(self, player):
        pass

class HealingPotion(Consumable_Items):
    def __init__(self):
        self.name = "Potion de soin"
        self.stat_boost = 10

    def use(self, player):
        player.hp += self.stat_boost
        if player.hp > player.max_hp:
            player.hp = player.max_hp
        print(f"{player.name} a utilisé une {self.name} et a récupéré {self.stat_boost} points de vie.")
        
class AttackPotion(Consumable_Items):
    def __init__(self):
        self.name = "Potion d'attaque"
        self.stat_boost = 5

    def use(self, player):
        player.atk += self.stat_boost
        print(f"{player.name} a utilisé une {self.name} et a gagné {self.stat_boost} points de d'attaque pour un combat.")
        player.used_items.append(self)

class DefensePotion(Consumable_Items):
    def __init__(self):
        self.name = "Potion de défense"
        self.stat_boost = 4

    def use(self, player):
        player.defense += self.stat_boost
        print(f"{player.name} a utilisé une {self.name} et a gagné {self.stat_boost} points de défense pour un combat.")
        player.used_items.append(self)

class DeceptionDagger(Items):
    def __init__(self):
        self.name = "Dague de Tromperie"
        self.description = "Une dague sournoise, tranchante et agile. Chaque attaque inflige des dégâts modérés, mais avec une forte chance d'étourdir l'ennemi. Idéale pour les attaques rapides et les tactiques rusées."

healpotion = HealingPotion()
atkpotion = AttackPotion()
defpotion = DefensePotion()
deceptiondagger = DeceptionDagger()