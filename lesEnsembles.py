# Les ensembles sont des structures de donnees avec les caracteristiques suivantes :
# – il n’y a pas d’acces indexe aux elements, ni d’ordre entre ces derniers,
# – il n’y a pas de repetition des elements : un element appartient ou non a un ensemble, mais cela n’a pas de sens de se demander s’il s’y trouve plusieurs fois,
# – en contrepartie, le test d’appartenance est optimise : le necessaire est fait pour que le test element ∈ ensemble ?(en Python : element in ensemble) puisse etre evalue de maniere extremement eﬃcace.


# On construit un ensemble par une expression de la forme
# set( sequence )
# ou sequence est une donnee parcourable (liste, tuple, chaıne de caracteres, etc.).

s = set("abracadabra")
print(s)


texte = """Maitre Corbeau, sur un arbre perche 
Tenait en son bec un fromage 
Maitre Renard, par l’odeur alleche 
lui tint a peu pres ce langage"""

# affiche les caracteres qui n'apparaissent qu'une fois

auMoinsUneFois = set()
auMoinsDeuxFois = set()
for caract in texte:
    if caract in auMoinsUneFois: auMoinsDeuxFois.add(caract)
    else: auMoinsUneFois.add(caract)
print( auMoinsUneFois.difference(auMoinsDeuxFois))
