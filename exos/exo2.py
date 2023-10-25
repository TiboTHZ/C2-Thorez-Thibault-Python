phrase = input("Veuillez entrer une phrase : ")

majuscules = phrase.upper()
print("En majuscules :", majuscules)

minuscules = phrase.lower()
print("En minuscules :", minuscules)

mots = phrase.split()
nombre_de_mots = len(mots)
print("Nombre de mots :", nombre_de_mots)