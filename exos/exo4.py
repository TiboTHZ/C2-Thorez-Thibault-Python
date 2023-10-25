nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def calcul(list):
    maximum = max(list)
    minimum = min(list)
    somme = sum(list)
    moyenne = somme / len(list)
    print("Maximum :", maximum)
    print("Minimum :", minimum)
    print("Moyenne :", moyenne)

calcul(nombres)