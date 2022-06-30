def appartient(n,liste) :

    for element in liste : 

        for i in element : 

            if i==n :

                return True
        return False

liste = eval(input())

nombre = int(input())

print(appartient(nombre,liste))