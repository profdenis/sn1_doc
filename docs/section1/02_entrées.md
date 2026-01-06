# **2. Utilisation de l'entrée standard**

---

## **1. Définition générale de l'entrée standard**

**Concept** :
L’**entrée standard** (ou *standard input*, souvent abrégée **stdin**) est un mécanisme qui permet à un programme de
recevoir des données de l’utilisateur ou d’un autre programme. Par défaut, l’entrée standard est associée au **clavier**
dans un terminal.

- **Complémentarité avec `stdout`** :
    - `stdout` (sortie standard) : Affiche des données à l’utilisateur.
    - `stdin` (entrée standard) : Reçoit des données de l’utilisateur.
- **Utilisation universelle** :
  Tous les langages de programmation offrent un moyen de lire depuis `stdin` (ex. : `scanf` en C, `input` en Python).

---

## **2. Lecture de chaînes de caractères avec `input()`**

En Python, la fonction `input()` est utilisée pour lire une ligne de texte depuis `stdin`. Elle retourne toujours une
**chaîne de caractères** (`str`).

### **Syntaxe**

```python
variable = input("Message à afficher : ")
```

- **`"Message à afficher : "`** : Invite (*prompt*) affichée à l’utilisateur.
- **`variable`** : Stocke la valeur entrée par l’utilisateur.

---

### **Exemples d’utilisation**

#### **2.1 Lecture d’une chaîne simple**

```python
prenom = input("Entrez votre prénom : ")
print(f"Bonjour, {prenom} !")
```

**Sortie possible** :

```
Entrez votre prénom : Alice
Bonjour, Alice !
```

#### **2.2 Lecture de plusieurs chaînes**

```python
nom = input("Entrez votre nom : ")
ville = input("Entrez votre ville : ")
print(f"{nom} habite à {ville}.")
```

**Sortie possible** :

```
Entrez votre nom : Alice
Entrez votre ville : Drummondville
Alice habite à Montréal.
```

---

## **3. Le concept de variable**

**Définition** :
Une **variable** est un **conteneur** qui stocke une valeur en mémoire. Elle est caractérisée par :

- Un **nom** (ex. : `age`, `nom`).
- Un **type** (ex. : `int`, `str`, `float`).
- Une **valeur** (ex. : `25`, `"Alice"`, `3.14`).

### **Affectation**

```python
age = 25  # Variable de type entier (int)
nom = "Alice"  # Variable de type chaîne (str)
pi = 3.14159  # Variable de type flottant (float)
```

### **Utilisation avec `input()`**

Toute valeur lue avec `input()` est une **chaîne de caractères**. Pour l’utiliser comme un nombre, il faut la
**convertir**.

---

## **4. Conversion de type pour les nombres**

`input()` retourne toujours une chaîne (`str`). Pour effectuer des calculs, il faut convertir cette chaîne en 
**entier** (`int`) ou **flottant** (`float`).

### **Syntaxe**

```python
entier = int(input("Entrez un nombre entier : "))
flottant = float(input("Entrez un nombre décimal : "))
```

---

### **Exemples de conversion**

#### **4.1 Conversion en entier (`int`)**

```python
age = int(input("Entrez votre âge : "))
print(f"L’année prochaine, vous aurez {age + 1} ans.")
```

**Sortie possible** :

```
Entrez votre âge : 25
L’année prochaine, vous aurez 26 ans.
```

#### **4.2 Conversion en flottant (`float`)**

```python
prix = float(input("Entrez le prix de l'article : "))
quantite = int(input("Entrez la quantité : "))
total = prix * quantite
print(f"Total à payer : {total:.2f} $")
```

**Sortie possible** :

```
Entrez le prix de l'article : 12.99
Entrez la quantité : 3
Total à payer : 38.97 $
```

---

### **Que se passe-t-il en cas d’erreur ?**

Si l’utilisateur entre une valeur **non convertible** (ex. : `"abc"` pour un `int`), Python génère une **erreur** (
`ValueError`).
**Exemple** :

```python
age = int(input("Entrez votre âge : "))
# Si l'utilisateur entre "vingt", le programme plante :
# ValueError: invalid literal for int() with base 10: 'vingt'
```

**Note** : La gestion des erreurs (avec `try`/`except`) sera abordée dans une section ultérieure.

---

## **5. Arrondir avec `round()` vs. formatage de sortie avec `:.2f`**

### **5.1 `round()` : Arrondir un nombre**

La fonction `round()` permet d’arrondir un nombre à un certain nombre de décimales.
**Syntaxe** :

```python
nombre_arrondi = round(nombre, ndigits)
```

- **`nombre`** : Le nombre à arrondir.
- **`ndigits`** : Nombre de décimales (optionnel, par défaut `0`).

#### **Exemple**

```python
pi = 3.14159
pi_arrondi = round(pi, 2)
print(pi_arrondi)  # Affiche : 3.14
```

---

### **5.2 Formatage de sortie avec `:.2f`**

Le formatage (avec `.format()` ou _f-strings_) permet d’afficher un nombre avec un certain nombre de décimales **sans
modifier sa valeur réelle**.
**Exemple** :

```python
pi = 3.14159
print(f"Pi arrondi à 2 décimales : {pi:.2f}")  # Affiche : 3.14
print(pi)  # Affiche toujours : 3.14159 (valeur non modifiée)
```

---

### **Comparaison**

| **Méthode**        | **Effet**                                    | **Utilisation typique**                     |
|--------------------|----------------------------------------------|---------------------------------------------|
| `round()`          | Modifie la valeur du nombre.                 | Calculs ultérieurs avec la valeur arrondie. |
| `:.2f` (formatage) | Affiche le nombre arrondi, sans le modifier. | Affichage propre à l’utilisateur.           |

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
