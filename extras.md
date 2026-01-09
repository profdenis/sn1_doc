## **Partie 3 : Défis combinés**

### **Exercice 9 : Tableau de multiplication**

Affiche un tableau de multiplication pour les nombres de 1 à 5, sous la forme :

```
1 x 1 = 1
1 x 2 = 2
...
5 x 5 = 25
```

- Utilise une boucle `for` et la méthode de formatage de ton choix.

---
**Question bonus** : Comment ferais-tu pour aligner les résultats à droite ?

---

### **Exercice 10 : Menu interactif**

Crée un menu simple qui affiche :

```
Menu :
1. Afficher la date
2. Calculer une moyenne
3. Quitter
```

- Utilise `print()` avec `sep` et `end` pour formater le menu.
- Pour chaque option, utilise `.format()` ou les f-strings pour afficher un message personnalisé (ex. :
  `"Vous avez choisi l'option 1."`).

### **Exercice 10 : Menu interactif**

```python
print("Menu :", "1. Afficher la date", "2. Calculer une moyenne", "3. Quitter", sep="\n")

choix = 1  # Exemple
print(f"Vous avez choisi l'option {choix}.")
```

---

## **Partie 3 : Défis combinés**

### **Exercice 9 : Tableau de multiplication**

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
```

---
**Réponse bonus** :
Pour aligner les résultats à droite, on peut utiliser :

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j:2d}")
```

---


---

### **Exercice 15 : Formatage conditionnel**

Utilisez une f-string pour afficher un message différent selon la valeur de la variable :

- `note = 15.5`

Résultat attendu :

- Si `note >= 10`, affichez : `"Félicitations ! Vous avez réussi avec une note de 15.50."`
- Sinon, affichez : `"Dommage, vous avez échoué avec une note de 15.50."`

---

### **Exercice 16 : Formatage de listes**

Utilisez une f-string pour afficher chaque élément d'une liste sur une nouvelle ligne avec un numéro d'index :

- `fruits = ["pomme", "banane", "cerise"]`

Résultat attendu :

```
0 : pomme
1 : banane
2 : cerise
```

---

### **Exercice 17 : Formatage de dictionnaires**

Utilisez une f-string pour afficher chaque paire clé-valeur d'un dictionnaire :

- `capitales = {"France": "Paris", "Canada": "Ottawa", "Japon": "Tokyo"}`

Résultat attendu :

```
France : Paris
Canada : Ottawa
Japon : Tokyo
```

---

### **Exercice 18 : Formatage de tableaux NumPy**

Utilisez une f-string pour afficher les éléments d'un tableau NumPy avec **2 décimales** :

- `tableau = np.array([3.14159, 2.71828, 1.41421])`

Résultat attendu : `"[3.14, 2.72, 1.41]"`

---

### **Exercice 19 : Formatage de dates**

Formatez les variables suivantes pour afficher une date sous la forme `JJ/MM/AAAA` :

- `jour = 5`
- `mois = 12`
- `annee = 2023`

Résultat attendu : `"05/12/2023"`


---

### **Exercice 15 : Formatage conditionnel**

```python
note = 15.5
message = "Félicitations ! Vous avez réussi" if note >= 10 else "Dommage, vous avez échoué"
print(f"{message} avec une note de {note:.2f}.")
# Résultat : "Félicitations ! Vous avez réussi avec une note de 15.50."
```

---

### **Exercice 16 : Formatage de listes**

```python
fruits = ["pomme", "banane", "cerise"]
for index, fruit in enumerate(fruits):
    print(f"{index} : {fruit}")
# Résultat :
# 0 : pomme
# 1 : banane
# 2 : cerise
```

---

### **Exercice 17 : Formatage de dictionnaires**

```python
capitales = {"France": "Paris", "Canada": "Ottawa", "Japon": "Tokyo"}
for pays, capitale in capitales.items():
    print(f"{pays} : {capitale}")
# Résultat :
# France : Paris
# Canada : Ottawa
# Japon : Tokyo
```

---

### **Exercice 18 : Formatage de tableaux NumPy**

