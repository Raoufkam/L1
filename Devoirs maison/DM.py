print("Veuillez entrez votre age : ")
age=int(input())
print("Veuillez entrez votre salaire :")
slr=int(input())
print("Veuillez entrez votre statut :")
stat=input() # Les status sont : "incapable" ; "emancipe"
print("Etes vous handicap ? oui / non : ")
handi=input() #La réponse dois être sois : "oui" ; "non"

#*
# la fonction 'financement()' qui renvoie le message si le financement est autirise pour le condidature passe en parametre ou pas .
#*

def financement(age,salaire,statut,handicap):

    if age<18 and statut!="emancipe" :
        x="Financement autorise percu par les parents du candidat"
    if statut=="emancipe" and age < 18 :
        x="Financement autorise percu par le candidat"
    elif (age>=18 and salaire<1500 )or ( age >=18 and handicap=="oui" ):
        x="Financement autorise percu par le candidat "
    elif statut=="incapable":
        x="Pas de droit de financement"
    else :
        x = "Une erreur est produite lors du passage de vos informations , veuillez reessayer !"
    return(x)
print("\n"+financement(age,slr,stat,handi))
