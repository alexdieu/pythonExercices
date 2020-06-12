# Une liste est une séquence modiﬁable : on peut changer ses elements, lui en ajouter et lui en enlever

# On construit une liste en ecrivant ses elements, separes par des virgules, encadres par les crochets.
# La liste vide se note [ ]

# liste[indice] --> designation de l’element de rang indice de la liste
# liste[indice] -->  expression remplacement de l’element de liste ayant l’indice indique
# liste1 + liste2 --> concatenation (mise bout a bout ) de deux listes
# liste.append(element) --> ajout d’un element a la ﬁn d’une liste
# liste.insert(indice, element) --> insertion d’un element a l’emplacement de liste indique par l’indice donne
# element in liste --> test d’appartenance : element ∈ liste ?
# for element in liste -->  parcours s´equentiel

#  Attention : Il y a  deux manieres d'ajouter un element  a la ﬁn d’une liste
# liste + [ element ] ne modiﬁe pas liste, mais renvoie une nouvelle liste comme resultat
# liste.append(element) modiﬁe liste et ne renvoie pas de resultat.

# range([start], stop[, step]) -->
# start: Starting number of the sequence.
# stop: Generate numbers up to, but not including this number.
# step: Difference between each number in the sequence.

# trouver les nombres premiers

borne = 25
premiers = [ ]
r = range(3, borne + 1, 2)

for candidat in r :
    estPremier = True
    for premier in premiers:
        if candidat % premier == 0:
            estPremier = False
            break
    if estPremier:
        premiers.append(candidat)

print ("candidats= "+str(list(r)))
print ("premiers ="+str(premiers))

