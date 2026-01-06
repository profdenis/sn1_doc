# **1. Gestion des exceptions et validation d'entrées**

---

## **1. Introduction aux exceptions**

Les **exceptions** sont des erreurs qui se produisent pendant l'exécution d'un programme. En Python, elles permettent de
gérer les situations anormales de manière élégante, évitant ainsi que le programme ne plante brutalement.

### **Tableau des exceptions courantes en Python**

Voici un **tableau récapitulatif des exceptions les plus courantes et importantes** qu'un débutant peut rencontrer en
Python, avec une brève description et un exemple pour chacune. Le but n'est pas de couvrir toutes les exceptions
possibles, mais plutôt de fournir un aperçu des exceptions les plus courantes et importantes. Il n'est pas 
nécessaire de mémoriser toutes les exceptions, mais plutôt de comprendre comment les gérer et les traiter, et de se 
référer à ce tableau au besoin, ou à la documentation officielle ou aux ressources en ligne pour plus d'informations.

| **Exception**             | **Description**                                                           | **Exemple déclencheur**                                             | **Solution typique**                                                         |
|---------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------|
| **`SyntaxError`**         | Erreur de syntaxe (ex. : parenthèse manquante, mot-clé mal orthographié). | `print("Bonjour"` (parenthèse fermante manquante)                   | Vérifier la syntaxe et corriger les erreurs.                                 |
| **`IndentationError`**    | Mauvaise indentation (ex. : espace ou tabulation manquante).              | `if True:`<br>`print("Bonjour")` (sans indentation)                 | Corriger l'indentation (4 espaces par niveau).                               |
| **`NameError`**           | Variable ou nom non défini.                                               | `print(ma_variable)` (si `ma_variable` n'est pas définie)           | Définir la variable avant de l'utiliser.                                     |
| **`TypeError`**           | Opération ou fonction appliquée à un type inapproprié.                    | `"5" + 3` (ne peut pas additionner `str` et `int`)                  | Convertir les types (`int("5") + 3`).                                        |
| **`IndexError`**          | Accès à un index invalide dans une liste, un tuple ou une chaîne.         | `ma_liste = [1, 2, 3]`<br>`print(ma_liste[5])`                      | Vérifier les limites des indices (`len(ma_liste)`).                          |
| **`KeyError`**            | Accès à une clé inexistante dans un dictionnaire.                         | `mon_dict = {"a": 1}`<br>`print(mon_dict["b"])`                     | Vérifier l'existence de la clé (`"b" in mon_dict`) ou utiliser `dict.get()`. |
| **`ValueError`**          | Valeur incorrecte pour une opération (ex. : conversion impossible).       | `int("abc")`                                                        | Valider les entrées avant conversion.                                        |
| **`AttributeError`**      | Accès à un attribut ou une méthode inexistante.                           | `"Bonjour".append("!")` (les chaînes n'ont pas de méthode `append`) | Vérifier les méthodes disponibles pour le type.                              |
| **`ZeroDivisionError`**   | Division par zéro.                                                        | `10 / 0`                                                            | Vérifier que le dénominateur n'est pas zéro avant la division.               |
| **`FileNotFoundError`**   | Fichier introuvable lors de l'ouverture.                                  | `open("fichier_inexistant.txt", "r")`                               | Vérifier le chemin du fichier ou utiliser `try/except`.                      |
| **`PermissionError`**     | Permission refusée (ex. : écriture dans un fichier en lecture seule).     | `open("/fichier_protégé.txt", "w")`                                 | Vérifier les permissions ou utiliser `try/except`.                           |
| **`ImportError`**         | Module ou bibliothèque introuvable.                                       | `import module_inexistant`                                          | Installer le module (`pip install module`) ou vérifier l'orthographe.        |
| **`KeyboardInterrupt`**   | Interruption par l'utilisateur (Ctrl+C).                                  | Appuyez sur `Ctrl+C` pendant l'exécution.                           | Gérer avec `try/except` si nécessaire.                                       |
| **`OverflowError`**       | Résultat d'une opération trop grand pour être représenté.                 | Calculs avec des entiers très grands.                               | Utiliser des types adaptés (ex. : `float` au lieu de `int`).                 |
| **`MemoryError`**         | Manque de mémoire.                                                        | Création d'une liste ou d'un tableau trop grand.                    | Optimiser l'utilisation de la mémoire ou diviser les tâches.                 |
| **`AssertionError`**      | Échec d'une assertion (`assert`).                                         | `assert 1 == 2, "1 n'est pas égal à 2"`                             | Corriger la condition ou supprimer l'assertion.                              |
| **`OSError`**             | Erreur liée au système d'exploitation (ex. : chemin invalide).            | `os.remove("fichier_inexistant.txt")`                               | Vérifier l'existence du fichier ou utiliser `try/except`.                    |
| **`RuntimeError`**        | Erreur générique pendant l'exécution.                                     | Erreur interne dans un module.                                      | Vérifier la documentation ou le code source.                                 |
| **`NotImplementedError`** | Méthode ou fonction non implémentée.                                      | Appel à une méthode abstraite.                                      | Implémenter la méthode ou utiliser une alternative.                          |
| **`UnicodeError`**        | Erreur de codage/decodage Unicode.                                        | `b'\xff'.decode('utf-8')`                                           | Spécifier le bon encodage (ex. : `'latin-1'`).                               |

---

### **Bonnes pratiques pour les débutants**

1. **Utilisez `try/except`** pour gérer les erreurs prévisibles (ex. : division par zéro, fichiers introuvables).
2. **Lisez les messages d'erreur** : Ils indiquent généralement la nature du problème et la ligne concernée.
3. **Validez les entrées** : Utilisez des conditionnelles pour vérifier les types et les valeurs avant de les utiliser.
4. **Documentez vos fonctions** : Utilisez des docstrings pour expliquer les paramètres attendus et les exceptions
   possibles.
5. **Testez votre code** : Utilisez des cas de test pour couvrir les scénarios d'erreur.

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

!!! warning "Attention"
    **Règle générale** : Évitez les boucles infinies explicites, sauf dans des cas très précis où il n'y a aucune autre
    option possible. Exemple : un serveur qui doit accepter un nombre de requêtes indéterminé, et qui doit 
    s'exécuter pour un temps indéterminé, sans condition d'arrêt précise, donc qui doit s'exécuter le plus 
    longtemps possible.

---

## **4. Définition d'une fonction pour faciliter la validation**

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
    valeur_valide = False
    while not valeur_valide:
        try:
            valeur = int(input(prompt))
            valeur_valide = True
        except ValueError:
            print("Erreur :", message_erreur)
    return valeur

age = demander_entier("Quel est votre âge ? ", "L'âge doit être un nombre entier.")
print(f"Votre âge est {age}.")
```

---

## **6. Validation d'un nombre flottant**

On peut adapter la fonction pour valider un nombre flottant.

```python
def demander_flottant(prompt="Entrez un nombre : "):
    valeur_valide = False
    while not valeur_valide:
        try:
            valeur = float(input(prompt))
            valeur_valide = True
        except ValueError:
            print("Erreur : Vous devez entrer un nombre.")
    return valeur

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

### **7.1 Exemple : Gestion de `IndexError`**

```python
ma_liste = [1, 2, 3]
index = 5 # la valeur pourrait venir d'un utilisateur ou d'un fichier
try:
    print(ma_liste[index])
except IndexError:
    print("Erreur : Index hors limites.")
```

**Sortie** :

```
Erreur : Index hors limites.
```

!!! tip "Astuce"
    Lorsque vous travaillez avec des listes, assurez-vous toujours de vérifier les limites avant d'accéder à un 
    élément. Il est plus facile de vérifier les limites avec une conditionnelle que d'essayer d'accéder à un 
    élément sans vérifier et d'attraper les erreurs avec `try/except`. Le code est plus facile à lire et plus 
    maintenable avec la conditionnelle que le `try/except`.
    ```python
    ma_liste = [1, 2, 3]
    index = 5 # la valeur pourrait venir d'un utilisateur ou d'un fichier
    if 0 <= index < len(ma_liste):
        print(ma_liste[index])
    else:
        print("Erreur : Index hors limites.")
    ```

---

### **7.2 Exemple : Gestion de `ZeroDivisionError`**

```python
valeur = 0 # la valeur pourrait venir d'un utilisateur ou d'un fichier
try:
    resultat = 10 / valeur
except ZeroDivisionError:
    print("Erreur : Division par zéro.")
```

**Sortie** :

```
Erreur : Division par zéro.
```

!!! tip "Astuce"
    Même logique ici que dans l'exemple précédent : il serait préférable de vérifier si le dénominateur est différent 
    de zéro avant de faire la division, plutôt que d'attraper l'exception `ZeroDivisionError`. Cela rend le code plus 
    efficace et plus facile à comprendre.

---

### **7.3 Exemple : Gestion de `KeyError`**

**Note** : les dictionnaires seront présentés en détail dans une section ultérieure.

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

**Note** : la gestion des fichiers sera présentée en détail dans une section ultérieure.

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
    valeur_valide = False
    while not valeur_valide:
        try:
            valeur = int(input(prompt))
            valeur_valide = True
        except ValueError:
            print("Erreur :", message_erreur)
    return valeur


def demander_age():
    valeur_valide = False
    while not valeur_valide:
        age = demander_entier("Quel est votre âge ? ", "L'âge doit être un nombre entier.")
        if age >= 0:
            valeur_valide = True
        else:
            print("Erreur : L'âge doit être un nombre positif ou nul.")
    return age

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

!!! note "Remarque"
    On pourrait généraliser cette fonction pour qu'elle devienne `demander_entier_positif` ou 
    `demander_entier_non_negatif`, en prenant en paramètre le message d'erreur et le message de demande.

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
    valeur_valide = False
    while not valeur_valide:
        try:
            note = float(input("Entrez une note (entre 0 et 100) : "))
            if 0 <= note <= 100:
                valeur_valide = True
            else:
                print("Erreur : La note doit être entre 0 et 100.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre.")
    return note

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
    valeur_valide = False
    while not valeur_valide:
        try:
            choix = int(input("Choisissez une option (1, 2 ou 3) : "))
            if 1 <= choix <= 3:
                valeur_valide = True
            else:
                print("Erreur : Le choix doit être 1, 2 ou 3.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")
    return choix

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
    valeur_valide = False
    while not valeur_valide:
        try:
            annee = int(input(f"Entrez une année (entre 1900 et {annee_actuelle}) : "))
            if 1900 <= annee <= annee_actuelle:
                valeur_valide = True
            else:
                print(f"Erreur : L'année doit être entre 1900 et {annee_actuelle}.")
        except ValueError:
            print("Erreur : Vous devez entrer un nombre entier.")
    return annee

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

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
