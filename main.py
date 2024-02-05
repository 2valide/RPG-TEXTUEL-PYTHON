import json
import time   
from entities import *
from maps import deplacer_joueur




def main_menu():
    # Afficher les optionsf
    castel()
    print("MAIN MENU :")
    print("1. Création d'une nouvelle partie")                                          
    print("2. Charger une partie")
    print("3. Crédit")
    print("4. Fermer")

def introduction():
    print("Bienvenue dans le monde fantastique de Fantasia !")
    time.sleep(0.3)
    print("Depuis des siècles, des monstres terrifiants terrorisent les villages, semant le chaos et la destruction.")
    time.sleep(0.3)
    print("Votre quête est de pourchasser ces créatures maléfiques et de ramener la paix dans le royaume.")
    time.sleep(0.3)
    print("Préparez-vous, brave chevalier, l'aventure commence !")
    time.sleep(0.3)
    print("Les Îles de l'Aurore sont le point de départ de votre voyage. ")
    time.sleep(0.3)
    print("Alors que vous respirez l'air pur de l'aube, une vieille carte dans votre main indique des terres lointaines remplies de mystères. ")
    time.sleep(0.3)
    print("Une voix mystique dans votre esprit évoque le destin qui vous attend.")
    time.sleep(0.3)
    print("Vous êtes le héros choisi, appelé à explorer des contrées inconnues, à affronter des défis et à révéler des secrets millénaires.")
    time.sleep(0.3)
    print("Votre première destination est Îles de l'Aurore, un archipel paisible entouré d'eaux scintillantes. Des plages de sable fin bordent les rives, et des arbres luxuriants fournissent une ombre accueillante.")
    time.sleep(0.3)
    print(" Des plages de sable fin bordent les rives, et des arbres luxuriants fournissent une ombre accueillante.")
    time.sleep(0.3)
    print("Le ciel est baigné de teintes rosées et dorées, créant une atmosphère magique qui donne son nom aux îles. Les doux bruits des vagues bercent les rivages, accueillant les aventuriers intrépides qui débutent leur quête. ")
    time.sleep(0.3)
    print("Au loin, un vieux marin vous observe avec un sourire bienveillant.")
    time.sleep(0.3)
    print(" Il vous encourage à choisir une direction et à commencer votre quête. Les Îles de l'Aurore, berceau de votre aventure, vous invitent à prendre les premiers pas vers l'inconnu. Oserez-vous répondre à l'appel du destin qui résonne à travers ces îles enchantées?")
    time.sleep(0.3)
    
    print("Armez-vous de votre épée, mettez votre armure, et que la quête commence!")
    
    
def castel():
    CYAN = "\033[96m"
    RESET = "\033[0m"
    asciiart ="""         
    
    
    =========================================================
    =========================================================   


     
                               o                    
                           _---|         _ _ _ _ _ 
                        o   ---|     o   ]-I-I-I-[ 
       _ _ _ _ _ _  _---|      | _---|    \ ` ' / 
       ]-I-I-I-I-[   ---|      |  ---|    |.   | 
        \ `   '_/       |     / \    |    | /^\| 
         [*]  __|       ^    / ^ \   ^    | |*|| 
         |__   ,|      / \  /    `\ / \   | ===| 
      ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
      I_I__I_I__I_I  (====(_________)___|_|____|____
      \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_| 
       |[]      '|   | []  |`__  . [  \-\--|-|--/-/  
       |.   | |' |___|_____I___|___I___|---------| 
      / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] | 
     <===>  |   .|-=-=-=-=-=-=-=-=-=-=-|   |    / \  
     ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===> 
     ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [ 
     <===>     ' ||||| |   |   | ||||.||  []   <===>
      \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/ 
       |      . _||||| |   |   | ||||.|| |     | |
     ../|' v . | .|||||/____|____\|||| /|. . | . ./
     .|//\............/...........\........../../\\\



    =======================================================
    Destinée des Mondes Lointains
    =======================================================
    """

    print(CYAN +asciiart+ RESET)




# Charger la partie depuis le fichier JSON
def load_game():
    try:
        with open("save_game.json", "r") as file:
            saved_data = json.load(file)
            print("Partie chargée avec succès.")
            return saved_data
    except FileNotFoundError:
        print("Aucune sauvegarde trouvée.")
        return None


def save_to_json(player, filename="save_game.json"):
    data_to_save = {
        "name": player.name,
        "max_hp": player.max_hp,
        "hp": player.hp,
        "atk": player.atk,
        "defense": player.defense,
        # "position": historique_positions
    }

    with open(filename, "w") as file:
        json.dump(data_to_save, file)
        print(f"Les données ont été sauvegardées dans {filename}.")

# Demander au joueur de choisir son pseudo





main_menu()

# Demander au joueur de choisir une option
choice = input("Entrer votre choix: ")
nom = None
if choice == "1":
        print("Creation d'une nouvelle partie...")
        # Ajoutez ici le code pour créer une nouvelle partie
        nom = input("Choisissez votre pseudo :")
        player.name = nom
        print(f"Ravie de vous rencontrez {player.name}")
        time.sleep(0.3)
        save_to_json(player)
        introduction()
        # Utilisation de la fonction
        deplacer_joueur()

        # Sauvegarder la nouvelle partie
  
        
elif choice == "2":

        # Charger la partie existante
        saved_data = load_game()
        if saved_data:
            print(f"Partie chargée pour le joueur {saved_data[nom]}.")
            main_menu() 

elif choice == "3":
        print("Crédit")
        print("Réalisateur: Willy, Anthony, Imrane")
        print("Copyrigh 2024")
        main_menu()


elif choice == "4":
        print("Fermeture du jeu...")
        
else:
        print("Choix Invalide")
        main_menu()
        

def game_over():
    print("GAME OVER")
    saved_data = load_game()
    if saved_data:
        print(f"Partie chargée pour le joueur {saved_data[nom]}.")

