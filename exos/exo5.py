def factoriel(n):
    if n == 0:
        return 1
    else:
        resultat = 1
        for i in range(1, n + 1):
            resultat *= i
        return resultat

nombre = int(input("Entrez un nombre : "))

resultat_factoriel = factoriel(nombre)

print(f"Le factoriel de {nombre} est {resultat_factoriel}")