```python
import numpy as np

tableau = np.array([3.14159, 2.71828, 1.41421])
formatted = ", ".join([f"{x:.2f}" for x in tableau])
print(f"[{formatted}]")
# Résultat : "[3.14, 2.72, 1.41]"
```

---

### **Exercice 19 : Formatage de dates**

```python
jour = 5
mois = 12
annee = 2023
print(f"{jour:02d}/{mois:02d}/{annee}")
# Résultat : "05/12/2023"
```


### **Exercice 8 : Lecture de plusieurs valeurs en une ligne**

Demandez à l’utilisateur d’entrer **trois nombres séparés par des espaces** (ex. : `10 20 30`).

- Lisez ces nombres en une seule ligne avec `input().split()`.
- Convertissez-les en entiers.
- Affichez leur somme.

---

### **Exercice 8 : Lecture de plusieurs valeurs en une ligne**

```python
nombres = input("Entrez trois nombres séparés par des espaces : ")
a, b, c = map(int, nombres.split())
somme = a + b + c
print(f"La somme est {somme}.")
```

---

---

## **Exercices avancés**

### **Exercice 11 : Calcul de factorielle**

Demandez à l’utilisateur un nombre entier positif, puis :

- Calculez sa factorielle (ex. : `5! = 5 * 4 * 3 * 2 * 1 = 120`).
- Affichez le résultat.

---

### **Exercice 12 : Lecture et traitement de liste**

Demandez à l’utilisateur d’entrer **5 nombres séparés par des virgules** (ex. : `1,2,3,4,5`).

- Convertissez ces nombres en une liste d’entiers.
- Calculez et affichez la **somme** et la **moyenne** de ces nombres.

---

### **Exercice 13 : Conversion de temps en secondes**

Demandez à l’utilisateur une durée sous la forme `HH:MM:SS` (ex. : `01:30:45`), puis :

- Convertissez cette durée en **secondes**.
- Affichez le résultat.

---

### **Exercice 14 : Calcul de distance**

Demandez à l’utilisateur :

- La vitesse (en km/h).
- Le temps (en heures).
  Calculez et affichez la distance parcourue (formule : `distance = vitesse * temps`).

---

### **Exercice 15 : Jeu de devinette**

Générez un nombre aléatoire entre 1 et 100.
Demandez à l’utilisateur de deviner ce nombre.

- Si le nombre est trop grand ou trop petit, donnez un indice.
- Répétez jusqu’à ce que l’utilisateur trouve le bon nombre.

---

---

## **Exercices bonus (pour aller plus loin)**

### **Exercice 16 : Calcul de pourcentage**

Demandez à l’utilisateur :

- Un nombre total (ex. : 500).
- Un nombre partiel (ex. : 125).
  Calculez et affichez le pourcentage que représente le nombre partiel par rapport au total.

---

### **Exercice 17 : Lecture et validation**

Demandez à l’utilisateur un nombre entre 1 et 100.

- Tant que l’entrée n’est pas un nombre valide dans cet intervalle, redemandez-lui.
- Affichez le nombre une fois qu’il est valide.

*(Note : Cet exercice nécessite une boucle `while`, mais sans gestion d’exceptions pour l’instant.)*

---

### **Exercice 18 : Calcul de volume**

Demandez à l’utilisateur :

- Le rayon d’une sphère.
  Calculez et affichez son volume (formule : `V = (4/3) * π * r^3`).

---

---

## **Exercices avancés**

### **Exercice 11 : Calcul de factorielle**

```python
n = int(input("Entrez un nombre entier positif : "))
factorielle = 1
for i in range(1, n + 1):
    factorielle *= i
print(f"La factorielle de {n} est {factorielle}.")
```

---

### **Exercice 12 : Lecture et traitement de liste**

```python
nombres_str = input("Entrez 5 nombres séparés par des virgules : ")
nombres = [int(n) for n in nombres_str.split(",")]
somme = sum(nombres)
moyenne = somme / len(nombres)
print(f"Somme : {somme}, Moyenne : {moyenne:.2f}.")
```

---

### **Exercice 13 : Conversion de temps en secondes**

