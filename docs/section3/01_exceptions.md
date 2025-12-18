# **1. Gestion des exceptions et validation d'entrées**

---

## **1. Introduction aux exceptions**

Les **exceptions** sont des erreurs qui se produisent pendant l'exécution d'un programme. En Python, elles permettent de
gérer les situations anormales de manière élégante, évitant ainsi que le programme ne plante brutalement.

---

## **2. Exemple de base : Conversion d'une entrée**

### **2.1 Sans gestion d'exception**

Si l'utilisateur entre une valeur non numérique, le programme plante avec une erreur `ValueError`.

```python
age = int(input("Entrez votre âge : "))
print(f"Votre âge est {age}.")
```

**Exemple d'exécution avec une entrée invalide** :

```
Entrez votre âge : vingt
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'vingt'
```

---

### **2.2 Avec gestion d'exception**

On utilise `try` et `except` pour capturer et gérer l'erreur.

```python
try:
    age = int(input("Entrez votre âge : "))
    print(f"Votre âge est {age}.")
except ValueError:
    print("Erreur : Vous devez entrer un nombre entier.")
```

**Exemple d'exécution avec une entrée invalide** :

```
Entrez votre âge : vingt
Erreur : Vous devez entrer un nombre entier.
```

---

## **3. Validation d'une entrée avec une boucle**

Pour s'assurer que l'utilisateur entre un nombre entier valide, on utilise une boucle `while` avec une gestion
d'exception.

### **3.1 Première option : avec `while True`**

```python
while True:
    try:
        age = int(input("Entrez votre âge : "))
        break  # Sort de la boucle si la conversion réussit
    except ValueError:
        print("Erreur : Vous devez entrer un nombre entier.")
print(f"Votre âge est {age}.")
```

**Exemple d'exécution** :

```
Entrez votre âge : vingt
Erreur : Vous devez entrer un nombre entier.
Entrez votre âge : 25
Votre âge est 25.
```

### **3.2 Alternative à `while True`**

On utilise une variable booléenne pour contrôler la boucle.

```python
valeur_valide = False
while not valeur_valide:
    try:
        age = int(input("Entrez votre âge : "))
        valeur_valide = True  # La boucle s'arrête si la conversion réussit
    except ValueError:
        print("Erreur : Vous devez entrer un nombre entier.")
print(f"Votre âge est {age}.")
```

**Exemple d'exécution** :

```
Entrez votre âge : vingt
Erreur : Vous devez entrer un nombre entier.
Entrez votre âge : 25
Votre âge est 25.
```

### **3.2 Pourquoi éviter `while True` ?**

- **Lisibilité** : Une boucle `while True` peut rendre le code moins clair, car elle ne montre pas explicitement la
  condition de sortie.
- **Maintenabilité** : Dans un code complexe, il est facile d'oublier un `break`, ce qui peut entraîner des boucles
  infinies.
- **Style** : Certaines équipes de développement préfèrent éviter les boucles infinies explicites pour des raisons de
  style et de robustesse.

---


## **4. Définition d'une fonction pour faciliter la validation**

### **4.1 Version 1 : Avec `while True`**

Cette version est concise et souvent utilisée pour des cas simples.

```python
def demander_entier():
    while True:
        try:
            valeur = int(input("Entrez un nombre entier : "))
            return valeur
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")


age = demander_entier()
print(f"Votre âge est {age}.")
```

---

### **4.2 Version 2 : Sans `while True`**

Cette version utilise une variable booléenne pour contrôler la boucle, ce qui peut être plus explicite.

```python
def demander_entier():
    valeur_valide = False
    while not valeur_valide:
        try:
            valeur = int(input("Entrez un nombre entier : "))
            valeur_valide = True
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")
    return valeur


age = demander_entier()
print(f"Votre âge est {age}.")
```


---

## **5. Fonction avec un prompt personnalisable**

### **5.1 Version 1 : Avec `while True`**

```python
def demander_entier(prompt="Entrez un nombre entier : "):
    while True:
        try:
            valeur = int(input(prompt))
            return valeur
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")


age = demander_entier("Quel est votre âge ? ")
print(f"Votre âge est {age}.")
```

---

### **5.2 Version 2 : Sans `while True`**

```python
def demander_entier(prompt="Entrez un nombre entier : "):
    valeur_valide = False
    while not valeur_valide:
        try:
            valeur = int(input(prompt))
            valeur_valide = True
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")
    return valeur


age = demander_entier("Quel est votre âge ? ")
print(f"Votre âge est {age}.")
```


