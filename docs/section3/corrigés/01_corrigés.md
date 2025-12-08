
# **Corrigés : Gestion des exceptions et validation d'entrées**

---

## **Exercice 1 : Prédire la sortie**

1.
```python
try:
    nombre = int("vingt")
except ValueError:
    print("Erreur : Ce n'est pas un nombre.")
```
**Sortie** :
```
Erreur : Ce n'est pas un nombre.
```

2.
```python
while True:
    try:
        age = int(input("Entrez votre âge : "))
        break
    except ValueError:
        print("Erreur : Vous devez entrer un nombre entier.")
print(f"Votre âge est {age}.")
```
**Exemple d'exécution** :
```
Entrez votre âge : 25
Votre âge est 25.
```

---

## **Exercice 2 : Validation d'un entier positif**
```python
def demander_entier_positif():
    while True:
        try:
            entier = int(input("Entrez un entier positif : "))
            if entier >= 0:
                return entier
            else:
                print("Erreur : L'entier doit être positif.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")

entier = demander_entier_positif()
print(f"Entier positif valide : {entier}.")
```

---

## **Exercice 3 : Validation d'une note**
```python
def demander_note():
    while True:
        try:
            note = float(input("Entrez une note (entre 0 et 100) : "))
            if 0 <= note <= 100:
                return note
            else:
                print("Erreur : La note doit être entre 0 et 100.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre.")

note = demander_note()
print(f"Note valide : {note}.")
```

---

## **Exercice 4 : Validation d'un choix de menu**
```python
def demander_choix():
    while True:
        try:
            choix = int(input("Choisissez une option (1, 2, 3 ou 4) : "))
            if 1 <= choix <= 4:
                return choix
            else:
                print("Erreur : Le choix doit être entre 1 et 4.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")

choix = demander_choix()
print(f"Choix valide : {choix}.")
```

---

## **Exercice 5 : Validation d'une année**
```python
from datetime import datetime

def demander_annee():
    annee_actuelle = datetime.now().year
    while True:
        try:
            annee = int(input(f"Entrez une année (entre 1900 et {annee_actuelle}) : "))
            if 1900 <= annee <= annee_actuelle:
                return annee
            else:
                print(f"Erreur : L'année doit être entre 1900 et {annee_actuelle}.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")

annee = demander_annee()
print(f"Année valide : {annee}.")
```

---

## **Exercice 6 : Validation d'un code postal**
```python
def demander_code_postal():
    while True:
        code_postal = input("Entrez un code postal (5 chiffres) : ")
        if len(code_postal) == 5 and code_postal.isdigit():
            return code_postal
        else:
            print("Erreur : Le code postal doit être une chaîne de 5 chiffres.")

code_postal = demander_code_postal()
print(f"Code postal valide : {code_postal}.")
```

---

## **Exercice 7 : Validation d'une adresse e-mail**
```python
def demander_email():
    while True:
        email = input("Entrez une adresse e-mail : ")
        if "@" in email and "." in email.split("@")[-1]:
            return email
        else:
            print("Erreur : L'adresse e-mail doit contenir un '@' et un '.'.")

email = demander_email()
print(f"Adresse e-mail valide : {email}.")
```

---

## **Exercice 8 : Division sécurisée**
```python
def division_securisee():
    while True:
        try:
            numerateur = float(input("Entrez le numérateur : "))
            denominateur = float(input("Entrez le dénominateur : "))
            resultat = numerateur / denominateur
            return resultat
        except ValueError:
            print("Erreur : Vous devez entrer un nombre.")
        except ZeroDivisionError:
            print("Erreur : Le dénominateur ne peut pas être zéro.")

resultat = division_securisee()
print(f"Résultat de la division : {resultat}.")
```

---

## **Exercice 9 : Lecture sécurisée d'un fichier**
```python
def lire_fichier():
    while True:
        try:
            nom_fichier = input("Entrez le nom du fichier : ")
            with open(nom_fichier, "r") as fichier:
                contenu = fichier.read()
                return contenu
        except FileNotFoundError:
            print("Erreur : Le fichier n'existe pas.")

contenu = lire_fichier()
print(f"Contenu du fichier : {contenu}")
```

---

## **Exercice 10 : Validation d'une liste d'entiers**
```python
def demander_liste_entiers():
    while True:
        try:
            entree = input("Entrez une liste d'entiers séparés par des espaces : ")
            liste_entiers = [int(nombre) for nombre in entree.split()]
            return liste_entiers
        except ValueError:
            print("Erreur : Tous les éléments doivent être des entiers.")

liste_entiers = demander_liste_entiers()
print(f"Liste d'entiers valide : {liste_entiers}.")
```

---

## **Exercice 11 : Validation d'une date**
```python
def demander_date():
    while True:
        date = input("Entrez une date (JJ/MM/AAAA) : ")
        try:
            jour, mois, annee = map(int, date.split("/"))
            if 1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee <= 2100:
                return date
            else:
                print("Erreur : Date invalide.")
        except ValueError:
            print("Erreur : Format de date incorrect.")

date = demander_date()
print(f"Date valide : {date}.")
```

---

## **Exercice 12 : Validation d'un mot de passe**
```python
def demander_mot_de_passe():
    while True:
        mot_de_passe = input("Entrez un mot de passe (au moins 8 caractères, une majuscule et un chiffre) : ")
        if len(mot_de_passe) >= 8 and any(c.isupper() for c in mot_de_passe) and any(c.isdigit() for c in mot_de_passe):
            return mot_de_passe
        else:
            print("Erreur : Le mot de passe doit contenir au moins 8 caractères, une majuscule et un chiffre.")

mot_de_passe = demander_mot_de_passe()
print(f"Mot de passe valide : {mot_de_passe}.")
```

---

## **Exercice 13 : Validation d'une heure**
```python
def demander_heure():
    while True:
        heure = input("Entrez une heure (HH:MM) : ")
        try:
            heures, minutes = map(int, heure.split(":"))
            if 0 <= heures <= 23 and 0 <= minutes <= 59:
                return heure
            else:
                print("Erreur : Heure invalide.")
        except ValueError:
            print("Erreur : Format d'heure incorrect.")

heure = demander_heure()
print(f"Heure valide : {heure}.")
```

---

## **Exercice 14 : Validation d'une liste de notes**
```python
def demander_liste_notes():
    while True:
        try:
            entree = input("Entrez une liste de notes (entre 0 et 100) séparées par des virgules : ")
            liste_notes = [float(note) for note in entree.split(",")]
            if all(0 <= note <= 100 for note in liste_notes):
                return liste_notes
            else:
                print("Erreur : Toutes les notes doivent être entre 0 et 100.")
        except ValueError:
            print("Erreur : Toutes les notes doivent être des nombres.")

liste_notes = demander_liste_notes()
print(f"Liste de notes valide : {liste_notes}.")
```

---

## **Exercice 15 : Validation d'un numéro de téléphone**
```python
def demander_numero_telephone():
    while True:
        numero = input("Entrez un numéro de téléphone (10 chiffres) : ")
        if len(numero) == 10 and numero.isdigit():
            return numero
        else:
            print("Erreur : Le numéro de téléphone doit être une chaîne de 10 chiffres.")

numero = demander_numero_telephone()
print(f"Numéro de téléphone valide : {numero}.")
```

---
**Conseils pédagogiques** :
- Encouragez les étudiants à **tester chaque programme** avec différentes valeurs pour vérifier leur bon fonctionnement.
- Ils peuvent aussi **modifier les exercices** pour explorer d'autres cas ou ajouter des fonctionnalités.

---