```python
temps = input("Entrez une durée sous la forme HH:MM:SS : ")
heures, minutes, secondes = map(int, temps.split(":"))
total_secondes = heures * 3600 + minutes * 60 + secondes
print(f"{temps} équivaut à {total_secondes} secondes.")
```

---

### **Exercice 14 : Calcul de distance**

```python
vitesse = float(input("Entrez la vitesse (en km/h) : "))
temps = float(input("Entrez le temps (en heures) : "))
distance = vitesse * temps
print(f"La distance parcourue est {distance:.2f} km.")
```

---

### **Exercice 15 : Jeu de devinette**

```python
import random

nombre_a_deviner = random.randint(1, 100)
while True:
    devine = int(input("Devinez le nombre entre 1 et 100 : "))
    if devine < nombre_a_deviner:
        print("Trop petit !")
    elif devine > nombre_a_deviner:
        print("Trop grand !")
    else:
        print(f"Bravo ! Vous avez trouvé {nombre_a_deviner}.")
        break
```

---

---

## **Exercices bonus**

### **Exercice 16 : Calcul de pourcentage**

```python
total = float(input("Entrez le nombre total : "))
partiel = float(input("Entrez le nombre partiel : "))
pourcentage = (partiel / total) * 100
print(f"{partiel} représente {pourcentage:.2f}% de {total}.")
```

---

### **Exercice 17 : Lecture et validation**

```python
while True:
    nombre = int(input("Entrez un nombre entre 1 et 100 : "))
    if 1 <= nombre <= 100:
        print(f"Nombre valide : {nombre}.")
        break
    else:
        print("Nombre invalide. Réessayez.")
```

---

### **Exercice 18 : Calcul de volume**

```python
import math

rayon = float(input("Entrez le rayon de la sphère (en mètres) : "))
volume = (4 / 3) * math.pi * (rayon ** 3)
print(f"Le volume de la sphère est {volume:.2f} m³.")
```

---

### **Exercice 3 : Choix aléatoire**

Créez une liste de 5 fruits (ex. : `["pomme", "banane", "orange", "kiwi", "fraise"]`). Utilisez `random.choice()` pour
sélectionner un fruit aléatoire et affichez-le.

---

### **Exercice 4 : Mélanger une liste**

Créez une liste de 5 nombres entiers. Utilisez `random.shuffle()` pour mélanger cette liste, puis affichez-la avant et
après le mélange.

---

### **Exercice 5 : Échantillon aléatoire**

Créez une liste de nombres de 1 à 20. Utilisez `random.sample()` pour tirer un échantillon de 5 nombres aléatoires *
*sans répétition**, puis affichez cet échantillon.

---

### **Exercice 3 : Choix aléatoire**
```python
import random
fruits = ["pomme", "banane", "orange", "kiwi", "fraise"]
fruit_aleatoire = random.choice(fruits)
print(f"Fruit choisi : {fruit_aleatoire}")
```

---

### **Exercice 4 : Mélanger une liste**
```python
import random
nombres = [1, 2, 3, 4, 5]
print(f"Liste originale : {nombres}")
random.shuffle(nombres)
print(f"Liste mélangée : {nombres}")
```

---

### **Exercice 5 : Échantillon aléatoire**
```python
import random
nombres = list(range(1, 21))
echantillon = random.sample(nombres, 5)
print(f"Échantillon aléatoire : {echantillon}")
```

---


### **Exercice 6 : Jeu de pile ou face**

Simulez un **lancer de pièce** (pile ou face) en utilisant `random.choice()`. Affichez le résultat.

---


### **Exercice 6 : Jeu de pile ou face**
```python
import random
resultat = random.choice(["pile", "face"])
print(f"Résultat du lancer : {resultat}")
```

---

---

## **Exercices combinés**

### **Exercice 17 : Simulation de lancer de dés**

Simulez 10 lancers d’un dé à 6 faces en utilisant `random.randint()`. Stockez les résultats dans une liste et affichez :

- La liste des résultats.
- La moyenne des lancers (utilisez `sum()` et `len()`).

---

### **Exercice 18 : Calcul de date aléatoire**

Générez une **date aléatoire** entre le 1er janvier 2020 et le 31 décembre 2025 en utilisant `random` et `datetime`.
Affichez cette date au format `DD/MM/YYYY`.

