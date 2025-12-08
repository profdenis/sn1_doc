# **Boucles `for`**

---

## **1. Pourquoi utiliser des boucles ?**

### **1.1 Illustration du besoin d'une boucle**

Imaginons que nous voulons calculer la somme de plusieurs nombres :

- **Sans boucle** :
    - Pour 3 nombres, on peut écrire :
      ```python
      somme = nombre1 + nombre2 + nombre3
      ```
    - Mais pour **100 nombres**, il faudrait écrire une ligne très longue et répétitive :
      ```python
      somme = nombre1 + nombre2 + nombre3 + ... + nombre100
      ```
    - Cela devient **fastidieux, long et source d'erreurs**.

- **Avec une boucle** :
    - On peut écrire un code **concise et réutilisable** pour additionner 100 nombres (ou même 1000 !) sans répéter
      manuellement chaque addition.

---

## **2. Introduction aux listes**

Avant de parler des boucles `for`, il est utile de comprendre ce qu'est une **liste** en Python.

### **2.1 Qu'est-ce qu'une liste ?**

- Une **liste** est une collection ordonnée d'éléments.
- Les éléments d'une liste peuvent être de **n'importe quel type** (nombres, chaînes de caractères, etc.).
- Les listes sont définies avec des **crochets** `[]`.

### **2.2 Exemple de liste simple**

```python
nombres = [1, 2, 3, 4, 5]
fruits = ["pomme", "banane", "orange"]
```

---

## **3. La boucle `for` avec une liste simple**

### **3.1 Syntaxe de la boucle `for`**

La boucle `for` permet de **parcourir chaque élément d'une liste** (ou d'une autre séquence) et d'exécuter un bloc de
code pour chaque élément.

**Syntaxe** :

```python
for element in liste:
    # Instructions à exécuter pour chaque élément
```

---

### **3.2 Exemple : Afficher chaque élément d'une liste**

```python
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)
```

**Sortie** :

```
pomme
banane
orange
```

---

### **3.3 Exemple : Calculer la somme des éléments d'une liste**

```python
nombres = [1, 2, 3, 4, 5]
somme = 0
for nombre in nombres:
    somme += nombre
print(f"La somme est {somme}.")
```

**Sortie** :

```
La somme est 15.
```

---

## **4. La fonction `range()`**

### **4.1 Qu'est-ce que `range()` ?**

- `range()` est une fonction qui génère une **séquence de nombres**.
- Elle est souvent utilisée avec les boucles `for` pour répéter une action un certain nombre de fois.

---

### **4.2 Syntaxe de `range()`**

- **`range(stop)`** : Génère une séquence de nombres de `0` à `stop - 1`.
- **`range(start, stop)`** : Génère une séquence de nombres de `start` à `stop - 1`.
- **`range(start, stop, step)`** : Génère une séquence de nombres de `start` à `stop - 1`, en incrémentant de `step`.

---

### **4.3 Exemples de `range()`**

#### **Exemple 1 : `range(stop)`**

```python
for i in range(5):
    print(i)
```

**Sortie** :

```
0
1
2
3
4
```

---

#### **Exemple 2 : `range(start, stop)`**

```python
for i in range(2, 6):
    print(i)
```

**Sortie** :

```
2
3
4
5
```

---

#### **Exemple 3 : `range(start, stop, step)`**

```python
for i in range(0, 10, 2):
    print(i)
```

**Sortie** :

```
0
2
4
6
8
```

---

## **5. Exemples pratiques avec `for` et `range()`**

### **5.1 Afficher les nombres de 1 à 10**

```python
for i in range(1, 11):
    print(i)
```

---

### **5.2 Calculer la somme des nombres de 1 à 100**

```python
somme = 0
for i in range(1, 101):
    somme += i
print(f"La somme des nombres de 1 à 100 est {somme}.")
```

**Sortie** :

```
La somme des nombres de 1 à 100 est 5050.
```

---

### **5.3 Afficher les nombres pairs de 0 à 20**

```python
for i in range(0, 21, 2):
    print(i)
```

**Sortie** :

```
0
2
4
6
8
10
12
14
16
18
20
```

---

### **5.4 Compter à rebours de 10 à 1**

```python
for i in range(10, 0, -1):
    print(i)
```

**Sortie** :

```
10
9
8
7
6
5
4
3
2
1
```

---

## **6. Résumé des concepts clés**

| **Concept**                    | **Description**                                                           |
|--------------------------------|---------------------------------------------------------------------------|
| **Boucle `for`**               | Permet de parcourir chaque élément d'une séquence (liste, `range`, etc.). |
| **Liste**                      | Collection ordonnée d'éléments, définie avec des crochets `[]`.           |
| **`range(stop)`**              | Génère une séquence de `0` à `stop - 1`.                                  |
| **`range(start, stop)`**       | Génère une séquence de `start` à `stop - 1`.                              |
| **`range(start, stop, step)`** | Génère une séquence de `start` à `stop - 1`, avec un incrément de `step`. |

---
