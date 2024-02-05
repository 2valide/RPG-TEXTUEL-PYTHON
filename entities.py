import random
import time
from colorama import Fore, Back, Style
from items import *
"""   
    name, max_hp, hp, atk, defense, xp, xp_until_lvlup, level
    p1.max_hp, p1.hp, p1.atk, p1.defense, p1.xp, p1.xp_until_lvlup, p1.level p1.inventory


    Pour créer une classe joueur
    p1 = Player("Joueur")
"""


    
class Entity:
    def __init__(self, name : str):
        self.name = name
        self.max_hp = 10
        self.hp = 10  # Commence avec la santé maximale
        self.atk = 6
        self.defense = 5
        self.is_stunned = False

    def show_stats(self):
        print(f"Stats de {self.name}")
        print("------------")
        print(f"HP: {self.hp}/{self.max_hp}")
        print(f"Attaque: {self.atk}")
        print(f"Defense: {self.defense}")
        print(f"Niveau: {self.level}")
                
    def attack(self, target):
        crit_rate = 0.15
        damage = (self.atk*1.5) - target.defense
        if random.random() < crit_rate:
            damage = (self.atk*2.3) - target.defense
            print("Coup critique !")
        
        target.hp -= int(damage)
        print(f"{self.name} inflige {int(damage)} points de dégats à {target.name} !")
        time.sleep(2)
        
    def is_defeated(self):
        return self.hp <= 0
        
    
    def take_turn(self, target):
        pass
        
        

    
            
