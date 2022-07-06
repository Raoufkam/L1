def appartient(n,liste) :

    for element in liste : 

        for i in element : 

            if i==n :

                return True

    return False

liste = eval(input())

nombre = int(input())

if(not(appartient(nombre,liste))) :
    print("Non ce nombre n'appartient pas a la liste ")
else :
    print("Oui ce nombre est bien present dans la liste !")