*(Indice : Générez un nombre aléatoire de jours entre les deux dates, puis ajoutez-le à la date de début.)*

---

### **Exercice 19 : Calcul de volume d’une sphère**

Demandez à l’utilisateur le rayon d’une sphère. Utilisez `math.pi` pour calculer son volume (formule :
`V = (4/3) * π * r^3`). Affichez le résultat avec 2 décimales.

---

### **Exercice 20 : Jeu de devinette amélioré**

Générez un nombre aléatoire entre 1 et 100. Demandez à l’utilisateur de deviner ce nombre. Utilisez une boucle pour :

- Donner des indices ("Trop grand" ou "Trop petit").
- Compter le nombre de tentatives.
- Afficher un message de félicitations une fois le nombre trouvé.

*(Indice : Utilisez `random.randint()` pour générer le nombre aléatoire.)*

---

---

## **Corrigés pour les exercices combinés**

### **Exercice 17 : Simulation de lancer de dés**
```python
import random
lancers = [random.randint(1, 6) for _ in range(10)]
moyenne = sum(lancers) / len(lancers)
print(f"Résultats des lancers : {lancers}")
print(f"Moyenne des lancers : {moyenne:.2f}")
```

---

### **Exercice 18 : Calcul de date aléatoire**
```python
import random
from datetime import datetime, timedelta
date_debut = datetime(2020, 1, 1)
date_fin = datetime(2025, 12, 31)
duree = date_fin - date_debut
jours_aleatoires = random.randint(0, duree.days)
date_aleatoire = date_debut + timedelta(days=jours_aleatoires)
print(f"Date aléatoire : {date_aleatoire.strftime('%d/%m/%Y')}")
```

---

### **Exercice 19 : Calcul de volume d’une sphère**
```python
import math
rayon = float(input("Entrez le rayon de la sphère : "))
volume = (4/3) * math.pi * (rayon ** 3)
print(f"Volume de la sphère : {volume:.2f}")
```

---

### **Exercice 20 : Jeu de devinette amélioré**
```python
import random
nombre_a_deviner = random.randint(1, 100)
tentatives = 0
while True:
    devine = int(input("Devinez le nombre entre 1 et 100 : "))
    tentatives += 1
    if devine < nombre_a_deviner:
        print("Trop petit !")
    elif devine > nombre_a_deviner:
        print("Trop grand !")
    else:
        print(f"Bravo ! Vous avez trouvé en {tentatives} tentatives.")
        break
```

---


### **Exercice 9 : Recherche dans une matrice**

Écrivez un programme qui recherche un nombre dans une matrice 3x3 prédéfinie. Le programme doit demander à l'utilisateur
d'entrer un nombre et utiliser des boucles imbriquées pour vérifier si ce nombre est présent dans la matrice.

---

## **Exercice 9 : Recherche dans une matrice**

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
recherche = int(input("Entrez un nombre à rechercher : "))
trouve = False
for i in range(3):
    for j in range(3):
        if matrice[i][j] == recherche:
            trouve = True
            break
    if trouve:
        break
if trouve:
    print(f"Le nombre {recherche} a été trouvé.")
else:
    print(f"Le nombre {recherche} n'a pas été trouvé.")
```

**Exemple d'exécution** :

```
Entrez un nombre à rechercher : 5
Le nombre 5 a été trouvé.
```

---

### **Exercice 6 : Validation d'un code postal**

Écrivez une fonction `demander_code_postal()` qui demande à l'utilisateur d'entrer un code postal de 5 chiffres.
Utilisez une boucle et une gestion d'exception pour valider l'entrée.

---


## **Exercice 6 : Validation d'un code postal**
```python
def demander_code_postal():
    code_valide = False
    while not code_valide:
        code_postal = input("Entrez un code postal (5 chiffres) : ")
        if len(code_postal) == 5 and code_postal.isdigit():
            code_valide = True
        else:
            print("Erreur : Le code postal doit être une chaîne de 5 chiffres.")
    return code_postal

