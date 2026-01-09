# **Corrigés 1 : Gestion des exceptions et validation d'entrées**

---

## **Exercice 1 : Prédire la sortie**

```python
try:
    nombre = int("vingt")
except ValueError:
    print("Erreur : Ce n'est pas un nombre.")
# Résultat : "Erreur : Ce n'est pas un nombre."
```

---

## **Exercice 2 : Validation d'un entier positif**

```python
def demander_entier_positif():
    valeur_valide = False
    while not valeur_valide:
        try:
            entier = int(input("Entrez un entier positif : "))
            if entier >= 0:
                valeur_valide = True
            else:
                print("Erreur : L'entier doit être positif.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")
    return entier


entier = demander_entier_positif()
print(f"Entier positif valide : {entier}.")
```

---

## **Exercice 3 : Validation d'une note**

```python
def demander_note():
    note_valide = False
    while not note_valide:
        try:
            note = float(input("Entrez une note (entre 0 et 100) : "))
            if 0 <= note <= 100:
                note_valide = True
            else:
                print("Erreur : La note doit être entre 0 et 100.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre.")
    return note


note = demander_note()
print(f"Note valide : {note}.")
```

---

## **Exercice 4 : Validation d'un choix de menu**

```python
def demander_choix():
    choix_valide = False
    while not choix_valide:
        try:
            choix = int(input("Choisissez une option (1, 2, 3 ou 4) : "))
            if 1 <= choix <= 4:
                choix_valide = True
            else:
                print("Erreur : Le choix doit être entre 1 et 4.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")
    return choix


choix = demander_choix()
print(f"Choix valide : {choix}.")
```

---

## **Exercice 5 : Validation d'une année**

```python
from datetime import datetime


def demander_annee():
    annee_valide = False
    annee_actuelle = datetime.now().year
    while not annee_valide:
        try:
            annee = int(input(f"Entrez une année (entre 1900 et {annee_actuelle}) : "))
            if 1900 <= annee <= annee_actuelle:
                annee_valide = True
            else:
                print(f"Erreur : L'année doit être entre 1900 et {annee_actuelle}.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")
    return annee


annee = demander_annee()
print(f"Année valide : {annee}.")
```

---

## **Exercice 6 : Division sécurisée**

```python
def division_securisee():
    division_valide = False
    while not division_valide:
        try:
            numerateur = float(input("Entrez le numérateur : "))
            denominateur = float(input("Entrez le dénominateur : "))
            resultat = numerateur / denominateur
            division_valide = True
        except ValueError:
            print("Erreur : Vous devez entrer un nombre.")
        except ZeroDivisionError:
            print("Erreur : Le dénominateur ne peut pas être zéro.")
    return resultat


resultat = division_securisee()
print(f"Résultat de la division : {resultat}.")
```

---


-------

??? info "Utilisation de l'IA"
Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été
utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations
ont été vérifiées, éditées et complétées par l'auteur.
