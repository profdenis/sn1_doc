somme = 0
terminé = False
while not terminé:
    nombre = int(input("Entrez un nombre (ou 0 pour arrêter) : "))
    if nombre == 0:
        terminé = True
    else:
        somme += nombre
print(f"La somme est {somme}.")
