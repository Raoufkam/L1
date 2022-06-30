# On import numpy qui est une librairie contenant array permettant de créer une grille avec des listes
from numpy import *
from test import *

def choisir_case(ligne, colonne, grille, joueur):
  #On verifie si la case est dans la grille
  if est_dans_grille (ligne, colonne, grille):
	#Puis si elle appartient au joueur courant
    if appartient_joueur (ligne, colonne, grille, joueur):
	    print('(', ligne, ',', colonne, ')')
	    ligne = changement_lettre_en_chiffre(ligne)
	    return int(ligne), int(colonne)
  # si la case n'est pas dans la grille ou n'appartient pas au joueur courant on redemande des coordonnées
  print('Mauvaise saisie ou non valide,')
    return (choisir_case(input('Veuillez donner la ligne du pion que
    vous souhaitez sélectionner (A à I, en majuscule) :'),
    input('Veuillez donner la colonne du pion que vous souhaitez
    sélectionner (1 à 9) :'), grille, joueur))

def changement_lettre_en_chiffre(ligne):
  if ligne == 'A':
    return '1'
  if ligne == 'B':
    return '2'
  if ligne == 'C':
    return '3'
  if ligne == 'D':
    return '4'
  if ligne == 'E':
    return '5'
  if ligne == 'F':
    return '6'
  if ligne == 'G':
    return '7'
  if ligne == 'H':
    return '8'
  if ligne == 'I':
    return '9'
  return '0'

def validation_ligne(ligne, grille):
  # On transforme la ligne en chiffre pour localiser plus facilement son emplacement
  ligne = changement_lettre_en_chiffre(ligne)
  # On vérifie si la ligne est bien dans l'intervalle 1 à 9 (première liste de grille) mais on retire l'espace
  return (bool ((ligne in grille[0]) and (ligne!=grille[0][0])))
  
def validation_colonne(colonne, grille):
  # On vérifie si la colonne est bien dans l'intervalle 1 à 9 (première liste de grille) mais on retire l'espace
  return (bool ((colonne in grille[0]) and (colonne!=grille[0][0])))

def appartient_joueur(ligne, colonne, grille, joueur):
	ligne = changement_lettre_en_chiffre(ligne)
	if grille[int(ligne)][int(colonne)] == joueur:
		return True
	return False

def est_dans_grille(ligne, colonne, grille):
  if not(validation_ligne(ligne, grille) and validation_colonne(colonne, grille)):
    return False
  else:
    return True

def affichage(grille, total_pion_joueur_X, total_pion_joueur_O):
  print (grille)
  print ("Joueur X :", total_pion_joueur_X, "pions")
  print ("Joueur O :", total_pion_joueur_O, 'pions')

def debut_de_partie():
  # On initialise les différentes variables nécessaire pour la partie (la grille, les pions de joueur 1 et 2)
  return (array([[' ',1,2,3,4,5,6,7,8,9],['A','x','x','x','x','x','x','x','x','x'],['B','x','x','x','x','x','x','x','x','x'],['C','x','x','x','x','x','x','x','x','x'],['D',' ',' ',' ',' ',' ',' ',' ',' ',' '],['E',' ',' ',' ',' ',' ',' ',' ',' ',' '],['F',' ',' ',' ',' ',' ',' ',' ',' ',' '],['G','o','o','o','o','o','o','o','o','o'],['H','o','o','o','o','o','o','o','o','o'],['I','o','o','o','o','o','o','o','o','o']]), 27, 27)

def milieu_de_partie():
  # On donne un exemple de variables possibles en milieu de partie
  return (array([[' ',1,2,3,4,5,6,7,8,9],['A','x','x','x','x','x',' ','x','x','x'],['B','x','o',' ','x',' ',' ','x','x',' '],['C','x','o',' ',' ',' ',' ',' ',' ',' '],['D',' ',' ','o',' ',' ',' ',' ',' ',' '],['E',' ',' ',' ',' ',' ',' ',' ',' ',' '],['F',' ','x',' ',' ',' ',' ',' ',' ',' '],['G','x',' ',' ',' ',' ',' ',' ',' ',' '],['H',' ',' ',' ',' ','o','o','o','o','o'],['I','o','o','o','o','o','o','o','o','o']]), 15, 17)

def Avant_fin_de_partie():
  # On donne un exemple de variables qques coups avant la fin de la partie 
  return (array([[' ',1,2,3,4,5,6,7,8,9],['A','x',' ',' ',' ',' ',' ',' ','x','x'],['B','x',' ','x',' ',' ',' ',' ',' ',' '],['C',' ',' ','o',' ',' ',' ',' ',' ','o'],['D',' ',' ','o',' ',' ',' ',' ',' ','o'],['E',' ','o',' ',' ',' ',' ',' ',' ',' '],['F',' ',' ',' ',' ',' ',' ',' ','o','o'],['G',' ',' ',' ','x','x',' ',' ',' ',' '],['H',' ',' ',' ',' ',' ',' ',' ',' ',' '],['I','o','o',' ',' ',' ',' ',' ',' ','o']]), 7, 10)

def choix_moment_partie (moment) :
	if moment == 'debut' :
		return debut_de_partie()
	if moment == 'milieu' :
		return milieu_de_partie()
	if moment == 'fin' :
		return Avant_fin_de_partie()
	print('mauvaise saisie, ')	
	return choix_moment_partie (input('à quel moment voulez vous jouer votre tour de jeu ? (debut, milieu, fin) :'))

def choix_deplacement (deplacement):
	if (deplacement != 'retournement') and (deplacement != 'elimination') and (deplacement != 'passer') :
		print ('mauvaise saisie, ')
		return choix_deplacement(input('quel deplacement voulez vous effectuer ? (retournement, elimination, passer) :'))	
	return deplacement

def a_qui_de_jouer (joueur):
	#si c'est le premier tour ou que c'était au joueur O de jouer c'est au joueur X
	if joueur==0 or joueur=='o':
		return 'x'
	#sinon c'est au joueur O de jouer
	return 'o'

	
	
def retournement (joueur, ligne_depart, colonne_depart, grille, total_pion_joueur_X, total_pion_joueur_O, recommencement):
	#On demande les coordonnées de la case que le joueur souhaite eliminé
	#On va utiliser la fonction a_qui_de_jouer pour que la case appartiennent bien au joueur adverse
	ligne_arrivee, colonne_arrivee = choisir_case(input('Veuillez donner la ligne du pion que vous souhaitez retourner (A à I, en majuscule) :'), input('Veuillez donner la colonne du pion que vous souhaitez retourner (1 à 9) :'), grille, a_qui_de_jouer (joueur))
	#On verifie si la case se trouve dans une trajectoire du pion selectionné et si il n'y a pas de pion entre les deux pions
	if validation_case_prenable(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
		#On verifie si la case suivante est vide 
		if case_apres_vide(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
			#On modifie la grille avec le deplacement effectué et on crée le nouveau depart si le joueur souhaite continuer son retournement
			grille, ligne_depart, colonne_depart = changement_grille_retournement(grille, joueur, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee)
			#On modifie les totals de pions des joueurs
			total_pion_joueur_X, total_pion_joueur_O = modification_pion_retournement(joueur, total_pion_joueur_X, total_pion_joueur_O)
			print(grille)
			print('vous etes en :', (ligne_depart, colonne_depart))
			if continuer_retournement(input('voulez vous faire un nouveau retournement ? (oui ou non) :')) :
				#Si le joueur souhaite continuer son  retournement on lui redonne la grille et son nouveau positionnement
				return retournement (joueur, ligne_depart, colonne_depart, grille, total_pion_joueur_X, total_pion_joueur_O, 1)
			#Sinon on s'arrete là
			return (total_pion_joueur_X, total_pion_joueur_O, grille)	
	#sinon on relance un tour de jeu pour permettre au joueur de modifier ses saisis ou on relance un retournement si c'est son deuxieme retournement et plus 
	if recommencement == 1 :
		print('ce pion ne peut pas etre retourner par le pion selectionné, nous recommencerons à partir de la fin du dernier retournement')
		if continuer_retournement(input('voulez vous faire un nouveau retournement ? (oui ou non) :')) :
				#Si le joueur souhaite continuer son  retournement on lui redonne la grille et son nouveau positionnement
			print(grille)
			print('vous etes en :', (ligne_depart, colonne_depart))
			return retournement (joueur, ligne_depart, colonne_depart, grille, total_pion_joueur_X, total_pion_joueur_O, 1)
		#Sinon on s'arrete là
		return (total_pion_joueur_X, total_pion_joueur_O, grille)
	print('ce pion ne peut pas etre retourner par le pion selectionné, veuillez recommencer vos selections') 
	return tour_de_jeu(joueur, total_pion_joueur_X, total_pion_joueur_O, grille)	

def case_apres_vide(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
	#ligne
	if ligne_depart == ligne_arrivee :
		if min(ligne_depart, ligne_arrivee) == ligne_depart :
			if grille[ligne_arrivee][colonne_arrivee+1] != ' ' :
				return False
		else:
			if grille[ligne_arrivee][colonne_arrivee-1] != ' ' :
				return False
		return True
	#colonne
	if colonne_depart == colonne_arrivee :
		if min(colonne_depart, colonne_arrivee) == colonne_depart :
			if grille[ligne_arrivee+1][colonne_arrivee] != ' ' :
				return False
		else:
			if grille[ligne_arrivee-1][colonne_arrivee] != ' ' :
				return False
		return True
	#diagonale
	if abs((ligne_depart)-(ligne_arrivee)) == abs((colonne_depart)-(colonne_arrivee)) :
		return case_vide_diagonale(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille)
	
def case_vide_diagonale(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
	#En haut à gauche
	if (colonne_arrivee < colonne_depart) and (ligne_arrivee < ligne_depart) :
		if grille[ligne_arrivee-1][colonne_arrivee-1] != ' ' :
			return False 
		return True
	#En haut à droite
	if (colonne_arrivee > colonne_depart) and (ligne_arrivee < ligne_depart) :
		if grille[ligne_arrivee-1][colonne_arrivee+1] != ' ' :
			return False
		return True
	#En bas à gauche
	if (colonne_arrivee < colonne_depart) and (ligne_arrivee > ligne_depart) :
		if grille[ligne_arrivee+1][colonne_arrivee-1] != ' ' :
			return False 
		return True
	#En bas à droite
	if (colonne_arrivee > colonne_depart) and (ligne_arrivee > ligne_depart) :
		if grille[ligne_arrivee+1][colonne_arrivee+1] != ' ' :
			return False 
		return True

def modification_pion_retournement(joueur, total_pion_joueur_X, total_pion_joueur_O) :
	if joueur == 'x':
		total_pion_joueur_O = total_pion_joueur_O-1
		total_pion_joueur_X = total_pion_joueur_X+1
	else :
		total_pion_joueur_X = total_pion_joueur_X-1
		total_pion_joueur_O = total_pion_joueur_O+1
		
	return total_pion_joueur_X, total_pion_joueur_O
	
def continuer_retournement(decision) :
	if decision == 'oui' :
		return True 
	if decision == 'non' :
		return False
	print('mauvaise saisie,')
	return continuer_retournement(input('voulez vous faire un nouveau retournement ? (oui ou non) :'))
	
def changement_grille_retournement(grille, joueur, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee):
	#On remplace le pion éliminé par un pion du joueur courant et on remplace la case initiale par une case vide
	grille[ligne_depart][colonne_depart] = ' '
	grille[ligne_arrivee][colonne_arrivee] = joueur
	#puis la case suivante par un pion du joueur
	if ligne_depart == ligne_arrivee :
		if min(ligne_depart, ligne_arrivee) == ligne_depart :
			grille[ligne_arrivee][colonne_arrivee+1] = joueur 
			return (grille, ligne_arrivee, (colonne_arrivee+1))
		grille[ligne_arrivee][colonne_arrivee-1] = joueur
		return (grille, ligne_arrivee, (colonne_arrivee-1))
	if colonne_depart == colonne_arrivee :
		if min(colonne_depart, colonne_arrivee) == colonne_depart :
			grille[ligne_arrivee+1][colonne_arrivee] = joueur
			return (grille, ligne_arrivee+1, (colonne_arrivee))
		grille[ligne_arrivee-1][colonne_arrivee] = joueur
		return (grille, (ligne_arrivee-1), colonne_arrivee)
	if abs((ligne_depart)-(ligne_arrivee)) == abs((colonne_depart)-(colonne_arrivee)) :
		return changement_grille_diagonale_retournement(grille, joueur, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee)

def changement_grille_diagonale_retournement(grille, joueur, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee):
	#On modifie selon la diagonale
	#En haut à gauche
	if (colonne_arrivee < colonne_depart) and (ligne_arrivee < ligne_depart) :
		grille[ligne_arrivee-1][colonne_arrivee-1] = joueur 
		return (grille, (ligne_arrivee-1), (colonne_arrivee-1))
	#En haut à droite
	if (colonne_arrivee > colonne_depart) and (ligne_arrivee < ligne_depart) :
		grille[ligne_arrivee-1][colonne_arrivee+1] = joueur 
		return (grille, (ligne_arrivee-1), (colonne_arrivee+1))
	#En bas à gauche
	if (colonne_arrivee < colonne_depart) and (ligne_arrivee > ligne_depart) :
		grille[ligne_arrivee+1][colonne_arrivee-1] = joueur 
		return (grille, (ligne_arrivee+1), (colonne_arrivee-1))
	#En bas à droite
	if (colonne_arrivee > colonne_depart) and (ligne_arrivee > ligne_depart) :
		grille[ligne_arrivee+1][colonne_arrivee+1] = joueur 
		return (grille, (ligne_arrivee+1), (colonne_arrivee+1))


	
def elimination (joueur, ligne_depart, colonne_depart, grille, total_pion_joueur_X, total_pion_joueur_O):
	#On demande les coordonnées de la case que le joueur souhaite eliminé
	#On va utiliser la fonction a_qui_de_jouer pour que la case appartiennent bien au joueur adverse
	ligne_arrivee, colonne_arrivee = choisir_case(input('Veuillez donner la ligne du pion que vous souhaitez éliminer (A à I, en majuscule) :'), input('Veuillez donner la colonne du pion que vous souhaitez éliminer (1 à 9) :'), grille, a_qui_de_jouer (joueur))
	#Si la case à prendre se trouve à coté il faut recommencer
	if case_a_cote(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee):
		print('ce pion ne peut pas etre eliminé par le pion selectionné car il se trouve juste à coté, veuillez recommencer vos selections') 
		return tour_de_jeu(joueur, total_pion_joueur_X, total_pion_joueur_O, grille)
	#On verifie si la case se trouve dans une trajectoire du pion selectionné et si il n'y a pas de pion entre les deux pions
	if validation_case_prenable(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
		#On modifie la grille avec le deplacement effectué
		grille = changement_grille_elimination(grille, joueur, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee)
		#On modifie les totals de pions des joueurs
		total_pion_joueur_X, total_pion_joueur_O = modification_pion_elimination (joueur, total_pion_joueur_X, total_pion_joueur_O)
		return (total_pion_joueur_X, total_pion_joueur_O, grille)
	#sinon on relance un tour de jeu pour permettre au joueur de modifier ses saisis
	print('ce pion ne peut pas etre eliminer par le pion selectionné, veuillez recommencer vos selections') 
	return tour_de_jeu(joueur, total_pion_joueur_X, total_pion_joueur_O, grille)

def modification_pion_elimination (joueur, total_pion_joueur_X, total_pion_joueur_O):
	if joueur == 'x':
		total_pion_joueur_O = total_pion_joueur_O-1
	else :
		total_pion_joueur_X = total_pion_joueur_X-1
		
	return total_pion_joueur_X, total_pion_joueur_O
	
def changement_grille_elimination(grille, joueur, ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee):
	#On remplace le pion éliminé par un pion du joueur courant et on remplace la case initiale par une case vide
	grille[ligne_depart][colonne_depart] = ' '
	grille[ligne_arrivee][colonne_arrivee] = joueur
	return grille
	
def case_a_cote(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee):
	#Si la case est juste à gauche ou à droite elle ne peut pas etre prise
	if ((colonne_arrivee == colonne_depart+1) and (ligne_arrivee == ligne_depart))  or ((colonne_arrivee == colonne_depart-1) and (ligne_arrivee == ligne_depart)) :
		return True 
	#Si la case est juste en dessous ou au dessus elle ne peut pas etre prise
	if ((ligne_arrivee == ligne_depart+1) and (colonne_arrivee == colonne_depart)) or ((ligne_arrivee == ligne_depart-1) and (colonne_arrivee == colonne_depart)) :
		return True 
	#Puis si elle se trouve sur les diagonales à cotés elle ne peut pas etre prise non plus
	if ((ligne_arrivee == ligne_depart+1) and (colonne_arrivee == colonne_depart+1)) or ((ligne_arrivee == ligne_depart-1) and (colonne_arrivee == colonne_depart-1)) :
		return True
	if ((ligne_arrivee == ligne_depart+1) and (colonne_arrivee == colonne_depart-1)) or ((ligne_arrivee == ligne_depart-1) and (colonne_arrivee == colonne_depart+1)) :
		return True
	#Sinon elle n'est pas à coté on peut passer aux autres verifications
	return False

	

def validation_case_prenable(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
	#soit il est sur la meme ligne ou meme colonne et qu'il n'y a pas de pion entre les deux
	if ligne_depart == ligne_arrivee :
		if pas_de_pion_entre_ligne(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
			return True
	if colonne_depart == colonne_arrivee :
		if pas_de_pion_entre_colonne(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
			return True
	#soit il est sur sa diagonale et qu'il n'y a pas de pion entre les deux
	if abs((ligne_depart)-(ligne_arrivee)) == abs((colonne_depart)-(colonne_arrivee)) :
		if pas_de_pion_entre_diagonale(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille):
			return True
	#sinon il n'est pas prenable
	return False

def pas_de_pion_entre_ligne(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
	#On regarde si il n'y a aucun pion entre la case choisi et la case à prendre sur la ligne
	for i in range (min(colonne_depart, colonne_arrivee)+1, max(colonne_depart, colonne_arrivee)):
		if grille[ligne_depart][i] != ' ' :
		  return False
	return True
	
def pas_de_pion_entre_colonne(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
	#On regarde si il n'y a aucun pion entre la case choisi et la case à prendre sur la colonne
	for i in range (min(ligne_depart, ligne_arrivee)+1, max(ligne_depart, ligne_arrivee)):
		if grille[i][colonne_depart] != ' ' :
			return False
	return True

def pas_de_pion_entre_diagonale(ligne_depart, colonne_depart, ligne_arrivee, colonne_arrivee, grille) :
	augmentation_de_la_colonne = 0
	#On regarde si il n'y a aucun pion entre la case choisi et la case à prendre sur la colonne
	ligne_min = min(ligne_depart, ligne_arrivee)
	#On inverse la colonne de depart selon la plus petite ligne pour ne faire que descendre
	if ligne_min == ligne_arrivee :
		colonne_depart = colonne_arrivee
		colonne_arrivee = colonne_depart
	#On choisi l'incrementation qui va bien selon le coté vers lequel on descent
	if (colonne_depart < colonne_arrivee) :
	  augmentation_de_la_colonne=1
	else :
	  augmentation_de_la_colonne=(-1)
	colonne = colonne_depart + augmentation_de_la_colonne
	for i in range (ligne_min+1, max(ligne_depart, ligne_arrivee)):
		if grille[i][colonne] != ' ' :
			return False
		colonne = colonne + augmentation_de_la_colonne
	return True
	

	
def tour_de_jeu (joueur, total_pion_joueur_X, total_pion_joueur_O, grille) :
	#On demande le deplacement que le joueur courant souhaite effectuer
	deplacement = choix_deplacement(input('quel deplacement voulez vous effectuer ? (retournement, elimination, passer) :'))
	if deplacement != 'passer' :
		#Si le joueur ne souhaite pas passer alors on lui demande de selectionner un pion de depart lui appartenant
		ligne_depart, colonne_depart = choisir_case(input('Veuillez donner la ligne du pion que vous souhaitez sélectionner (A à I, en majuscule) :'), input('Veuillez donner la colonne du pion que vous souhaitez sélectionner (1 à 9) :'), grille, joueur)
		if deplacement == 'elimination':
			return elimination(joueur, ligne_depart, colonne_depart, grille, total_pion_joueur_X, total_pion_joueur_O)
		return retournement(joueur, ligne_depart, colonne_depart, grille, total_pion_joueur_X, total_pion_joueur_O, 0)
	return (total_pion_joueur_X, total_pion_joueur_O, grille)

def partie_finie (total_pion_joueur_X, total_pion_joueur_O):
	if (total_pion_joueur_X < 6) :
		print ('joueur x a gagné la partie !')
		return 2
	if (total_pion_joueur_O < 6) :
		print ('joueur o a gagné la partie !')
		return 1
	return 0
	

# On initialise toute les variables
joueur=0
total_pion_joueur_X=27
total_pion_joueur_O=27
grille=0

# On demande de choisir un moment de la partie à partir du quel le joueur veut réaliser son coup 
grille, total_pion_joueur_X, total_pion_joueur_O = choix_moment_partie (input('à quel moment voulez vous jouer votre tour de jeu ? (debut, milieu, fin) :'))

# On affiche aux joueurs les variables initiales qui leur sont nécessaires
affichage(grille, total_pion_joueur_X, total_pion_joueur_O)

# On annonce le joueur courant
joueur = a_qui_de_jouer(joueur)
print('c est au joueur', joueur, 'de jouer')

#On realise un tour de jeu
total_pion_joueur_X, total_pion_joueur_O, grille = tour_de_jeu (joueur, total_pion_joueur_X, total_pion_joueur_O, grille)

#On réaffiche les totaux de pions et la grille 
affichage(grille, total_pion_joueur_X, total_pion_joueur_O)

# On verifie si la partie ets finie et si oui qui a gagné
victoire = partie_finie(total_pion_joueur_X, total_pion_joueur_O)





























