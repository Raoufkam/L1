# -- coding: utf-8 --

def creation_grille():
    grille = []
    nb_colonnes = 8  # nombre de colonnes
    nb_lignes = 8  # nombre de lignes
    valeur = " "  # valeur de depart
    for ligne in range(nb_lignes):
      grille.append([])
      for colonne in range(nb_colonnes):
        grille[ligne].append(valeur)
    return grille

def affichergrille(grille):
    Alphabet=['A','B','C','D','E','F','G','H']
    print('       1       2       3       4       5       6       7       8')
    print("   __")
    n = 0
    while n<len(grille):
        print("   |       |       |       |       |       |       |       |       |")
        print(Alphabet[n]," |  ",grille[n][0],"  |  ",grille[n][1],"  |  ",grille[n][2],"  |  ",grille[n][3],"  |  ",grille[n][4],"  |  ",grille[n][5],"  |  ",grille[n][6],"  |  ",grille[n][7],"  |")
        print("   |__|__|__|__|__|__|__|___|")
        n=n+1
    return print("\n")


def remplir_grille_debut(grille):
    grille[0][0] = "1"
    grille[7][7] = 1
    #TODO
    #....
    return grille

def saisi_du_joueur():
    ligne_et_colonne = input("Entrez les.... : ")
    ligne_et_colonne_destination = input("Entrez les... : ")

    return ligne,colonne,ligne_de_destination, colonne_de_destination

afficher_grille(remplir_grille_debut(creation_grille()))

saisi_du_joueur()
