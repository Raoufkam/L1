# -*- coding: utf-8 -*-

def afficher_grille():
    grille=[]
    nb_colonnes=8 #nombre de colonnes 
    nb_lignes=8 #nombre de lignes 
    valeur=" " #valeur de depart 
    n=0
#construction de la grille de depart 

    for ligne in range(nb_lignes):
      grille.append([])
      for colonne in range(nb_colonnes):
        grille[ligne].append(valeur)
    #sortie de grille for element in grille :
    grille[1][0]="x"
    lig=2
    col=1
    while col<=7:
        grille[lig][col]="x"
        if lig==2 :
            lig=lig-1
        else :
            lig=lig+1
        col=col+1
    Alphabet=['A  ','B  ','C  ','D  ','E   ','F   ','G  ','H  ']
    print('         1         2         3         4         5         6        7      8')
    print("      _________________________________________")
    while n<len(Alphabet):
          print(Alphabet[n],"|__",grille[n][0],"__ |__",grille[n][1],"__|__",grille[n][2],"__|__",grille[n][3],"__|__",grille[n][4],"__|__",grille[n][5],"__|__",grille[n][6],"__|__",grille[n][7],"__|")
          n=n+1

afficher_grille()
        
            
