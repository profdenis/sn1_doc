def exercice_1_affichage_simple():
    nom = "Alice"
    age = 25
    print(f"{nom} a {age} ans.")


def exercice_2_calculs_f_strings():
    a = 10
    b = 3
    print(f"{a} divisé par {b} est égal à {a / b}.")


def exercice_3_formatage_flottants():
    prix = 12.3456789
    taux = 0.123456789
    print(f"Prix : {prix:.2f} $")
    print(f"Taux : {taux:.2%}")


def exercice_4_formatage_entiers():
    jour = 5
    mois = 12
    annee = 2023
    print(f"{jour:03d}/{mois:03d}/{annee}")


def exercice_5_alignement_texte():
    mot = "Bonjour"
    print(f"{mot:<15}")  # Aligné à gauche
    print(f"{mot:^15}")  # Centré
    print(f"{mot:>15}")  # Aligné à droite


def exercice_6_formatage_scientifique():
    grand_nombre = 123456789
    print(f"{grand_nombre:.3e}")


def exercice_7_formatage_binaire_octal_hex():
    nombre = 255
    print(f"Binaire : {nombre:b}")
    print(f"Octal : {nombre:o}")
    print(f"Hexadécimal : {nombre:#x}")


def exercice_8_separateurs_milliers():
    grand_nombre = 1000000
    print(f"{grand_nombre:,}")


def exercice_9_affichage_signes():
    positif = 123
    negatif = -456
    print(f"Positif : {positif:+d}")
    print(f"Négatif : {negatif:d}")


def exercice_11_formatage_pourcentages():
    taux = 0.7563
    print(f"{taux:.2%}")


def exercice_12_formatage_durees():
    secondes = 3661
    heures = secondes // 3600
    minutes = (secondes % 3600) // 60
    secondes_restantes = secondes % 60
    print(f"{heures:02d}:{minutes:02d}:{secondes_restantes:02d}")


def exercice_13_formatage_monetaire():
    prix = 1234.56789
    print(f"{prix:,.2f} $")


def exercice_14_combinaison_specificateurs():
    nombre = 12345.6789
    print(f"{nombre:+15,.2f}")


def exercice_15_formatage_conditionnel():
    note = 15.5
    message = "Félicitations ! Vous avez réussi" if note >= 10 else "Dommage, vous avez échoué"
    print(f"{message} avec une note de {note:.2f}.")


def exercice_16_formatage_listes():
    fruits = ["pomme", "banane", "cerise"]
    for index, fruit in enumerate(fruits):
        print(f"{index} : {fruit}")


def exercice_17_formatage_dictionnaires():
    capitales = {"France": "Paris", "Canada": "Ottawa", "Japon": "Tokyo"}
    for pays, capitale in capitales.items():
        print(f"{pays} : {capitale}")


def exercice_18_formatage_tableaux_numpy():
    import numpy as np
    tableau = np.array([3.14159, 2.71828, 1.41421])
    formatted = ", ".join([f"{x:.2f}" for x in tableau])
    print(f"[{formatted}]")


def exercice_19_formatage_dates():
    jour = 5
    mois = 12
    annee = 2023
    print(f"{jour:02d}/{mois:02d}/{annee}")


def exercice_20_formatage_personnalise():
    client = "Jean Dupont"
    montant_ht = 123.456
    taux_tva = 0.15
    montant_ttc = montant_ht * (1 + taux_tva)

    print(f"Facture pour {client}")
    print(f"Montant HT : {montant_ht:.2f} $")
    print(f"TVA ({taux_tva:.2%}) : {montant_ht * taux_tva:.2f} $")
    print(f"Montant TTC : {montant_ttc:.2f} $")


def main():
    print("Exécution des corrigés sur les f-strings...\n")
    exercice_1_affichage_simple()
    print()
    exercice_2_calculs_f_strings()
    print()
    exercice_3_formatage_flottants()
    print()
    exercice_4_formatage_entiers()
    print()
    exercice_5_alignement_texte()
    print()
    exercice_6_formatage_scientifique()
    print()
    exercice_7_formatage_binaire_octal_hex()
    print()
    exercice_8_separateurs_milliers()
    print()
    exercice_9_affichage_signes()
    print()
    exercice_11_formatage_pourcentages()
    print()
    exercice_12_formatage_durees()
    print()
    exercice_13_formatage_monetaire()
    print()
    exercice_14_combinaison_specificateurs()
    print()
    exercice_15_formatage_conditionnel()
    print()
    exercice_16_formatage_listes()
    print()
    exercice_17_formatage_dictionnaires()
    print()
    exercice_18_formatage_tableaux_numpy()
    print()
    exercice_19_formatage_dates()
    print()
    exercice_20_formatage_personnalise()
    print("\nTous les corrigés ont été exécutés.")


if __name__ == "__main__":
    main()