class Player(Entity):
    def __init__(self, name : str):
        super().__init__(name=name)
        self.level = 1
        self.xp = 0
        self.xp_until_lvlup = 20  # Valeur à ajuster selon votre logique de jeu
        self.inventory = []
        self.spe_cd = 0
        self.strong_cd = 0
        self.flee = False
        self.used_items = []
        
    def level_up(self):
        self.max_hp += 6
        self.hp = self.max_hp
        self.atk += 3
        self.defense += 2
        self.xp_until_lvlup *= 1.6
        self.level += 1
        print(f"{self.name} a monté de niveau !")
        
    def show_stats(self):
        super().show_stats()
        print(f"XP: {self.xp}/{self.xp_until_lvlup}")
        self.show_inv()     
             
    def show_inv(self): 
        print("Inventaire :")
        for i in self.inventory:
            print(i.name) 
            
    

    
    def show_ennemy_stats(self, monster):
        print(f"Stats de {monster.name}")
        print("-----------")
        print(f"HP: {monster.hp}")
        print(f"Attaque : Entre {monster.atk-random.randint(1,4)} et {monster.atk + random.randint(1, 4)}")
        print(f"Défense : Entre {monster.defense-random.randint(1,4)} et {monster.defense + random.randint(1, 4)}")
        
         
    def add_item(self, item):
        self.inventory.append(item)
             
    
    def use_item(self, item):
        if isinstance(item, Items):                         #Potion de défense = defpotion    
            if item in self.inventory:                      #Potion d'attaque = atkpotion
                item.use(self)                              #Potion de soin = healpotion
                self.inventory.remove(item)
            else:
                print(f"{self.name} ne possède pas {item.name} dans son inventaire.")
        else:
            print("Cet objet ne peut pas être utilisé")
                
    def xp_gain(self, xp_gained):
        self.xp += int(xp_gained)
        print(f"Vous avez gagné {int(xp_gained)} points d'expérience")
        while self.xp >= self.xp_until_lvlup:
            self.level_up()
            
    def show_xp(self):
        print(f"xp : {self.xp}/{self.xp_until_lvlup}")
                    
          
     #PARTIE COMBAT     
               
            
    def start_combat(self, target):
        print(f"Vous entrez en combat contre {target.name}")
        #Boucle tour par tour
        self.flee = False
        while not target.is_defeated() and not self.is_defeated():
            if self.strong_cd > 0:
                self.strong_cd -= 1
            if self.spe_cd > 0:
                self.spe_cd -= 1
                
            if self.is_stunned:
                print(f"{self.name} est étourdi et est incapable d'attaquer")
                self.is_stunned = False
                time.sleep(1.5)
            else:
                self.take_turn(target)
                
            if not target.is_defeated():
                if target.is_stunned:
                    print(f"{target.name} est étourdi et est incapable d'attaquer")
                    target.is_stunned = False
                    time.sleep(1.5)
                    
                elif self.flee:
                    break

                else:
                    target.take_turn(self)
                
            if target.is_defeated():
                print("Vous gagnez le combat !")
                target.hp = target.max_hp
                self.xp_gain(target.level*1.5)
                while len(self.used_items) > 0:  
                    if self.used_items[0] == atkpotion:
                        self.atk -= 5
                    if self.used_items[0] == defpotion:
                        self.defense -= 4
                    self.used_items.pop(0)
                break
            if self.is_defeated():
                while len(self.used_items) > 0:  
                    if self.used_items[0] == atkpotion:
                        self.atk -= 5
                    if self.used_items[0] == defpotion:
                        self.defense -= 4
                    self.used_items.pop(0)
                game_over()
                break
               
                
   
    def is_defeated(self):      
        return self.hp <= 0
         
    def take_turn(self, target):
        while True:
            print(Fore.GREEN + "\n1. Attaque simple")
            print("2. Coup bas")
            print("3. Fracas")
            print("4. Utiliser un objet")
            print("5. Afficher ses statistiques")
            print("6. Afficher les statistiques de l'ennemi")
            print("7. Informations sur les compétences")
            print("8. Fuir le combat")
            
            try:
                action = int(input())
                if action == 1:
                    self.attack(target)
                    break
                    
                elif action == 2:
                    if deceptiondagger in self.inventory:
                        if self.spe_cd != 0:
                            print("Cette attaque se recharge, patience !")
                        else:
                            self.special_attack(target)
                            break
                    else:
                        print(f"Vous devez posséder {deceptiondagger.name} pour pouvoir utiliser cette compétence")
                        time.sleep(2)
                        
                elif action == 3:
                    if self.strong_cd != 0:
                        print("Cette attaque se recharge, patience !")
                    else:
                        self.strong_attack(target)
                        break
                        
                elif action == 4:
                    if len(self.inventory) == 0:
                        print("Vous ne possedez aucun objet")
                        time.sleep(2)
                    else:
                        self.combat_use_item()
                        break
                        
                elif action == 5:
                    self.show_stats()
                    time.sleep(2)
                
                elif action == 6:
                    self.show_ennemy_stats(target)
                    time.sleep(2)
                
                elif action == 7:
                    print(Fore.CYAN + "Attaque simple")
                    time.sleep(0.3)
                    print("Une attaque des plus basiques, peut être critique\n")
                    time.sleep(1.5)
                    print("Coup bas")
                    time.sleep(0.3)
                    print("Une technique infligeant des dégâts réduits mais avec une probabilité significative d'immobiliser l'ennemi. Son exécution nécessite la possession l'objet Dague de Tromperie.\n ")
                    time.sleep(1.5)
                    print("Fracas")
                    time.sleep(0.3)
                    print("Une frappe d'une puissance dévastatrice, provoquant des dégâts considérables, mais soumise à une faible chance d'échouer.")
                    time.sleep(3)
                    
                elif action == 8:
                    flee_chance = 0.5
                    if random.random() > flee_chance:
                        print("Vous avez fui le combat.")
                        self.flee = True
                        break
                    else:
                        print("Vous n'avez pas réussi à fuir")
                        time.sleep(2)
                        break
                    
                else:
                    print("Action invalide. Veuillez choisir une action valide.")
            except ValueError:                    
                print("Action invalide. Veuillez choisir une action valide.")
                
                
    def special_attack(self, target):
            self.spe_cd = 2
            stun_rate = 0.6
            crit_rate = 0.15
            if random.random() < stun_rate:
                target.is_stunned = True
                print(f"{target.name} a été étourdi")
            damage = max(0, (self.atk*1.2) - target.defense)
            if random.random() < crit_rate:
                damage = (self.atk*1.8) - target.defense
                print("Coup critique !") 
            target.hp -= int(damage)
            print(f"{self.name} inflige {int(damage)} points de dégats à {target.name} !")
            time.sleep(2)                
        
    def strong_attack(self, target):
        miss_rate = 30
        crit_rate = 0.10
        if random.random() < miss_rate:
            damage = (self.atk*2.2) - target.defense
            if random.random() < crit_rate:
                damage = (self.atk*3.7) - target.defense
                print("Coup critique !")
            target.hp -= int(damage)
            print(f"{self.name} inflige {int(damage)} points de dégats à {target.name} !")
            self.strong_cd = 3
            time.sleep(2)   
        else:
            print(f"{self.name} a raté sa cible !")
        
    def combat_use_item(self):
        while True:
            try:
                for i, item in enumerate(self.inventory):
                    print(f"{i}. {item.name}")
                choice = int(input("Quel objet souhaitez vous utiliser ? "))
                if 0 <= choice < len(self.inventory):
                    self.use_item(self.inventory[choice])
                    break
                else:
                    print("Choix invalide. Veuillez entrer un numéro d'objet valide.")
                    time.sleep(2)
            except ValueError:
                print("Ce n'est pas un objet utilisable")    
                time.sleep(2)
                
    
        
player = Player("test")   
     
class Monster(Entity):
    def __init__(self, name:str):
        super().__init__(name=name)
        self.level = player.level+(random.randint(0,2))
        self.atk = 5+self.level
        self.defense = 3+self.level
        self.max_hp = 11+self.level
        self.hp = self.max_hp
        
    def take_turn(self, target):
        self.attack(target)
        pass


class Boss(Entity):
    def init(self, name:str, atk, defense, max_hp):
        super().init(name=name)
        self.level = player.level+4
        self.atk = 15
        self.defense = 10
        self.max_hp = 20
        self.hp = 20
        
    def take_turn(self, target):
        self.attack(target)
        pass
    
def game_over():
    print("    _____          __  __ ______    ______      ________ _____  ")
    print("   / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
    print("  | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
    print("  | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
    print("  | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
    print("   \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ \n")
                                                              
    
         
player = Player("placeholder")
    
    
    

    
    
    
    
