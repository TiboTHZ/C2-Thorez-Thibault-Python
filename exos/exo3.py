nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

addition = nombre1 + nombre2
soustraction = nombre1 - nombre2
multiplication = nombre1 * nombre2

if nombre2 != 0:
    division = nombre1 / nombre2
else:
    division = "Division par zéro impossible"

print(f"Addition : {addition}")
print(f"Soustraction : {soustraction}")
print(f"Multiplication : {multiplication}")
print(f"Division : {division}")
