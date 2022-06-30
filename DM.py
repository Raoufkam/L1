#print l'âge
age=int(input())
#le salaire
slr=int(input())
#le statut
stat=input()
#handicap
handi=input()
#la fonction qui renvoie le message ...financement
def financement(age,salaire,statut,handicap):
    if age<18 and statut!="emancipe" :
        x="Financement autorise percu par les parents du candidat"
    elif (age>=18 and salaire<1500 )or ( age >=18 and handicap=="oui" ):
        x="Financement autorise percu par le candidat "
    elif statut=="incapable":
        x="Pas de droit de financement"
    return(x)
financement(age,slr,stat,handi)
