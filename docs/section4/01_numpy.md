# 1. **Introduction à NumPy**

NumPy (*Numerical Python*) est une bibliothèque fondamentale pour le calcul scientifique en Python. Elle fournit des
outils pour travailler avec des **tableaux multidimensionnels** et des **fonctions mathématiques optimisées**.

---

## **1. Installation et importation**

Avant de commencer, assurez-vous d'avoir installé NumPy :

```bash
pip install numpy
```

Ensuite, importez NumPy dans vos scripts :

```python
import numpy as np
```

---

## **2. Constantes mathématiques**

NumPy fournit des **constantes mathématiques** utiles, plus précises que celles de Python standard.

| **Constante** | **Description**                   | **Exemple**         |
|---------------|-----------------------------------|---------------------|
| `np.pi`       | Constante π (pi)                  | `3.141592653589793` |
| `np.e`        | Constante e (base du logarithme)  | `2.718281828459045` |
| `np.inf`      | Infini                            | `inf`               |
| `np.nan`      | "Not a Number" (valeur indéfinie) | `nan`               |

### **Exemples d'utilisation**

```python
import numpy as np

print("π :", np.pi)  # Affiche 3.141592653589793
print("e :", np.e)  # Affiche 2.718281828459045
print("Infini :", np.inf)  # Affiche inf
print("NaN :", np.nan)  # Affiche nan
```

---

## **3. Fonctions mathématiques (sans tableaux)**

NumPy propose des **fonctions mathématiques** optimisées, souvent plus rapides que celles du module `math` de Python.

| **Fonction**     | **Description**              | **Exemple**              |
|------------------|------------------------------|--------------------------|
| `np.sin(x)`      | Sinus de `x` (en radians)    | `np.sin(np.pi/2) → 1.0`  |
| `np.cos(x)`      | Cosinus de `x`               | `np.cos(np.pi) → -1.0`   |
| `np.tan(x)`      | Tangente de `x`              | `np.tan(0) → 0.0`        |
| `np.exp(x)`      | Exponentielle de `x`         | `np.exp(1) → 2.71828...` |
| `np.log(x)`      | Logarithme naturel de `x`    | `np.log(np.e) → 1.0`     |
| `np.log10(x)`    | Logarithme base 10 de `x`    | `np.log10(100) → 2.0`    |
| `np.sqrt(x)`     | Racine carrée de `x`         | `np.sqrt(9) → 3.0`       |
| `np.abs(x)`      | Valeur absolue de `x`        | `np.abs(-5) → 5`         |
| `np.power(x, y)` | `x` élevé à la puissance `y` | `np.power(2, 3) → 8.0`   |

### **Exemples d'utilisation**

```python
angle = np.pi / 4  # 45 degrés en radians
print("sin(π/4) :", np.sin(angle))  # Affiche 0.7071067811865475
print("exp(1) :", np.exp(1))  # Affiche 2.718281828459045
print("log(1) :", np.log(1))  # Affiche 0.0
print("2^3 :", np.power(2, 3))  # Affiche 8.0
```

---

## **4. Introduction aux tableaux (`ndarray`)**

Un **tableau NumPy** (`ndarray`) est une structure de données **multidimensionnelle**, homogène (tous les éléments sont
du même type) et **optimisée pour les calculs numériques**.

### **4.1 Créer un tableau**

```python
# Tableau 1D (vecteur)
vecteur = np.array([1, 2, 3, 4, 5])
print("Vecteur :", vecteur)  # Affiche [1 2 3 4 5]

# Tableau 2D (matrice)
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrice :\n", matrice)
# Affiche :
# [[1 2 3]
#  [4 5 6]]
```

### **4.2 Types de données (`dtype`)**

NumPy infère automatiquement le type des éléments, mais vous pouvez le spécifier explicitement :

```python
vecteur_float = np.array([1, 2, 3], dtype=np.float64)
vecteur_int = np.array([1, 2, 3], dtype=np.int32)
print("Float64 :", vecteur_float.dtype)  # Affiche float64
print("Int32 :", vecteur_int.dtype)  # Affiche int32
```

### **4.3 Propriétés des tableaux**

| **Propriété** | **Description**          | **Exemple**              |
|---------------|--------------------------|--------------------------|
| `ndim`        | Nombre de dimensions     | `vecteur.ndim → 1`       |
| `shape`       | Forme du tableau (tuple) | `matrice.shape → (2, 3)` |
| `size`        | Nombre total d'éléments  | `matrice.size → 6`       |
| `dtype`       | Type des éléments        | `vecteur.dtype → int64`  |

```python
print("Dimensions de la matrice :", matrice.ndim)  # Affiche 2
print("Forme de la matrice :", matrice.shape)  # Affiche (2, 3)
print("Taille totale :", matrice.size)  # Affiche 6
```

