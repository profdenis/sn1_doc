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
