import os.path
import random
import pickle
from donnees import *

#fonction utilisateur pour retourner le nom du joueur

def utilisateur():
    nom=input("veuillez mentionnez votre nom de joueur : ")
    nom =nom.capitalize()
    if len(nom) < 4 or not nom.isalnum() :
        print("votre nom doit contenir minimun 4 caratere alphanumerique ")
        return utilisateur()
    else:
        return nom
# fonction qui permet de retourner un  mot au hazard dans la liste de mot
def choisir_mot():
    selectionne = random.choice(mot)

    return selectionne
# fonction qui permet de recuper l enregitrement du score d'un joueur dans un fichier
def recup_score_enregistrer():

    if os.path.exists(sauvegarde): # Le fichier existe
        # On le récupère
        fichier_scores = open(sauvegarde, "rb")
        mon_depickler = pickle.Unpickler(fichier_scores)
        scores = mon_depickler.load()
        fichier_scores.close()
    else: # Le fichier n'existe pas
        scores = {}
    return scores
# fonction qui permet de enregistrer un score dans un fichier
def score_enregistrer(scores):

    fichier_scores = open(sauvegarde, "wb") # On écrase les anciens scores
    mon_pickler = pickle.Pickler(fichier_scores)
    mon_pickler.dump(scores)
    fichier_scores.close()



    #fonction qui permet de saisir une lettre a trouver dans un mot de la liste
def get_caractere():
     lettre = input("saisissez une lettre : ").lower()
     if len(lettre)>1 or not lettre.isalpha():
         print("saisissez qu'une seule lettre s'il vous plais ")
         return get_caractere()
     else:
      return lettre


 #fonction qui retourne la lettre quand c est correct ou decrimente le nombre de tour quand la lettre est incorrect

def test_caractere(mot_complet, lettre_trouve):
    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettre_trouve:
            mot_masque += lettre
        else:
            mot_masque += "*"
    return mot_masque