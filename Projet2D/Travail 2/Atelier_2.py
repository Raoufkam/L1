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

def afficher_grille(grille):
    Alphabet=['A','B','C','D','E','F','G','H']
    print('       1       2       3       4       5       6       7       8')
    print("   ________________________________________________________________")
    n = 0
    while n<len(grille):
        print("   |       |       |       |       |       |       |       |       |")
        print(Alphabet[n]," |  ",grille[n][0],"  |  ",grille[n][1],"  |  ",grille[n][2],"  |  ",grille[n][3],"  |  ",grille[n][4],"  |  ",grille[n][5],"  |  ",grille[n][6],"  |  ",grille[n][7],"  |")
        print("   |_______|_______|_______|_______|_______|_______|_______|_______|")
        n=n+1
    return print("\n")


def remplir_grille_debut(grille):
    col=0
    lig=1
    grille[lig][col]="X"
    while col <= 7 :
        grille[lig][col]="X"
        if lig==2 :
            lig=lig-1
        else :
            lig=lig+1
        col=col+1
    col=0
    lig=5
    grille[lig][col]="O"
    while col<=7 :
        grille[lig][col]="O"
        if lig==6 :
            lig=lig-1
        else :
            lig=lig+1
        col=col+1
    return grille
def remplir_grille_milieu(grille):
    col=2
    lig=0
    grille[lig][col]="X"
    lig=2
    grille[lig][col]="X"
    col=0
    lig=0
    grille[lig][col]="X"
    col=5
    lig=1
    grille[lig][col]="X"
    col=7
    lig=2
    grille[lig][col]="X"
    col=7
    lig=0
    grille[lig][col]="X"
    col=0
    lig=2
    grille[lig][col]="X"
    col=3
    lig=1
    grille[lig][col]="X"
    col=4
    lig=4
    grille[lig][col]="O"
    col=0
    lig=5
    grille[lig][col]="O"
    col=7
    lig=6
    grille[lig][col]="O"
    col=5
    lig=3
    grille[lig][col]="O"
    col=0
    lig=4
    grille[lig][col]="O"
    col=3
    lig=6
    grille[lig][col]="O"
    col=1
    lig=7
    grille[lig][col]="O"
    col=5
    lig=6
    grille[lig][col]="O"
    return grille
def remplir_grille_fin(grille):
    col=2
    lig=0
    grille[lig][col]="X"
    lig=2
    grille[lig][col]="X"
    col=0
    lig=0
    grille[lig][col]="X"
    col=6
    lig=2
    grille[lig][col]="X"
    col=7
    lig=2
    grille[lig][col]="X"
    col=7
    lig=0
    grille[lig][col]="X"
    col=1
    lig=4
    grille[lig][col]="X"
    col=3
    lig=1
    grille[lig][col]="X"
    col=4
    lig=0
    grille[lig][col]="O"
    col=0
    lig=5
    grille[lig][col]="O"
    col=7
    lig=6
    grille[lig][col]="O"
    col=5
    lig=1
    grille[lig][col]="O"
    col=1
    lig=1
    grille[lig][col]="O"
    col=3
    lig=6
    grille[lig][col]="O"
    col=1
    lig=7
    grille[lig][col]="O"
    col=5
    lig=6
    grille[lig][col]="O"
    return grille
def saisi_du_joueur():
    Alphabet=['A','B','C','D','E','F','G','H']
    n=0
    ligne_1= input("Entrez ligne: ",)
    while ligne_1 not in Alphabet : 
        ligne_1 = input("Erreur !, Entrez ligne: ",)
        
    while n < len(Alphabet) :
        if ligne_1==Alphabet[n]:
            ligne_1=n
        n=n+1
    colonne_1= int(input("Entrez colonne: ",))
    colonne_1=colonne_1-1
    return (ligne_1,colonne_1)
  
def est_dans_grille(ligne_1,colonne_1,grille):
    if 0<=ligne_1<=7 and 0<=colonne_1<=7  :
        return True
    else :
        return False
afficher_grille(remplir_grille_debut(creation_grille()))
afficher_grille(remplir_grille_milieu(creation_grille()))
afficher_grille(remplir_grille_fin(creation_grille()))
ligne_1,colonne_1=saisi_du_joueur()
grille=creation_grille()
VAR=est_dans_grille(ligne_1,colonne_1,grille)
if VAR==True :
    print(" la case est dans la grille ")
else :
    print(" non valide ")