code_postal = demander_code_postal()
print(f"Code postal valide : {code_postal}.")
```

---



### **Exercice 7 : Validation d'une adresse e-mail**

Écrivez une fonction `demander_email()` qui demande à l'utilisateur d'entrer une adresse e-mail valide (contenant un `@`
et un `.`). Utilisez une boucle et une gestion d'exception pour valider l'entrée.

---

## **Exercice 7 : Validation d'une adresse e-mail**
```python
def demander_email():
    email_valide = False
    while not email_valide:
        email = input("Entrez une adresse e-mail : ")
        if "@" in email and "." in email.split("@")[-1]:
            email_valide = True
        else:
            print("Erreur : L'adresse e-mail doit contenir un '@' et un '.'.")
    return email

email = demander_email()
print(f"Adresse e-mail valide : {email}.")
```



### **Exercice 9 : Lecture sécurisée d'un fichier**

Écrivez une fonction `lire_fichier()` qui demande à l'utilisateur d'entrer le nom d'un fichier et tente de lire son
contenu. Gérez l'exception `FileNotFoundError`.

---

### **Exercice 10 : Validation d'une liste d'entiers**

Écrivez une fonction `demander_liste_entiers()` qui demande à l'utilisateur d'entrer une liste d'entiers séparés par des
espaces. Validez chaque entier et retournez la liste.

---

### **Exercice 11 : Validation d'une date**

Écrivez une fonction `demander_date()` qui demande à l'utilisateur d'entrer une date sous la forme `JJ/MM/AAAA`. Validez
que la date est correcte (ex. : le jour est entre 1 et 31, le mois entre 1 et 12, etc.).

---


## **Exercice 9 : Lecture sécurisée d'un fichier**
```python
def lire_fichier():
    fichier_valide = False
    while not fichier_valide:
        try:
            nom_fichier = input("Entrez le nom du fichier : ")
            with open(nom_fichier, "r") as fichier:
                contenu = fichier.read()
                fichier_valide = True
        except FileNotFoundError:
            print("Erreur : Le fichier n'existe pas.")
    return contenu

contenu = lire_fichier()
print(f"Contenu du fichier : {contenu}")
```

---

## **Exercice 10 : Validation d'une liste d'entiers**
```python
def demander_liste_entiers():
    liste_valide = False
    while not liste_valide:
        try:
            entree = input("Entrez une liste d'entiers séparés par des espaces : ")
            liste_entiers = [int(nombre) for nombre in entree.split()]
            liste_valide = True
        except ValueError:
            print("Erreur : Tous les éléments doivent être des entiers.")
    return liste_entiers

liste_entiers = demander_liste_entiers()
print(f"Liste d'entiers valide : {liste_entiers}.")
```

---

## **Exercice 11 : Validation d'une date**
```python
def demander_date():
    date_valide = False
    while not date_valide:
        date = input("Entrez une date (JJ/MM/AAAA) : ")
        try:
            jour, mois, annee = map(int, date.split("/"))
            if 1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee <= 2100:
                date_valide = True
            else:
                print("Erreur : Date invalide.")
        except ValueError:
            print("Erreur : Format de date incorrect.")
    return date

date = demander_date()
print(f"Date valide : {date}.")
```

---


### **Exercice 12 : Validation d'un mot de passe**

Écrivez une fonction `demander_mot_de_passe()` qui demande à l'utilisateur d'entrer un mot de passe contenant au moins 8
caractères, une majuscule et un chiffre. Utilisez une boucle et des conditionnelles pour valider l'entrée.

---

### **Exercice 13 : Validation d'une heure**

Écrivez une fonction `demander_heure()` qui demande à l'utilisateur d'entrer une heure sous la forme `HH:MM`. Validez
que l'heure est correcte (ex. : les heures entre 0 et 23, les minutes entre 0 et 59).

---

### **Exercice 14 : Validation d'une liste de notes**

Écrivez une fonction `demander_liste_notes()` qui demande à l'utilisateur d'entrer une liste de notes (entre 0 et 100)
séparées par des virgules. Validez chaque note et retournez la liste.

---

### **Exercice 15 : Validation d'un numéro de téléphone**

Écrivez une fonction `demander_numero_telephone()` qui demande à l'utilisateur d'entrer un numéro de téléphone de 10
chiffres. Utilisez une boucle et des conditionnelles pour valider l'entrée.

---



## **Exercice 12 : Validation d'un mot de passe**
```python
def demander_mot_de_passe():
    mot_de_passe_valide = False
    while not mot_de_passe_valide:
        mot_de_passe = input("Entrez un mot de passe (au moins 8 caractères, une majuscule et un chiffre) : ")
        if len(mot_de_passe) >= 8 and any(c.isupper() for c in mot_de_passe) and any(c.isdigit() for c in mot_de_passe):
            mot_de_passe_valide = True
        else:
            print("Erreur : Le mot de passe doit contenir au moins 8 caractères, une majuscule et un chiffre.")
    return mot_de_passe

