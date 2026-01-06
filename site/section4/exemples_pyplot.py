import matplotlib.pyplot as plt
import numpy as np

def exemple_1_tracer_un_point():
    """Tracer un point."""
    plt.plot(2, 3, 'ro')  # 'ro' : point rouge (red circle)
    plt.title("Exemple 1 : Tracer un point")
    plt.show()

def exemple_2_tracer_plusieurs_points():
    """Tracer plusieurs points."""
    plt.plot(1, 2, 'bo')  # Point bleu
    plt.plot(2, 3, 'go')  # Point vert
    plt.plot(3, 5, 'mo')  # Point magenta
    plt.title("Exemple 2 : Tracer plusieurs points")
    plt.show()

def exemple_3_tracer_une_ligne():
    """Tracer une ligne entre des points."""
    plt.plot([1, 2, 3], [2, 3, 5], 'b-')  # Ligne bleue reliant les points
    plt.title("Exemple 3 : Tracer une ligne")
    plt.show()

def exemple_4_couleurs_et_symboles():
    """Couleurs et symboles."""
    plt.plot([1, 2, 3], [2, 3, 5], 'g--')  # Ligne verte pointillée
    plt.plot([1, 2, 3], [1, 4, 6], 'rs:')  # Carrés rouges reliés par une ligne en pointillés
    plt.title("Exemple 4 : Couleurs et symboles")
    plt.show()

def exemple_5_etiquettes_et_titre():
    """Ajouter des étiquettes et un titre."""
    plt.plot([1, 2, 3], [2, 3, 5], 'bo-')  # Ligne bleue avec des cercles
    plt.xlabel("Axe X")
    plt.ylabel("Axe Y")
    plt.title("Exemple 5 : Étiquettes et titre")
    plt.show()

def exemple_6_limites_des_axes():
    """Modifier les limites des axes."""
    plt.plot([1, 2, 3], [2, 3, 5], 'go--')
    plt.xlim(0, 4)  # Limites de l'axe X : de 0 à 4
    plt.ylim(0, 6)  # Limites de l'axe Y : de 0 à 6
    plt.title("Exemple 6 : Limites des axes")
    plt.show()

def exemple_7_ajouter_une_legende():
    """Ajouter une légende."""
    plt.plot([1, 2, 3], [2, 3, 5], 'bo-', label="Série 1")
    plt.plot([1, 2, 3], [1, 4, 6], 'rs:', label="Série 2")
    plt.legend()  # Affiche la légende
    plt.title("Exemple 7 : Légende")
    plt.show()

def exemple_8_liste_de_valeurs():
    """Tracer une courbe à partir de listes."""
    x = [0, 1, 2, 3, 4, 5]
    y = [0, 1, 4, 9, 16, 25]  # y = x²

    plt.plot(x, y, 'm-', label="y = x²")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Exemple 8 : Liste de valeurs")
    plt.legend()
    plt.show()

def exemple_9_plusieurs_courbes():
    """Tracer plusieurs courbes."""
    x = [0, 1, 2, 3, 4, 5]
    y1 = [0, 1, 4, 9, 16, 25]  # y = x²
    y2 = [0, 1, 2, 3, 4, 5]   # y = x

    plt.plot(x, y1, 'b-', label="y = x²")
    plt.plot(x, y2, 'g--', label="y = x")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Exemple 9 : Plusieurs courbes")
    plt.legend()
    plt.show()

def exemple_10_diagramme_en_barres():
    """Diagramme en barres."""
    categories = ["A", "B", "C", "D"]
    valeurs = [5, 7, 3, 8]

    plt.bar(categories, valeurs, color='cyan')
    plt.xlabel("Catégories")
    plt.ylabel("Valeurs")
    plt.title("Exemple 10 : Diagramme en barres")
    plt.show()

def exemple_11_diagramme_en_secteurs():
    """Diagramme en secteurs (camembert)."""
    categories = ["A", "B", "C", "D"]
    valeurs = [15, 30, 45, 10]

    plt.pie(valeurs, labels=categories, autopct='%1.1f%%')
    plt.title("Exemple 11 : Diagramme en secteurs")
    plt.show()

def exemple_12_tableaux_numpy():
    """Utiliser des tableaux NumPy."""
    x = np.linspace(0, 2 * np.pi, 100)  # 100 valeurs entre 0 et 2π
    y = np.sin(x)  # y = sin(x)

    plt.plot(x, y, 'r-', label="sin(x)")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.title("Exemple 12 : Tableaux NumPy")
    plt.legend()
    plt.show()

def exemple_13_plusieurs_courbes_numpy():
    """Tracer plusieurs courbes avec des tableaux NumPy."""
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, 'b-', label="sin(x)")
    plt.plot(x, y2, 'g--', label="cos(x)")
    plt.xlabel("x")
    plt.ylabel("Valeurs")
    plt.title("Exemple 13 : Plusieurs courbes avec NumPy")
    plt.legend()
    plt.show()

def exemple_14_diagramme_de_dispersion():
    """Diagramme de dispersion (scatter plot)."""
    x = np.random.rand(50)  # 50 valeurs aléatoires entre 0 et 1
    y = np.random.rand(50)

    plt.scatter(x, y, color='blue', marker='o')
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Exemple 14 : Nuage de points aléatoires")
    plt.show()

def exemple_15_personnalisation_avancee():
    """Personnalisation avancée."""
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    plt.plot(x, y1, 'b-', linewidth=2, label="sin(x)")
    plt.plot(x, y2, 'g--', linewidth=2, label="cos(x)")
    plt.xlabel("x", fontsize=12)
    plt.ylabel("y", fontsize=12)
    plt.title("Exemple 15 : Personnalisation avancée", fontsize=14)
    plt.grid(True)  # Ajouter une grille
    plt.legend(fontsize=10)
    plt.show()

def exemple_16_sous_graphiques():
    """Sous-graphiques (subplots)."""
    x = np.linspace(0, 2 * np.pi, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # 1 ligne, 2 colonnes

    ax1.plot(x, y1, 'b-')
    ax1.set_title("sin(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("sin(x)")

    ax2.plot(x, y2, 'r--')
    ax2.set_title("cos(x)")
    ax2.set_xlabel("x")
    ax2.set_ylabel("cos(x)")

    plt.suptitle("Exemple 16 : Sous-graphiques")
    plt.tight_layout()  # Ajuste l'espacement entre les sous-graphiques
    plt.show()

def main():
    """Appel de toutes les fonctions d'exemples."""
    print("Exécution des exemples matplotlib.pyplot...\n")

    exemple_1_tracer_un_point()
    exemple_2_tracer_plusieurs_points()
    exemple_3_tracer_une_ligne()
    exemple_4_couleurs_et_symboles()
    exemple_5_etiquettes_et_titre()
    exemple_6_limites_des_axes()
    exemple_7_ajouter_une_legende()
    exemple_8_liste_de_valeurs()
    exemple_9_plusieurs_courbes()
    exemple_10_diagramme_en_barres()
    exemple_11_diagramme_en_secteurs()
    exemple_12_tableaux_numpy()
    exemple_13_plusieurs_courbes_numpy()
    exemple_14_diagramme_de_dispersion()
    exemple_15_personnalisation_avancee()
    exemple_16_sous_graphiques()

    print("\nTous les exemples ont été exécutés.")

if __name__ == "__main__":
    main()
