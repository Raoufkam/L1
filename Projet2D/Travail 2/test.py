def saisi_du_joueur():
    Alphabet=['A','B','C','D','E','F','G','H']
    n=0
    ligne_1= input("Entrez ligne: ",)
    colonne_1= int(input("Entrez colonne: ",))
    colonne_1=colonne_1-1
    while n < len(Alphabet) :
        if ligne_1==Alphabet[n]:
            ligne_1=n
        n=n+1
    return(ligne_1,colonne_1)
    
ligne_1,colonne_1=saisi_du_joueur()
