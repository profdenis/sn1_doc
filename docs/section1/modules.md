# **3. Importation de modules**

---

## **1. Introduction aux modules**

Un **module** en Python est un fichier contenant des **fonctions, variables et classes** que tu peux réutiliser dans tes
programmes. Les modules permettent de :

- **Organiser le code** en parties logiques.
- **Réutiliser du code** sans le réécrire.
- **Accéder à des fonctionnalités avancées** (ex. : générer des nombres aléatoires, faire des calculs mathématiques
  complexes).

Pour utiliser un module, il faut l’**importer** avec le mot-clé `import`.

---

## **2. Le module `random`**

Le module `random` permet de générer des **nombres aléatoires**. Il est utile pour :

- Les jeux (ex. : lancer de dés).
- Les simulations (ex. : modèles probabilistes).
- Les algorithmes nécessitant de l’aléatoire (ex. : mélanger une liste).

### **2.1 Importation du module**

```python
import random
```

---

### **2.2 Fonctions courantes de `random`**

#### **`randint(a, b)`**

Génère un **entier aléatoire** entre `a` et `b` (inclus).
**Exemple** :

```python
de = random.randint(1, 6)
print(f"Résultat du lancer de dé : {de}")
```

**Sortie possible** :

```
Résultat du lancer de dé : 4
```

---

#### **`uniform(a, b)`**

Génère un **nombre flottant aléatoire** entre `a` et `b` (inclus).
**Exemple** :

```python
nombre_aleatoire = random.uniform(1.5, 4.5)
print(f"Nombre aléatoire : {nombre_aleatoire:.2f}")
```

**Sortie possible** :

```
Nombre aléatoire : 3.14
```

---

#### **`choice(seq)`**

Sélectionne un **élément aléatoire** dans une séquence (liste, tuple, chaîne).
**Exemple** :

```python
couleurs = ["rouge", "bleu", "vert", "jaune"]
couleur_aleatoire = random.choice(couleurs)
print(f"Couleur choisie : {couleur_aleatoire}")
```

**Sortie possible** :

```
Couleur choisie : vert
```

---

#### **`shuffle(seq)`**

**Mélange** les éléments d’une liste **sur place** (modifie la liste originale).
**Exemple** :

```python
cartes = ["As", "Roi", "Dame", "Valet"]
random.shuffle(cartes)
print(f"Cartes mélangées : {cartes}")
```

**Sortie possible** :

```
Cartes mélangées : ['Dame', 'As', 'Valet', 'Roi']
```

---

#### **`sample(seq, k)`**

Retourne une **liste de `k` éléments aléatoires** tirés de la séquence `seq`, **sans répétition**.
**Exemple** :

```python
nombres = list(range(1, 11))
echantillon = random.sample(nombres, 3)
print(f"Échantillon aléatoire : {echantillon}")
```

**Sortie possible** :

```
Échantillon aléatoire : [7, 2, 9]
```

---

---

## **3. Le module `math`**

Le module `math` fournit des **fonctions mathématiques avancées**, comme les logarithmes, les puissances, ou les
fonctions trigonométriques.

### **3.1 Importation du module**

```python
import math
```

---

### **3.2 Fonctions courantes de `math`**

#### **`sqrt(x)`**

Calcule la **racine carrée** de `x`.
**Exemple** :

```python
racine = math.sqrt(16)
print(f"Racine carrée de 16 : {racine}")
```

**Sortie** :

```
Racine carrée de 16 : 4.0
```

---

#### **`pi` et `e`**

Constantes mathématiques **π (pi)** et **e**.
**Exemple** :

```python
print(f"Valeur de π : {math.pi:.2f}")
print(f"Valeur de e : {math.e:.2f}")
```

**Sortie** :

```
Valeur de π : 3.14
Valeur de e : 2.72
```

---

#### **`sin(x)`, `cos(x)`, `tan(x)`**

Fonctions trigonométriques (angle en **radians**).
**Exemple** :

```python
angle = math.pi / 2  # 90 degrés en radians
print(f"sin(π/2) = {math.sin(angle):.2f}")
```

**Sortie** :

```
sin(π/2) = 1.00
```

---

#### **`log(x, base)`**

Calcule le **logarithme** de `x` pour une base donnée (par défaut, base `e`).
**Exemple** :

```python
logarithme = math.log(100, 10)  # log10(100)
print(f"log10(100) = {logarithme}")
```

**Sortie** :

```
log10(100) = 2.0
```

---

---

## **4. Le module `datetime`**

Le module `datetime` permet de manipuler des **dates et heures**. Il est utile pour :

- Enregistrer des timestamps.
- Calculer des durées.
- Formater des dates pour l’affichage.

### **4.1 Importation du module**

```python
from datetime import datetime, timedelta
```

---

### **4.2 Fonctions courantes de `datetime`**

#### **`datetime.now()`**

Retourne la **date et l’heure actuelles**.
**Exemple** :

```python
maintenant = datetime.now()
print(f"Date et heure actuelles : {maintenant}")
```

**Sortie possible** :

```
Date et heure actuelles : 2025-12-04 14:30:45.123456
```

---

#### **Formater une date**

Utilise `strftime` pour formater une date en chaîne.
**Exemple** :

```python
date_formattee = maintenant.strftime("%d/%m/%Y %H:%M:%S")
print(f"Date formatée : {date_formattee}")
```

**Sortie possible** :

```
Date formatée : 04/12/2025 14:30:45
```

---

#### **`timedelta`**

Représente une **durée** (différence entre deux dates/heures).
**Exemple** :

```python
dans_une_semaine = maintenant + timedelta(days=7)
print(f"Dans une semaine, nous serons le : {dans_une_semaine.strftime('%d/%m/%Y')}")
```

**Sortie possible** :

```
Dans une semaine, nous serons le : 11/12/2025
```

---

---

## **5. Résumé des modules présentés**

| **Module** | **Utilité principale**            | **Fonctions/Constantes clés**                       |
|------------|-----------------------------------|-----------------------------------------------------|
| `random`   | Génération de nombres aléatoires. | `randint`, `uniform`, `choice`, `shuffle`, `sample` |
| `math`     | Fonctions mathématiques avancées. | `sqrt`, `pi`, `e`, `sin`, `cos`, `log`              |
| `datetime` | Manipulation de dates et heures.  | `datetime.now()`, `strftime`, `timedelta`           |

---
