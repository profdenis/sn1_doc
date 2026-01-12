# **Corrigés 1 : Introduction à NumPy**

---

## **Exercices sur les constantes et fonctions mathématiques**

### **Exercice 1 : Utiliser les constantes de NumPy**

```python
import numpy as np

# 1. Valeur de π avec 4 décimales
print(f"π : {np.pi:.4f}")  # Affiche 3.1416

# 2. Périmètre d'un cercle de rayon 5
rayon = 5
perimetre = 2 * np.pi * rayon
print(f"Périmètre : {perimetre:.2f}")  # Affiche 31.42

# 3. Valeur de e et e^2
print(f"e : {np.e}")
print(f"e^2 : {np.power(np.e, 2)}")  # Affiche 7.389056...
```

---

### **Exercice 2 : Fonctions trigonométriques**

```python
# 1. Sinus, cosinus et tangente de π/3
x = np.pi / 3
print(f"sin(π/3) : {np.sin(x):.4f}")  # Affiche 0.8660
print(f"cos(π/3) : {np.cos(x):.4f}")  # Affiche 0.5000
print(f"tan(π/3) : {np.tan(x):.4f}")  # Affiche 1.7321

# 2. Vérification de sin²(x) + cos²(x) = 1 pour x = π/4
x = np.pi / 4
print(f"sin²(x) + cos²(x) = {np.power(np.sin(x), 2) + np.power(np.cos(x), 2):.4f}")  # Affiche 1.0000
```

---

### **Exercice 3 : Fonctions exponentielles et logarithmes**

```python
# 1. e^3
print(f"e^3 : {np.exp(3):.4f}")  # Affiche 20.0855

# 2. Logarithme naturel de 10 et logarithme base 10 de 100
print(f"ln(10) : {np.log(10):.4f}")  # Affiche 2.3026
print(f"log10(100) : {np.log10(100):.4f}")  # Affiche 2.0000

# 3. Vérification de log(e^5) = 5
print(f"log(e^5) : {np.log(np.power(np.e, 5)):.4f}")  # Affiche 5.0000
```

---

### **Exercice 4 : Racines et puissances**

```python
# 1. Racine carrée de 16
print(f"√16 : {np.sqrt(16)}")  # Affiche 4.0

# 2. 3^4
print(f"3^4 : {np.power(3, 4)}")  # Affiche 81

# 3. Valeur absolue de -7.5
print(f"|-7.5| : {np.abs(-7.5)}")  # Affiche 7.5
```

---

## **Exercices sur les tableaux (`ndarray`)**

### **Exercice 5 : Créer des tableaux**

```python
# 1. Tableau 1D
vecteur = np.array([2, 4, 6, 8, 10])
print("Vecteur :", vecteur)  # Affiche [ 2  4  6  8 10]

# 2. Tableau 2D
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print("Matrice :\n", matrice)
# Affiche :
# [[1 2 3]
#  [4 5 6]]

# 3. Tableau de zéros
zeros = np.zeros((3, 3))
print("Zéros :\n", zeros)
# Affiche :
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# 4. Tableau de uns
uns = np.ones((2, 4))
print("Uns :\n", uns)
# Affiche :
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# 5. Tableau avec arange
arange = np.arange(0, 10, 1)
print("Arange :", arange)  # Affiche [0 1 2 3 4 5 6 7 8 9]

# 6. Tableau avec linspace
linspace = np.linspace(0, 1, 5)
print("Linspace :", linspace)  # Affiche [0.   0.25 0.5  0.75 1.  ]
```

---

### **Exercice 6 : Propriétés des tableaux**

```python
# Pour le tableau 1D
print("Vecteur - ndim :", vecteur.ndim)  # Affiche 1
print("Vecteur - shape :", vecteur.shape)  # Affiche (5,)
print("Vecteur - size :", vecteur.size)  # Affiche 5
print("Vecteur - dtype :", vecteur.dtype)  # Affiche int64

# Pour le tableau 2D
print("Matrice - ndim :", matrice.ndim)  # Affiche 2
print("Matrice - shape :", matrice.shape)  # Affiche (2, 3)
print("Matrice - size :", matrice.size)  # Affiche 6
print("Matrice - dtype :", matrice.dtype)  # Affiche int64
```