mot_de_passe = demander_mot_de_passe()
print(f"Mot de passe valide : {mot_de_passe}.")
```

---

## **Exercice 13 : Validation d'une heure**
```python
def demander_heure():
    heure_valide = False
    while not heure_valide:
        heure = input("Entrez une heure (HH:MM) : ")
        try:
            heures, minutes = map(int, heure.split(":"))
            if 0 <= heures <= 23 and 0 <= minutes <= 59:
                heure_valide = True
            else:
                print("Erreur : Heure invalide.")
        except ValueError:
            print("Erreur : Format d'heure incorrect.")
    return heure

heure = demander_heure()
print(f"Heure valide : {heure}.")
```

---

## **Exercice 14 : Validation d'une liste de notes**
```python
def demander_liste_notes():
    liste_notes_valide = False
    while not liste_notes_valide:
        try:
            entree = input("Entrez une liste de notes (entre 0 et 100) séparées par des virgules : ")
            liste_notes = [float(note) for note in entree.split(",")]
            if all(0 <= note <= 100 for note in liste_notes):
                liste_notes_valide = True
            else:
                print("Erreur : Toutes les notes doivent être entre 0 et 100.")
        except ValueError:
            print("Erreur : Toutes les notes doivent être des nombres.")
    return liste_notes

liste_notes = demander_liste_notes()
print(f"Liste de notes valide : {liste_notes}.")
```

---

## **Exercice 15 : Validation d'un numéro de téléphone**
```python
def demander_numero_telephone():
    numero_valide = False
    while not numero_valide:
        numero = input("Entrez un numéro de téléphone (10 chiffres) : ")
        if len(numero) == 10 and numero.isdigit():
            numero_valide = True
        else:
            print("Erreur : Le numéro de téléphone doit être une chaîne de 10 chiffres.")
    return numero

numero = demander_numero_telephone()
print(f"Numéro de téléphone valide : {numero}.")
```

---

---

### **Exercice 6 : Initiales**
```python
def initiales(nom_complet):
    mots = nom_complet.split()
    return " ".join([f"{mot[0]}." for mot in mots])

print(initiales("Jean Tremblay"))  # "J. T."
```

---

### **Exercice 7 : Valider un code postal**

Écrivez une fonction qui valide un code postal canadien (format : `A1A 1A1`).
**Exemple** : `est_code_postal_valide("H3T 1J4")` → `True`

---

### **Exercice 8 : Extraire les nombres d'une chaîne**

Écrivez une fonction qui extrait tous les nombres d'une chaîne et les retourne dans une liste.
**Exemple** : `"Il a 3 pommes et 5 bananes."` → `[3, 5]`

---

### **Exercice 7 : Valider un code postal**
```python
import re

