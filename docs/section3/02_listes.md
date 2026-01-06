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
  print(nombres[-6])  # Lève une erreur IndexError: list index out of range
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

!!! note "Remarques"
    - Si la liste est vide, le résultat de la somme est `0`.
    - Il existe une fonction pour faire exactement ce calcul : la fonction `sum()`. Elle effectue la même 
    boucle que l'exemple précédent.
    ```python
    nombres = [10, 20, 30, 40, 50]
    somme = sum(nombres)
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
nombres = [10, 20, 30, 20, 40]
nombres.remove(20)
print(nombres)  # Affiche [10, 30, 20, 40]
nombres.remove(123) # Lève une erreur ValueError: list.remove(x): x not in list
```

!!! note "Remarque"
    Si la valeur n'est pas dans la liste, une erreur `ValueError` est levée par `remove`. Il faut donc soit utiliser un 
    `try/except`, soit vérifier l'existence de la valeur avant de la supprimer.
    ```python
    if 123 in nombres:
        nombres.remove(123)
    ```

!!! note "Remarque"
    La méthode `remove()` supprime la première occurrence de la valeur spécifiée. Si la valeur est présente plusieurs
    fois, il faut utiliser une boucle pour supprimer toutes les occurrences.
    ```python
    nombres = [10, 20, 30, 20, 40]
    cible = 20
    while cible in nombres:
        nombres.remove(cible)
    print(nombres)  # Affiche [10, 30, 40]
    ```
    Cette méthode peut être inefficace pour les grandes listes car elle peut être coûteuse en temps de calcul. 
    Il existe une autre méthode plus efficace pour supprimer toutes les occurrences d'une valeur dans une liste
    en Python, mais elle utilise les _compréhensions de liste_, une technique avancée qui n'est pas présentée dans ce
    cours.


---

### **4.3 Supprimer un élément à un index donné**

```python
nombres = [10, 20, 30, 20, 40]
del nombres[1]
print(nombres)  # Affiche [10, 30, 20, 40]
```


---

### **4.4 Trier une liste**

```python
nombres = [30, 10, 40, 20]
nombres.sort()
print(nombres)  # Affiche [10, 20, 30, 40]
```

---

### **4.5 Inverser une liste**

```python
nombres = [10, 20, 30, 40]
nombres.reverse()
print(nombres)  # Affiche [40, 30, 20, 10]
```

---

### **4.6 Trouver l'index d'un élément**

```python
jours = ["lundi", "mardi", "mercredi", "jeudi"]
index = jours.index("mercredi")
print(index)  # Affiche 2
```

!!! note "Remarque"
    - Tout comme `remove()`, si l'élément n'est pas dans la liste, une erreur `ValueError` est levée. Il faut donc soit
    utiliser un `try/except`, soit vérifier l'existence de l'élément avant de le chercher.
    - Également comme `remove()`, si l'élément est dans la liste plusieurs fois, il faut utiliser une boucle pour trouver
    tous les index, ou une compréhension de liste.

---

## **5. Algorithmes de base sur les listes**

### **5.1 Recherche d'un élément**

```python
nombres = [10, 20, 30, 40, 50]
cible = 30
trouve = False
for nombre in nombres:
    if nombre == cible:
        trouve = True
        break
print(f"L'élément {cible} est présent : {trouve}")  # Affiche "L'élément 30 est présent : True"
```

!!! note "Remarque"
    Cet exemple utilise une boucle `for` pour parcourir la liste pour donner un exemple simple de parcours de liste.
    Dans ce cas-ci particulier, il serait plus simple d'utiliser `in` comme dans un exemple précédent.
    ```python
    nombres = [10, 20, 30, 40, 50]
    cible = 30
    trouve = cible in nombres
    print(f"L'élément {cible} est présent : {trouve}")  # Affiche "L'élément 30 est présent : True"
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

!!! note "Remarque"
    La boucle précédente pourrait être remplacée par un appel à la fonction `max()`, avec la liste de nombres en argument.

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

!!! note "Remarque"
    La boucle précédente pourrait être remplacée par un appel à la fonction `min()`, avec la liste de nombres en argument.


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

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.

