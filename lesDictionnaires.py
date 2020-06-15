# Un dictionnaire est une collection de couples (cle, valeur)
# il n’y a pas deux couples ayant la meme cle
# la recherche d’une valeur a partir de la cle correspondante soit extremement eﬃcace.

#  expression d'un dictionnaire : { cle1 : valeur1 , cle2 : valeur2 , ... clek : valeurk }


# dict[cle] = valeur ajoute au dictionnaire dict une paire (cle, valeur) ou, si une telle paire existait deja, modiﬁe sa partie valeur,
# dict[cle] renvoie la valeur correspondant a la cle donnee; une erreur est declenchee si une telle cle n’existe pas dans le dictionnaire,
# cle in dict : true si la cle appartient au dictionnaire
# dict.get(cle ,valsinon) renvoie la valeur correspondant a la cle donnee;si une telle cle est absente, renvoie valsinon ou (si valsinon est omise) None,
# del dict[cle] supprime du dictionnaire dict la paire (cle, valeur),
# dict.keys() renvoie une copie de la liste des cles du dictionnaire dict,
# dict.values() renvoie une copie de la liste des valeurs du dictionnaire dict,
# dict.items() renvoie une copie de la liste des associations constituant le dictionnaire dict.

texte = """Maitre Corbeau, sur un arbre perche Tenait en son bec un fromage Maitre Renard, par l’odeur alleche lui tint a peu pres ce langage"""

dict = { }
for car in texte:
    if car in dict:
         dict[car] = dict[car]+1
    else:
         dict[car] = 1

for car in dict.keys():
    print (car + ": "+str(dict[car])+" occurrence(s)")