def est_code_postal_valide(code):
    return bool(re.match(r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$', code))

print(est_code_postal_valide("H3T 1J4"))  # True
print(est_code_postal_valide("H3T1J4"))   # False
```

---

### **Exercice 8 : Extraire les nombres d'une chaîne**
```python
import re

def extraire_nombres(chaine):
    return [int(nombre) for nombre in re.findall(r'\d+', chaine)]

print(extraire_nombres("Il a 3 pommes et 5 bananes."))  # [3, 5]
```

---

### **Exercice 16 : Compter les occurrences de chaque lettre**

Écrivez une fonction qui prend une chaîne et retourne une liste de tuples, chaque tuple contenant une lettre et son
nombre d'occurrences (sans distinction de casse et en ignorant les espaces).
**Exemple** : `"Bonjour"` → `[('b', 1), ('o', 2), ('n', 1), ('j', 1), ('u', 1), ('r', 1)]`

---

### **Exercice 16 : Compter les occurrences de chaque lettre**
```python
def compter_occurrences(chaine):
    chaine = chaine.lower().replace(" ", "")
    occurrences = {}
    for lettre in chaine:
        if lettre in occurrences:
            occurrences[lettre] += 1
        else:
            occurrences[lettre] = 1
    return sorted(occurrences.items())

print(compter_occurrences("Bonjour"))  # [('b', 1), ('j', 1), ('n', 1), ('o', 2), ('r', 1), ('u', 1)]
```

---



### **Exercice 17 : Trouver les anagrammes**

Écrivez une fonction qui prend une liste de mots et retourne une liste de groupes d'anagrammes (mots formés des mêmes
lettres).
**Exemple** : `["écoute", "couteau", "tac", "cat", "acte"]` → `[["écoute"], ["couteau"], ["tac", "cat"], ["acte"]]`

---



### **Exercice 17 : Trouver les anagrammes**
```python
def trouver_anagrammes(mots):
    groupes = {}
    for mot in mots:
        cle = "".join(sorted(mot.lower()))
        if cle in groupes:
            groupes[cle].append(mot)
        else:
            groupes[cle] = [mot]
    return list(groupes.values())

print(trouver_anagrammes(["écoute", "couteau", "tac", "cat", "acte"]))
# [['écoute'], ['couteau'], ['tac', 'cat'], ['acte']]
```

---


## **Exercices combinant chaînes et fonctions**

### **Exercice 18 : Fonction de césar**

Écrivez une fonction qui applique un chiffrement de César (décalage de `n` lettres) à une chaîne.
**Exemple** : `cesar("Bonjour", 3)` → `"Erqmrxu"`

---

### **Exercice 19 : Fonction de capitalisation personnalisée**

Écrivez une fonction qui capitalise chaque mot d'une chaîne sauf une liste de mots exclus.
**Exemple** : `capitaliser("bonjour tout le monde", ["le"])` → `"Bonjour Tout le Monde"`

---

### **Exercice 20 : Fonction de troncature**

Écrivez une fonction qui tronque une chaîne à une longueur donnée et ajoute `"..."` si elle est plus longue.
**Exemple** : `tronquer("Bonjour tout le monde", 10)` → `"Bonjour..."`

---

---
**Conseils pour les exercices** :

- Utilisez les **méthodes de chaînes** (`split`, `join`, `replace`, etc.) et les **boucles/conditionnelles** pour
  résoudre les problèmes.
- Testez vos fonctions avec différents cas pour vérifier leur robustesse.


## **Exercices combinant chaînes et fonctions**

### **Exercice 18 : Fonction de césar**
```python
def cesar(chaine, decalage):
    resultat = []
    for lettre in chaine:
        if lettre.isalpha():
            base = ord('A') if lettre.isupper() else ord('a')
            nouvelle_lettre = chr((ord(lettre) - base + decalage) % 26 + base)
            resultat.append(nouvelle_lettre)
        else:
            resultat.append(lettre)
    return "".join(resultat)

print(cesar("Bonjour", 3))  # "Erqmrxu"
```

---

### **Exercice 19 : Fonction de capitalisation personnalisée**
```python
def capitaliser(chaine, exclus):
    mots = chaine.split()
    resultat = []
    for mot in mots:
        if mot.lower() in [e.lower() for e in exclus]:
            resultat.append(mot.lower())
        else:
            resultat.append(mot.capitalize())
    return " ".join(resultat)

print(capitaliser("bonjour tout le monde", ["le"]))  # "Bonjour Tout le Monde"
```

---

### **Exercice 20 : Fonction de troncature**
```python
def tronquer(chaine, longueur):
    if len(chaine) <= longueur:
        return chaine
    return chaine[:longueur] + "..."

print(tronquer("Bonjour tout le monde", 10))  # "Bonjour..."
```

---


e