### **4.4 Tableaux spéciaux**

| **Fonction**                 | **Description**                           | **Exemple**                                         |
|------------------------------|-------------------------------------------|-----------------------------------------------------|
| `np.zeros(shape)`            | Tableau de zéros                          | `np.zeros(3) → [0. 0. 0.]`                          |
| `np.ones(shape)`             | Tableau de uns                            | `np.ones((2, 2)) → [[1. 1.], [1. 1.]]`              |
| `np.arange(debut, fin, pas)` | Tableau de valeurs régulièrement espacées | `np.arange(0, 5, 1) → [0 1 2 3 4]`                  |
| `np.linspace(debut, fin, n)` | `n` valeurs entre `debut` et `fin`        | `np.linspace(0, 1, 5) → [0.  0.25  0.5  0.75  1. ]` |
| `np.eye(n)`                  | Matrice identité de taille `n`            | `np.eye(2) → [[1. 0.], [0. 1.]]`                    |

```python
print("Zéros :", np.zeros(3))  # [0. 0. 0.]
print("Uns :\n", np.ones((2, 2)))  # [[1. 1.], [1. 1.]]
print("Arange :", np.arange(0, 5, 1))  # [0 1 2 3 4]
print("Linspace :", np.linspace(0, 1, 5))  # [0.   0.25 0.5  0.75 1.  ]
print("Matrice identité :\n", np.eye(2))  # [[1. 0.], [0. 1.]]
```

---

## **5. Fonctions mathématiques sur les tableaux**

Les fonctions mathématiques de NumPy **s'appliquent élément par élément** sur les tableaux.

### **5.1 Fonctions élémentaires**

```python
vecteur = np.array([0, np.pi / 2, np.pi])
print("sin(vecteur) :", np.sin(vecteur))  # Affiche [0. 1. 1.2246468e-16]

matrice = np.array([[1, 4], [9, 16]])
print("Racine carrée :\n", np.sqrt(matrice))
# Affiche :
# [[1. 2.]
#  [3. 4.]]
```

### **5.2 Fonctions statistiques**

| **Fonction**              | **Description**            | **Exemple**                    |
|---------------------------|----------------------------|--------------------------------|
| `np.sum(a)`               | Somme de tous les éléments | `np.sum([1, 2, 3]) → 6`        |
| `np.mean(a)`              | Moyenne des éléments       | `np.mean([1, 2, 3]) → 2.0`     |
| `np.min(a)` / `np.max(a)` | Minimum / Maximum          | `np.min([1, 2, 3]) → 1`        |
| `np.std(a)`               | Écart-type                 | `np.std([1, 2, 3]) → 0.816...` |
| `np.var(a)`               | Variance                   | `np.var([1, 2, 3]) → 0.666...` |

```python
notes = np.array([12, 15, 18, 9, 14])
print("Moyenne :", np.mean(notes))  # Affiche 13.6
print("Max :", np.max(notes))  # Affiche 18
print("Écart-type :", np.std(notes))  # Affiche 3.361547262794316
```

### **5.3 Opérations arithmétiques**

Les opérations s'appliquent **élément par élément** :

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a + b :", a + b)  # Affiche [5 7 9]
print("a * b :", a * b)  # Affiche [4 10 18] (multiplication élément par élément)
print("a @ b :", a @ b)  # Affiche 32 (produit scalaire)
```

### **5.4 Agrégation par axe**

Pour les tableaux multidimensionnels, spécifiez l'`axe` :

```python
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print("Somme par ligne :", np.sum(matrice, axis=1))  # Affiche [6 15]
print("Somme par colonne :", np.sum(matrice, axis=0))  # Affiche [5 7 9]
```

---

## **6. Indexation et slicing**

L'**indexation** et le **slicing** fonctionnent comme pour les listes, mais en multidimensionnel.

### **6.1 Indexation**

```python
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print("Élément (0, 1) :", matrice[0, 1])  # Affiche 2
print("Première ligne :", matrice[0])  # Affiche [1 2 3]
```

### **6.2 Slicing**

```python
print("Sous-matrice :\n", matrice[:, 1:])  # Affiche [[2 3], [5 6]]
```

---

## **7. Modification des tableaux**

### **7.1 Modifier la forme (`reshape`)**

```python
vecteur = np.arange(6)  # [0 1 2 3 4 5]
matrice = vecteur.reshape(2, 3)
print("Matrice reshapée :\n", matrice)
# Affiche :
# [[0 1 2]
#  [3 4 5]]
```

### **7.2 Transposition**

```python
print("Transposée :\n", matrice.T)
# Affiche :
# [[0 3]
#  [1 4]
#  [2 5]]
```

---
