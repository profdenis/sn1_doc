---
icon: material/checkbox-outline
---

# **1. Les expressions booléennes**

---

## **1. Introduction aux expressions booléennes**

Une **expression booléenne** est une expression qui évalue à **`True`** (vrai) ou **`False`** (faux). Les expressions
booléennes sont utilisées pour prendre des décisions dans les programmes (par exemple, dans les conditions et les
boucles, que nous verrons plus tard).

---

## **2. Opérateurs de comparaison**

Les opérateurs de comparaison permettent de comparer des valeurs. Ils retournent toujours un booléen (`True` ou
`False`).

| **Opérateur** | **Description**     | **Exemple** | **Résultat** |
|---------------|---------------------|-------------|--------------|
| `==`          | Égal à              | `5 == 5`    | `True`       |
| `!=`          | Différent de        | `5 != 3`    | `True`       |
| `<`           | Inférieur à         | `5 < 3`     | `False`      |
| `>`           | Supérieur à         | `5 > 3`     | `True`       |
| `<=`          | Inférieur ou égal à | `5 <= 5`    | `True`       |
| `>=`          | Supérieur ou égal à | `5 >= 10`   | `False`      |

!!! warning "Remarque importante"
    1. **`=`** est un opérateur d'**affectation** 
        - exemple : `x = 5` ➡ la variable `x` obtient la valeur `5`
    2. **`==`** est un opérateur de **comparaison** 
        - exemple : `x == 5` ➡ la valeur de `x` est égale à `5` (vrai ou faux)

---

### **Exemples d'expressions de comparaison**

```python
a = 5
b = 10

print(a == b)  # False
print(a != b)  # True
print(a < b)  # True
print(a > b)  # False
print(a <= b)  # True
print(a >= b)  # False
```

---

## **3. Opérateurs logiques**

Les opérateurs logiques permettent de combiner des expressions booléennes.

| **Opérateur** | **Description**                                                | **Exemple**             | **Résultat** |
|---------------|----------------------------------------------------------------|-------------------------|--------------|
| `and`         | **ET** logique : `True` si les deux expressions sont `True`.   | `(5 < 10) and (10 > 3)` | `True`       |
| `or`          | **OU** logique : `True` si au moins une expression est `True`. | `(5 < 3) or (10 > 5)`   | `True`       |
| `not`         | **NON** logique : Inverse le booléen.                          | `not (5 == 5)`          | `False`      |

---

### **Exemples d'expressions logiques**

```python
x = 5
y = 10
z = 15

print((x < y) and (y < z))  # True
print((x < y) or (y > z))  # True
print(not (x == y))  # True
```

---

## **4. Tables de vérité**

Les tables de vérité montrent toutes les combinaisons possibles de valeurs booléennes pour les opérateurs logiques.

### **Table de vérité pour `and`**

| **A**   | **B**   | **A and B** |
|---------|---------|-------------|
| `True`  | `True`  | `True`      |
| `True`  | `False` | `False`     |
| `False` | `True`  | `False`     |
| `False` | `False` | `False`     |

---

### **Table de vérité pour `or`**

| **A**   | **B**   | **A or B** |
|---------|---------|------------|
| `True`  | `True`  | `True`     |
| `True`  | `False` | `True`     |
| `False` | `True`  | `True`     |
| `False` | `False` | `False`    |

---

### **Table de vérité pour `not`**

| **A**   | **not A** |
|---------|-----------|
| `True`  | `False`   |
| `False` | `True`    |

---

## **5. Exemples d'expressions booléennes**

### **Exemple 1 : Vérification d'un intervalle**

```python
age = 25
est_majeur = age >= 18
print(est_majeur)  # True
```

---

### **Exemple 2 : Combinaison de conditions**

```python
temperature = 22
est_chaud = temperature > 20
est_froid = temperature < 10
print(est_chaud and not est_froid)  # True
```

---

### **Exemple 3 : Vérification de l'égalité**

```python
mot_de_passe = "secret123"
entree_utilisateur = input("Entrez votre mot de passe : ")
acces_autorise = mot_de_passe == entree_utilisateur
print(acces_autorise)  # True si l'entrée utilisateur est "secret123", False sinon
```

---

### **Exemple 4 : Vérification de valeurs multiples**

```python
note = 85
reussi = note >= 60
bien = note >= 75
tres_bien = note >= 90
print(bien or tres_bien)  # True
```

---

### **Exemple 5 : Utilisation de `not`**

```python
note = 85
reussi = note >= 60
echec = not reussi
print(echec)  # False
```

---

### **Exemple 6 : Combinaison complexe**

```python
a = 5
b = 10
c = 15
resultat = (a < b) and (b < c) or (a == c)
print(resultat)  # True
```

---

!!! note "Remarque"
    Ces exemples montrent comment utiliser les expressions booléennes pour évaluer des conditions. Dans les
    prochaines sections, nous verrons comment utiliser ces expressions dans des **structures conditionnelles** et des
    **boucles**.

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