---

### **Exercice 7 : Tableaux spéciaux**

```python
# 1. Matrice identité
identite = np.eye(4)
print("Matrice identité :\n", identite)
# Affiche :
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# 2. Tableau avec linspace
linspace_10 = np.linspace(0, 1, 11)
print("Linspace 0-1 :", linspace_10)  # Affiche [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
```

---

## **Exercices sur les fonctions mathématiques appliquées aux tableaux**

### **Exercice 8 : Fonctions élémentaires sur les tableaux**

```python
# 1. Sinus et cosinus des angles
angles = np.array([0, np.pi / 4, np.pi / 2])
print("sin(angles) :", np.sin(angles))  # Affiche [0.         0.70710678 1.        ]
print("cos(angles) :", np.cos(angles))  # Affiche [1.         0.70710678 6.123234e-17]

# 2. Racine carrée des nombres
nombres = np.array([1, 4, 9, 16])
print("√nombres :", np.sqrt(nombres))  # Affiche [1. 2. 3. 4.]
```

---

### **Exercice 9 : Fonctions statistiques**

```python
# 1. Statistiques sur les notes
notes = np.array([12, 15, 18, 9, 14])
print("Moyenne :", np.mean(notes))  # Affiche 13.6
print("Max :", np.max(notes))  # Affiche 18
print("Min :", np.min(notes))  # Affiche 9
print("Écart-type :", np.std(notes))  # Affiche 3.361547262794316

# 2. Statistiques sur la matrice
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print("Somme totale :", np.sum(matrice))  # Affiche 21
print("Somme par ligne :", np.sum(matrice, axis=1))  # Affiche [6 15]
print("Somme par colonne :", np.sum(matrice, axis=0))  # Affiche [5 7 9]
```

---

### **Exercice 10 : Opérations arithmétiques sur les tableaux**

```python
# 1. Opérations sur a et b
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("a + b :", a + b)  # Affiche [5 7 9]
print("a * b :", a * b)  # Affiche [ 4 10 18]
print("Produit scalaire :", a @ b)  # Affiche 32

# 2. Ajouter 5 à chaque élément de c
c = np.array([10, 20, 30])
print("c + 5 :", c + 5)  # Affiche [15 25 35]
```

---

### **Exercice 11 : Indexation et slicing**

```python
# 1. Élément à la position (1, 2)
print("Élément (1, 2) :", matrice[1, 2])  # Affiche 6

# 2. Première ligne
print("Première ligne :", matrice[0])  # Affiche [1 2 3]

# 3. Deuxième colonne
print("Deuxième colonne :", matrice[:, 1])  # Affiche [2 5]

# 4. Sous-matrice
print("Sous-matrice :\n", matrice[0:2, 1:3])
# Affiche :
# [[2 3]
#  [5 6]]
```

---

### **Exercice 12 : Modification des tableaux**

```python
# 1. Redimensionner vecteur en 2x3
vecteur = np.arange(6)
matrice_2x3 = vecteur.reshape(2, 3)
print("Matrice 2x3 :\n", matrice_2x3)
# Affiche :
# [[0 1 2]
#  [3 4 5]]

# 2. Transposée
print("Transposée :\n", matrice_2x3.T)
# Affiche :
# [[0 3]
#  [1 4]
#  [2 5]]

# 3. Redimensionner en 3D
d = np.array([1, 2, 3, 4, 5, 6])
d_3d = d.reshape(2, 3, 1)
print("Tableau 3D :\n", d_3d)
# Affiche :
# [[[1]
#   [2]
#   [3]]
#
#  [[4]
#   [5]
#   [6]]]
```

---

### **Exercice 13 : Calculs avancés**

```python
# 1. Calcul de sin(x) et cos(x)
x = np.linspace(0, 2 * np.pi, 100)
sin_x = np.sin(x)
cos_x = np.cos(x)
print("5 premières valeurs de sin(x) :", sin_x[:5])  # Affiche [0.         0.06279052 0.12533323 0.18738131 0.24868989]

# 2. Tableau y = x^2
x = np.arange(0, 11, 1)
y = np.power(x, 2)
print("y = x^2 :", y)  # Affiche [  0   1   4   9  16  25  36  49  64  81 100]
```

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