### **5.3 Version 3 : Avec un message d'erreur personnalisable**

```python
def demander_entier(prompt="Entrez un nombre entier : ", message_erreur="Vous devez entrer un nombre entier."):
    while True:
        try:
            valeur = int(input(prompt))
            return valeur
        except ValueError:
            print("Erreur :", message_erreur)


age = demander_entier("Quel est votre âge ? ", "L'âge doit être un nombre entier.")
print(f"Votre âge est {age}.")
```


---

## **6. Validation d'un nombre flottant**

On peut adapter la fonction pour valider un nombre flottant.

```python
def demander_flottant(prompt="Entrez un nombre : "):
    while True:
        try:
            valeur = float(input(prompt))
            return valeur
        except ValueError:
            print("Erreur : Vous devez entrer un nombre.")


temperature = demander_flottant("Entrez la température : ")
print(f"La température est {temperature}°C.")
```

**Exemple d'exécution** :

```
Entrez la température : très chaud
Erreur : Vous devez entrer un nombre.
Entrez la température : 25.5
La température est 25.5°C.
```

---

## **7. Survol d'autres exceptions courantes**

Voici un aperçu d'autres exceptions courantes en Python :

| **Exception**       | **Cause**                                             |
|---------------------|-------------------------------------------------------|
| `ValueError`        | Valeur incorrecte (ex. : conversion impossible).      |
| `TypeError`         | Opération sur un type non supporté (ex. : `"5" + 3`). |
| `IndexError`        | Accès à un index invalide dans une liste.             |
| `KeyError`          | Accès à une clé inexistante dans un dictionnaire.     |
| `FileNotFoundError` | Tentative d'ouverture d'un fichier inexistant.        |
| `ZeroDivisionError` | Division par zéro.                                    |

---

### **7.1 Exemple : Gestion de `IndexError`**

```python
ma_liste = [1, 2, 3]
try:
    print(ma_liste[5])
except IndexError:
    print("Erreur : Index hors limites.")
```

**Sortie** :

```
Erreur : Index hors limites.
```

---

### **7.2 Exemple : Gestion de `ZeroDivisionError`**

```python
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Erreur : Division par zéro.")
```

**Sortie** :

```
Erreur : Division par zéro.
```

---

### **7.3 Exemple : Gestion de `KeyError`**

```python
mon_dictionnaire = {"nom": "Alice", "âge": 30}
try:
    print(mon_dictionnaire["ville"])
except KeyError:
    print("Erreur : Clé non trouvée.")
```

**Sortie** :

```
Erreur : Clé non trouvée.
```

---

### **7.4 Exemple : Gestion de `FileNotFoundError`**

```python
try:
    with open("fichier_inexistant.txt", "r") as fichier:
        contenu = fichier.read()
except FileNotFoundError:
    print("Erreur : Fichier non trouvé.")
```

**Sortie** :

```
Erreur : Fichier non trouvé.
```

---

## 8. Validation avancée

### **8.1. Exemple : Fonction `demander_age`**

```python
def demander_entier(prompt="Entrez un nombre entier : ", message_erreur="Vous devez entrer un nombre entier."):
    while True:
        try:
            valeur = int(input(prompt))
            return valeur
        except ValueError:
            print("Erreur :", message_erreur)


def demander_age():
    while True:
        age = demander_entier("Quel est votre âge ? ", "L'âge doit être un nombre entier.")
        if age >= 0:
            return age
        print("Erreur : L'âge doit être un nombre positif ou nul.")


age = demander_age()
print(f"Votre âge est {age}.")
```

---

#### **Explication :**

1. **`demander_entier`** :
    - Cette fonction demande à l'utilisateur d'entrer un nombre entier.
    - Elle gère les erreurs de conversion avec un message personnalisable.

2. **`demander_age`** :
    - Cette fonction appelle `demander_entier` pour obtenir un entier.
    - Elle vérifie que l'âge est **positif ou nul** (`age >= 0`).
    - Si l'âge est négatif, elle affiche un message d'erreur et redemande une valeur valide.

---

#### **Exemple d'exécution :**

```
Quel est votre âge ? -5
Erreur : L'âge doit être un nombre positif ou nul.
Quel est votre âge ? vingt
Erreur : L'âge doit être un nombre entier.
Quel est votre âge ? 25
Votre âge est 25.
```

