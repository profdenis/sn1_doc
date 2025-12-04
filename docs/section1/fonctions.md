# **4. Définition et utilisation des fonctions**

---

## **1. Définition vs. utilisation (appel) d'une fonction**

### **1.1 Définition d'une fonction**

Une **fonction** est un bloc de code qui effectue une tâche spécifique. Elle est définie avec le mot-clé `def`.

**Syntaxe** :

```python
def nom_de_la_fonction():
# Instructions
```

- **`def`** : Mot-clé pour définir une fonction.
- **`nom_de_la_fonction`** : Nom donné à la fonction (doit être descriptif).
- **`:`** : Indique le début du bloc de code.
- **Indentation** : Les instructions à l'intérieur de la fonction **doivent être indentées** (généralement 4 espaces).

---

### **1.2 Utilisation (appel) d'une fonction**

Pour **exécuter** une fonction, il faut l'**appeler** par son nom suivi de parenthèses.

**Syntaxe** :

```python
nom_de_la_fonction()
```

---

### **1.3 Exemple simple**

```python
# Définition de la fonction
def dire_bonjour():
    print("Bonjour !")


# Appel de la fonction
dire_bonjour()
```

**Sortie** :

```
Bonjour !
```

---

## **2. Fonctions sans paramètre ni retour**

### **2.1 Définition**

Une fonction **sans paramètre** et **sans retour** effectue une tâche sans recevoir ni retourner de données.

**Exemple** :

```python
def afficher_date_du_jour():
    from datetime import datetime
    aujourdhui = datetime.now()
    print(f"Aujourd'hui, nous sommes le {aujourdhui.strftime('%d/%m/%Y')}.")


# Appel
afficher_date_du_jour()
```

**Sortie possible** :

```
Aujourd'hui, nous sommes le 04/12/2025.
```

---

## **3. Fonctions avec 1 paramètre et sans retour**

### **3.1 Définition**

Une fonction avec **1 paramètre** reçoit une valeur lors de l'appel.

**Syntaxe** :

```python
def nom_de_la_fonction(parametre):
# Instructions utilisant parametre
```

---

### **3.2 Exemple**

```python
def dire_bonjour_a(nom):
    print(f"Bonjour, {nom} !")


# Appel
dire_bonjour_a("Alice")
```

**Sortie** :

```
Bonjour, Alice !
```

---

## **4. Fonctions avec 2 paramètres ou plus et sans retour**

### **4.1 Définition**

Une fonction peut recevoir **plusieurs paramètres**, séparés par des virgules.

**Syntaxe** :

```python
def nom_de_la_fonction(param1, param2, ...):
# Instructions utilisant param1, param2, etc.
```

---

### **4.2 Exemple**

```python
def afficher_somme(a, b):
    print(f"La somme de {a} et {b} est {a + b}.")


# Appel
afficher_somme(5, 3)
```

**Sortie** :

```
La somme de 5 et 3 est 8.
```

---

## **5. Fonctions avec retour et différents nombres de paramètres**

### **5.1 Retour de valeur**

Une fonction peut **retourner une valeur** avec le mot-clé `return`.

**Syntaxe** :

```python
def nom_de_la_fonction(param1, param2, ...):
    # Instructions
    return valeur
```

---

### **5.2 Exemples**

#### **5.2.1 Fonction avec 1 paramètre et retour**

```python
def carre(nombre):
    return nombre ** 2


# Appel
resultat = carre(4)
print(f"Le carré de 4 est {resultat}.")
```

**Sortie** :

```
Le carré de 4 est 16.
```

---

#### **5.2.2 Fonction avec 2 paramètres et retour**

```python
def produit(a, b):
    return a * b


# Appel
resultat = produit(3, 7)
print(f"Le produit de 3 et 7 est {resultat}.")
```

**Sortie** :

```
Le produit de 3 et 7 est 21.
```

---

#### **5.2.3 Fonction avec plusieurs retours**

Une fonction peut retourner **plusieurs valeurs** sous forme de tuple.

```python
def calculer_somme_et_produit(a, b):
    somme = a + b
    produit = a * b
    return somme, produit


# Appel
somme, produit = calculer_somme_et_produit(4, 5)
print(f"Somme : {somme}, Produit : {produit}")
```

**Sortie** :

```
Somme : 9, Produit : 20
```

---

## **6. Erreurs courantes avec les fonctions**

### **6.1 Mauvaise indentation**

**Problème** : Oublier d'indenter le code à l'intérieur de la fonction.
**Exemple incorrect** :

```python
def dire_bonjour():
    print("Bonjour !")  # Erreur : pas d'indentation
```

