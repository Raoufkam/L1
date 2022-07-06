#Programme qui calcul le nombre d’éléments divisibles par 5 de la variable 'li' :
print("Faite entrer votre liste de nombres : ")
liste =eval(input("Entrez votre liste : "))
occurence_nombre=0
for elem in liste :
    if elem%5==0 :
        print("le nombre :",elem,"est divisible par 5")
        occurence_nombre=occurence_nombre+1
print("Le nombre d'occurence des nombres divisble par 5 est : ",occurence_nombre)
