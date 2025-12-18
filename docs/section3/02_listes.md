# **2. Listes**

---

## **1. Introduction aux listes**

Une **liste** est une collection ordonnée et modifiable d'éléments. Les éléments d'une liste peuvent être de n'importe
quel type (nombres, chaînes de caractères, etc.).

### **1.1 Création d'une liste**

```python
nombres = [1, 2, 3, 4, 5]
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
```

---

## **2. Accès aux éléments d'une liste**

### **2.1 Accéder à un élément**

Les indices commencent à **0**.

```python
nombres = [10, 20, 30, 40, 50]
print(nombres[0])  # Affiche 10
print(nombres[2])  # Affiche 30
```

---

### **2.2 Accéder à une sous-liste (slicing)**

Le **slicing** permet d'extraire une partie d'une liste en utilisant la syntaxe `[début:fin:pas]`. Voici les détails des
différentes options avec le `:` :

- **`liste[debut:fin]`** :
    - Extrait les éléments de l'index `début` (inclus) à l'index `fin` (exclus).
    - Si `début` est omis, le slicing commence au début de la liste.
    - Si `fin` est omis, le slicing va jusqu'à la fin de la liste.
    - **Exemple** :
      ```python
      nombres = [10, 20, 30, 40, 50]
      print(nombres[1:4])  # Affiche [20, 30, 40]
      print(nombres[:3])   # Affiche [10, 20, 30]
      print(nombres[2:])   # Affiche [30, 40, 50]
      ```

- **`liste[debut:fin:pas]`** :
    - `pas` indique l'intervalle entre les éléments extraits.
    - Si `pas` est omis, il vaut `1` par défaut.
    - **Exemple** :
      ```python
      nombres = [10, 20, 30, 40, 50, 60, 70]
      print(nombres[1:6:2])  # Affiche [20, 40, 60]
      print(nombres[::2])    # Affiche [10, 30, 50, 70]
      ```

- **`liste[::-1]`** :
    - Inverse la liste en utilisant un `pas` de `-1`.
    - **Exemple** :
      ```python
      nombres = [10, 20, 30, 40, 50]
      print(nombres[::-1])  # Affiche [50, 40, 30, 20, 10]
      ```

---

### **2.3 Gestion des index invalides et des index négatifs**

#### **Index invalides**

Si vous essayez d'accéder à un index qui n'existe pas dans la liste, Python lève une **erreur `IndexError`**.

- **Exemple d'erreur** :
  ```python
  nombres = [10, 20, 30, 40, 50]
  print(nombres[10])  # Lève une erreur IndexError: list index out of range
  ```

#### **Index négatifs**

Les **index négatifs** permettent d'accéder aux éléments d'une liste en partant de la fin :

- `-1` : Dernier élément.
- `-2` : Avant-dernier élément.
- Et ainsi de suite.

- **Exemple** :
  ```python
  nombres = [10, 20, 30, 40, 50]
  print(nombres[-1])  # Affiche 50
  print(nombres[-3])  # Affiche 30
  ```

#### **Slicing avec des index négatifs**

Vous pouvez également utiliser des index négatifs dans le **slicing** :

- **Exemple** :
  ```python
  nombres = [10, 20, 30, 40, 50]
  print(nombres[-3:-1])  # Affiche [30, 40]
  print(nombres[-4:])    # Affiche [20, 30, 40, 50]
  ```

---

## **3. Calculs avec des boucles `for`**

### **3.1 Somme des éléments d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
somme = 0
for nombre in nombres:
    somme += nombre
print(f"La somme est {somme}.")  # Affiche "La somme est 150."
```

---

### **3.2 Produit des éléments d'une liste**

```python
nombres = [1, 2, 3, 4, 5]
produit = 1
for nombre in nombres:
    produit *= nombre
print(f"Le produit est {produit}.")  # Affiche "Le produit est 120."
```

---

### **3.3 Afficher les éléments d'une liste de chaînes**

```python
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for jour in jours:
    print(jour)
```

**Sortie** :

```
lundi
mardi
mercredi
jeudi
vendredi
samedi
dimanche
```

---

### **3.4 Afficher les éléments avec leur index**

```python
jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for index in range(len(jours)):
    print(f"{index} : {jours[index]}")
```

**Sortie** :

```
0 : lundi
1 : mardi
2 : mercredi
3 : jeudi
4 : vendredi
5 : samedi
6 : dimanche
```

---

## **4. Fonctions sur les listes**

### **4.1 Ajouter un élément**

```python
nombres = [10, 20, 30]
nombres.append(40)
print(nombres)  # Affiche [10, 20, 30, 40]
```

---

### **4.2 Supprimer un élément**

```python
nombres = [10, 20, 30, 40]
nombres.remove(20)
print(nombres)  # Affiche [10, 30, 40]
```

---

### **4.3 Trier une liste**

```python
nombres = [30, 10, 40, 20]
nombres.sort()
print(nombres)  # Affiche [10, 20, 30, 40]
```

---

### **4.4 Inverser une liste**

```python
nombres = [10, 20, 30, 40]
nombres.reverse()
print(nombres)  # Affiche [40, 30, 20, 10]
```

---

### **4.5 Trouver l'index d'un élément**

```python
jours = ["lundi", "mardi", "mercredi", "jeudi"]
index = jours.index("mercredi")
print(index)  # Affiche 2
```

---

## **5. Algorithmes de base sur les listes**

### **5.1 Recherche d'un élément**

```python
nombres = [10, 20, 30, 40, 50]
recherche = 30
trouve = False
for nombre in nombres:
    if nombre == recherche:
        trouve = True
        break
print(f"L'élément {recherche} est présent : {trouve}")  # Affiche "L'élément 30 est présent : True"
```

---

### **5.2 Filtrer les éléments pairs**

```python
nombres = [10, 15, 20, 25, 30, 35]
pairs = []
for nombre in nombres:
    if nombre % 2 == 0:
        pairs.append(nombre)
print(pairs)  # Affiche [10, 20, 30]
```

---

### **5.3 Trouver le maximum d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
maximum = nombres[0]
for nombre in nombres:
    if nombre > maximum:
        maximum = nombre
print(f"Le maximum est {maximum}.")  # Affiche "Le maximum est 50."
```

---

### **5.4 Trouver le minimum d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
minimum = nombres[0]
for nombre in nombres:
    if nombre < minimum:
        minimum = nombre
print(f"Le minimum est {minimum}.")  # Affiche "Le minimum est 10."
```

---

### **5.5 Calculer la moyenne d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
somme = 0
for nombre in nombres:
    somme += nombre
moyenne = somme / len(nombres)
print(f"La moyenne est {moyenne}.")  # Affiche "La moyenne est 30.0."
```

---