**Correction** :

```python
def dire_bonjour():
    print("Bonjour !")  # Indentation correcte
```

---

### **6.2 Utilisation de variables extérieures à la place de paramètres**

**Problème** : Utiliser une variable définie **en dehors** de la fonction au lieu de passer un paramètre.
**Exemple incorrect** :

```python
nom = "Alice"


def dire_bonjour():
    print(f"Bonjour, {nom}!")  # Utilise une variable externe


dire_bonjour()
```

**Problème** : Si `nom` change, la fonction ne sera plus fiable.

**Correction** :

```python
def dire_bonjour(nom):
    print(f"Bonjour, {nom}!")


dire_bonjour("Alice")
```

---

### **6.3 Oublier le `return`**

**Problème** : Oublier de retourner une valeur quand c'est nécessaire.
**Exemple incorrect** :

```python
def carre(nombre):
    nombre ** 2  # Oublie le return


resultat = carre(4)
print(resultat)  # Affiche None
```

**Correction** :

```python
def carre(nombre):
    return nombre ** 2  # Retourne le résultat
```

---

### **6.4 Nombre incorrect de paramètres**

**Problème** : Appeler une fonction avec un nombre incorrect de paramètres.
**Exemple incorrect** :

```python
def afficher_somme(a, b):
    print(a + b)


afficher_somme(5)  # Erreur : il manque un paramètre
```

**Correction** :

```python
afficher_somme(5, 3)  # Appel correct
```

---

## **7. Résumé des concepts clés**

| **Type de fonction**              | **Exemple de définition**                 | **Exemple d'appel**               |
|-----------------------------------|-------------------------------------------|-----------------------------------|
| Sans paramètre ni retour          | `def dire_bonjour():`                     | `dire_bonjour()`                  |
| Avec 1 paramètre et sans retour   | `def dire_bonjour_a(nom):`                | `dire_bonjour_a("Alice")`         |
| Avec 2+ paramètres et sans retour | `def afficher_somme(a, b):`               | `afficher_somme(5, 3)`            |
| Avec retour et 1 paramètre        | `def carre(nombre): return nombre ** 2`   | `resultat = carre(4)`             |
| Avec retour et 2+ paramètres      | `def produit(a, b): return a * b`         | `resultat = produit(3, 7)`        |
| Avec plusieurs retours            | `def calculer(a, b): return a + b, a * b` | `somme, produit = calculer(4, 5)` |

---

## **8. Exemples détaillés**

### **1. Calcul de l'aire d'un cercle**

**Formule** : \( \text{Aire} = \pi \times \text{rayon}^2 \)

```python
import math


def aire_cercle(rayon):
    """Calcule l'aire d'un cercle à partir de son rayon."""
    return math.pi * rayon ** 2


# Appel de la fonction
rayon = float(input("Entrez le rayon du cercle : "))
aire = aire_cercle(rayon)
print(f"L'aire du cercle de rayon {rayon} est {aire:.2f}.")
```

---

### **2. Calcul de l'aire d'un rectangle**

**Formule** : \( \text{Aire} = \text{longueur} \times \text{largeur} \)

```python
def aire_rectangle(longueur, largeur):
    """Calcule l'aire d'un rectangle à partir de sa longueur et de sa largeur."""
    return longueur * largeur


# Appel de la fonction
longueur = float(input("Entrez la longueur du rectangle : "))
largeur = float(input("Entrez la largeur du rectangle : "))
aire = aire_rectangle(longueur, largeur)
print(f"L'aire du rectangle est {aire:.2f}.")
```

---

### **3. Calcul de la moyenne de trois nombres**

**Formule** : \( \text{Moyenne} = \frac{\text{nombre1} + \text{nombre2} + \text{nombre3}}{3} \)

```python
def moyenne_trois_nombres(nombre1, nombre2, nombre3):
    """Calcule la moyenne de trois nombres."""
    return (nombre1 + nombre2 + nombre3) / 3


# Appel de la fonction
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))
moyenne = moyenne_trois_nombres(nombre1, nombre2, nombre3)
print(f"La moyenne des trois nombres est {moyenne:.2f}.")
```

---

### **4. Conversion de kilomètres en miles**

**Formule** : \( \text{Miles} = \text{Kilomètres} \times 0.621371 \)

```python
def kilometres_vers_miles(kilometres):
    """Convertit une distance de kilomètres en miles."""
    return kilometres * 0.621371


# Appel de la fonction
kilometres = float(input("Entrez la distance en kilomètres : "))
miles = kilometres_vers_miles(kilometres)
print(f"{kilometres} km équivaut à {miles:.2f} miles.")
```

---
