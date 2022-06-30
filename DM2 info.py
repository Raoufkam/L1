Exo1)

a)
n est de type entier, car on utilise le int qui définit les nombres entiers
b)
j est de type entier, car dans le programme on voit bien qu'on fait une égalité
entre j et n ( n est bien entier )
c)
i est de type liste , elle comporte les éléments entiers j donc i est une liste
d'entiers j
d)
li est de type liste , elle comporte liste d'entiers i
e)
occ est une variable de type int ( entier ), car on lui ajoute 1 qui est bien un
entier 
f)
Ce que le Programme devrait faire : Cherche a trouver le nombre de n dans la
liste li , la liste li est formée de liste i  qui contient des valeurs égale
à n , cette variable n elle prend la valeur dont on cherche le nombre d'apparitions
( nombre de n dans la liste li ) , la variable occ compte le nombre de n
il manque l'initialisation de la variable occ, donc on doit initialiser cette
variable au début de notre programme pour qu'il fonctionne
g)
Exemple Représentatif :
    On prend : li=[[4,8,9,2],[3,9,1,9]]
               n=9
               occ=0
    alors on aura dans i,j et occ :
             i=[4,8,9,2]
             j=4
             j=8
             j=9      #occ=occ+1 ( car la condition est vraie )
             j=2
             occ=1
             i=[3,9,1,9]
             j=3
             j=9      #occ=occ+1 ( car la condition est vraie )
             j=1
             j=9      #occ=occ+1 ( car la condition est vraie )
             occ=3
Exo2)

#initialisation de la liste :
liste=eval(input())
#initialisation du nombre :
nombre=int(input())
#initialisation de occurence_nombre:
occurence_nombre=0
#pour chaque élément de 'liste','liste2' prend tous les éléments de 'liste':
for liste2 in liste :
    #pour chaque élément de 'liste2' , 'verif' prend tous les éléments de 'liste2':
    for verif in liste2 :
        #Condition pour vérifier si 'verif' est égale à 'nombre' :
        if verif==nombre :
            #Ajouter 1 a chaque fois que la Condition est Vraie ( verif==nombre):
            occurence_nombre=occurence_nombre+1
#Afficher le résultat de 'occurence_nombre :
print(occurence_nombre)

Exo3)

#Programme qui calcul le nombre d’éléments divisibles par 5 de la variable 'li' :
liste=eval(input())
occurence_nombre=0
for liste2 in liste :
    for verif in liste2 :
        if verif%5==0 :
            occurence_nombre=occurence_nombre+1
print(occurence_nombre)





