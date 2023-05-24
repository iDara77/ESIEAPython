### Les listes ###
i=0
# 1. Définition
i+=1
liste = ["Gamma", 1, "Alpha", "Echo", 3,"Charlie", 8, "Zoulou","Bravo"]
print(i,liste)
print(i,f"Nombre d'objets: {len(liste)}")
# 2. Lire la valeur a l'indice x
i+=1
print(i,f"Je suis l'objet à l'indice 4 : {liste[4]}")
# 3. Changer la valeur a l'indice x
liste[4] = "Changement"
i+=1
print(i,f"Je suis l'objet à l'indice 4 : {liste[4]}")
# 4. Ajout en fin de liste
liste.append("Zoulou")
liste.append(5)
i+=1
print(i,liste)
# 5. Insertion à la position 5 - indice 4
liste.insert(4, "Victor")
i+=1
print(i,liste)
# 6. Supression de l'objet à l'indice 3
del(liste[1])
i+=1
print(i,liste)
# 7. Supression du premier objet ayant pour valeur Zoulou
liste.remove("Zoulou")
i+=1
print(i,liste)
# 8. Pop: retourne l'objet à l'indice x (ou le dernier si pas d'argument) et le supprime de la liste
obj = liste.pop()
i+=1
print(i,obj, liste)
obj2 = liste.pop(6)
print(i,obj2, liste)
# 9. Extraction des éléments de la liste [start:end:step]
i+=1
print(i,liste[0:3]) # de 0 à 2
print(i,liste[3:-3]) # de 3 à len-1 -3
print(i,liste[3:-3:2]) # chaque 2eme élément de 3 a len-1 -3
# 10. Triage de la liste
i+=1
trier = sorted(liste) # retourne une liste trier sans modifier liste
print(i,trier, liste)
liste.sort()
print(i,liste)
# 11. Combinaison de listes
liste1 = ["Alpha", "Echo", "Juliet"]
liste2 = ["Charlie", "Hotel", "Tango"]
liste1 += liste2
i+=1
print(i,liste1, liste2)

### Les tuples ###
# 12. Définition
alpha_tuple = ("Alpha", "Bravo", "Charlie")
i+=1
print(i, alpha_tuple)

### Les dictionnaires ###
# 13. Définition
alpha_dict = {"a": "Alpha", 2: "Bravo", ("c",3):"Charlie"}
i+=1
print(i, alpha_dict)
# 14. Lire la valeur de la clé 
i+=1
print(i,f"Je suis la valeure de la clé 'a' : {alpha_dict['a']}")
print(i,f"Je suis la valeure de la clé 2 : {alpha_dict[2]}")
print(i,f"Je suis la valeure de la clé ('c',3) : {alpha_dict[('c',3)]}")
# 15. Ajout d'une valeur par clé
alpha_dict["d"] = "Delta"
i+=1
print(i, alpha_dict)
# 16. Combinaisons de dict en utilisant update (comme extend pour les listes)
alpha_dict.update({"e":"Echo", "f":"Fox-trot"})
i+=1
print(i, alpha_dict)
# 17. Extraire la liste des 1) clés 2) valeurs 3) tuples clé/valeur
i+=1
print(i, alpha_dict.keys())
print(i, alpha_dict.values())
print(i, alpha_dict.items())


### Les sets ###
# 18. Définition
alpha_set = {"Alpha", "Bravo", "Charlie", "Alpha"}
i+=1
print(i, alpha_set)

### Les transformations ###
# 19. De string en liste
string_liste = list("helloworld")
i+=1
print(i, string_liste)
tuple_liste = list((1,2,4,6))
print(i, tuple_liste)
set_liste = list({1,2,4,6})
print(i, set_liste)
dictkey_liste = list({"a": "Alpha", 2: "Bravo", ("c",3):"Charlie"})
print(i, dictkey_liste)
# 20. De string en set
string_set = set("helloworld")
i+=1
print(i, string_set)
liste_set = set([1,2,3,2])
print(i, liste_set)
tuple_set = set((1,2,3,2))
print(i, tuple_set)
# 21. De string en tuple
string_set = tuple("helloworld")
i+=1
print(i, string_set)
# 22. De x en dict
ll_dict = dict([ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]) # liste de listes
i+=1
print(i, ll_dict)
lt_dict = dict([ ('a', 'b'), ('c', 'd'), ('e', 'f') ]) # liste de tuples
print(i, lt_dict)
tl_dict = dict(( ['a', 'b'], ['c', 'd'], ['e', 'f'] )) # tuple de listes
print(i, tl_dict)
ls_dict = dict([ 'ab', 'cd', 'ef' ]) # liste de 2 characteres
print(i, ls_dict)