### **8.2. Validation d'une note (float entre 0 et 100)**

#### **8.2.1 Avec boucle `while` et conditionnelles (sans gestion d'exception)**

```python
def demander_note():
    note = float(input("Entrez une note (entre 0 et 100) : "))
    while note < 0 or note > 100:
        print("Erreur : La note doit être entre 0 et 100.")
        note = float(input("Entrez une note (entre 0 et 100) : "))
    return note


note = demander_note()
print(f"Note valide : {note}")
```

**Exemple d'exécution** :

```
Entrez une note (entre 0 et 100) : 120
Erreur : La note doit être entre 0 et 100.
Entrez une note (entre 0 et 100) : -5
Erreur : La note doit être entre 0 et 100.
Entrez une note (entre 0 et 100) : 85.5
Note valide : 85.5
```

---

#### **8.2.2 Avec gestion d'exception et conditionnelles**

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
print(f"Note valide : {note}")
```

**Exemple d'exécution** :

```
Entrez une note (entre 0 et 100) : quatre-vingt-cinq
Erreur : Vous devez entrer un nombre.
Entrez une note (entre 0 et 100) : 120
Erreur : La note doit être entre 0 et 100.
Entrez une note (entre 0 et 100) : 85.5
Note valide : 85.5
```

---

### **8.3. Validation d'un choix dans un menu (entier entre 1 et 3)**

#### **8.3.1 Avec boucle `while` et conditionnelles**

```python
def demander_choix():
    choix = int(input("Choisissez une option (1, 2 ou 3) : "))
    while choix < 1 or choix > 3:
        print("Erreur : Le choix doit être 1, 2 ou 3.")
        choix = int(input("Choisissez une option (1, 2 ou 3) : "))
    return choix


choix = demander_choix()
print(f"Choix valide : {choix}")
```

**Exemple d'exécution** :

```
Choisissez une option (1, 2 ou 3) : 5
Erreur : Le choix doit être 1, 2 ou 3.
Choisissez une option (1, 2 ou 3) : 0
Erreur : Le choix doit être 1, 2 ou 3.
Choisissez une option (1, 2 ou 3) : 2
Choix valide : 2
```

---

#### **8.3.2 Avec gestion d'exception et conditionnelles**

```python
def demander_choix():
    while True:
        try:
            choix = int(input("Choisissez une option (1, 2 ou 3) : "))
            if 1 <= choix <= 3:
                return choix
            else:
                print("Erreur : Le choix doit être 1, 2 ou 3.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")


choix = demander_choix()
print(f"Choix valide : {choix}")
```

**Exemple d'exécution** :

```
Choisissez une option (1, 2 ou 3) : deux
Erreur : Vous devez entrer un nombre entier.
Choisissez une option (1, 2 ou 3) : 5
Erreur : Le choix doit être 1, 2 ou 3.
Choisissez une option (1, 2 ou 3) : 2
Choix valide : 2
```

---

### **8.4. Validation d'une année (entier entre 1900 et l'année actuelle)**

#### **8.4.1 Avec boucle `while` et conditionnelles**

```python
from datetime import datetime


def demander_annee():
    annee_actuelle = datetime.now().year
    annee = int(input(f"Entrez une année (entre 1900 et {annee_actuelle}) : "))
    while annee < 1900 or annee > annee_actuelle:
        print(f"Erreur : L'année doit être entre 1900 et {annee_actuelle}.")
        annee = int(input(f"Entrez une année (entre 1900 et {annee_actuelle}) : "))
    return annee


annee = demander_annee()
print(f"Année valide : {annee}")
```

**Exemple d'exécution** :

```
Entrez une année (entre 1900 et 2025) : 1850
Erreur : L'année doit être entre 1900 et 2025.
Entrez une année (entre 1900 et 2025) : 2030
Erreur : L'année doit être entre 1900 et 2025.
Entrez une année (entre 1900 et 2025) : 2000
Année valide : 2000
```

---

#### **8.4.2 Avec gestion d'exception et conditionnelles**

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
print(f"Année valide : {annee}")
```

**Exemple d'exécution** :

```
Entrez une année (entre 1900 et 2025) : mille neuf cent quatre-vingt-dix
Erreur : Vous devez entrer un nombre entier.
Entrez une année (entre 1900 et 2025) : 1850
Erreur : L'année doit être entre 1900 et 2025.
Entrez une année (entre 1900 et 2025) : 2000
Année valide : 2000
```

---


