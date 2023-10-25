def tri(liste):
    for i in range(1, len(liste)):
        valeur_actuelle = liste[i]
        position = i

        while position > 0 and liste[position - 1] > valeur_actuelle:
            liste[position] = liste[position - 1]
            position -= 1

        liste[position] = valeur_actuelle

ma_liste = [12, 11, 13, 5, 6]
tri(ma_liste)
print("Liste triée :", ma_liste)
