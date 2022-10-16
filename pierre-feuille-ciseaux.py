import time 
from random import randint
import os

os.system("cls")

while True:
    print("----------------------------\n|  Pierre Feuille Ciseaux  |\n----------------------------")

    item_user = str(input("\nEntrez le mot que vous choisissez (en minuscule) > "))
    item_ordi = randint(1,3)

    if item_user == "pierre":
        item_user = 1
    elif item_user == "feuille":
        item_user = 2
    elif item_user == "ciseaux":
        item_user = 3
    else:
        print("\nLe mot est mal orthographié")
        input("\nAppuyer sur entrée pour recommencer")
        os.system("cls")
        break

    if item_ordi == 1:
        answer_item_ordi = "pierre"
    elif item_ordi == 2:
        answer_item_ordi = "feuille"
    elif item_ordi == 3:
        answer_item_ordi = "ciseaux"

    print("\n3")
    time.sleep(1)

    print("\n2")
    time.sleep(1)

    print("\n1")
    time.sleep(1)

    if item_ordi == 1 and item_user == 1:
        print("\nEgalité, c'est sérré dis donc !")
    elif item_ordi == 1 and item_user == 2:
        print("\nOn dirai que l'utilisateur a gagné !")
    elif item_ordi == 1 and item_user == 3:
        print("\nOn dirai que l'ordi a gagné !")

    elif item_ordi == 2 and item_user == 1:
        print("\nOn dirai que l'ordi a gagné !")
    elif item_ordi == 2 and item_user == 2:
        print("\nEgalité, c'est sérré dis donc !")
    elif item_ordi == 2 and item_user == 3:
        print("\nOn dirai que l'utilisateur a gagné !")

    elif item_ordi == 3 and item_user == 1:
        print("\nOn dirai que l'utilisateur a gagné !")
    elif item_ordi == 3 and item_user == 2:
        print("\nOn dirai que l'ordi a gagné !")
    elif item_ordi == 3 and item_user == 3:
        print("\nEgalité, c'est sérré dis donc !")

    print(f"\nL'ordi avait choisi {answer_item_ordi}")
    input("\n\nAppuyez sur entrée pour recommencer > ")
    os.system("cls")
    break