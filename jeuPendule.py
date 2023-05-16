import os
import pickle
from fonctions import *
import  donnees

scores = recup_score_enregistrer()
nom = utilisateur()
if nom not in scores.keys():
    scores[nom]=0
"""sexe=input("veuillez renseignez votre sexe s'il vous plait :")
if sexe.lower()=='masculin' or sexe.lower()=='homme' or sexe.lower() == 'm':
     print(" bien venue dans cette nouvelle partie de jeu du pendu mme. {}.".format(nom))
elif sexe.lower()=='feminin' or sexe.lower()=='femme' or sexe.lower() == 'f':
     print(" bien venue dans cette nouvelle partie de jeu du pendu mme. {}.".format(nom))
else:
    print("bienvenue extra-terrestre au yeux du pendu ")
"""
jouer ='o'
while jouer !="n":
    print(" joueur {} a un score de {} :".format(nom,scores[nom]))
    mot_complet = choisir_mot()
    lettre_trouve = []
    mot_rech = test_caractere(mot_complet, lettre_trouve)
    nbre_chance = tour
    while mot_complet != mot_rech and nbre_chance > 0:
        print("le mot est {0} il vous reste {1} chances  ".format(mot_rech, nbre_chance))
        lettre = get_caractere()
        if lettre in lettre_trouve:
            print("vous avez deja trouver ce mot ,veuillez reessayer")
        elif lettre in mot_complet :
            lettre_trouve.append(lettre)
            print("mot trouves, bien jouer {}. ".format(nom))
        else:
            nbre_chance -= 1
            print("le mot ne se trouve pas dans le mot final pas de chance")
        mot_rech =test_caractere(mot_complet, lettre_trouve)
    if mot_complet == mot_rech:
        print("felicitation {} vous avez trouvez le mot qui est : {}".format(nom, mot_complet))
    else:
        print("bye {} vous avez perdu ".format(nom))

    scores[nom] += nbre_chance

    jouer =input("voulez vous continuez la partie O/N :").lower()

    print("nouvelle partie de jeu")

score_enregistrer(scores)
print("vous terminer la partie avec {} point".format(scores[nom]))


os.system("pause")