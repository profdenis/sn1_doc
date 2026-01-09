# **Corrigés 1 : Expressions booléennes**

---

## **Exercices de compréhension**

---

### **Exercice 1 : Évaluation d'expressions de comparaison**

| **Expression** | **Résultat (à la main)** | **Vérification avec Python** |
|----------------|--------------------------|------------------------------|
| `5 == 5`       | `True`                   | `print(5 == 5)` → `True`     |
| `10 != 10`     | `False`                  | `print(10 != 10)` → `False`  |
| `7 < 15`       | `True`                   | `print(7 < 15)` → `True`     |
| `20 > 30`      | `False`                  | `print(20 > 30)` → `False`   |
| `15 <= 15`     | `True`                   | `print(15 <= 15)` → `True`   |
| `25 >= 20`     | `True`                   | `print(25 >= 20)` → `True`   |

---

### **Exercice 2 : Évaluation d'expressions logiques**

| **Expression**           | **Résultat (à la main)** | **Vérification avec Python**             |
|--------------------------|--------------------------|------------------------------------------|
| `True and False`         | `False`                  | `print(True and False)` → `False`        |
| `True or False`          | `True`                   | `print(True or False)` → `True`          |
| `not True`               | `False`                  | `print(not True)` → `False`              |
| `(5 < 10) and (10 > 5)`  | `True`                   | `print((5 < 10) and (10 > 5))` → `True`  |
| `(5 > 10) or (10 == 10)` | `True`                   | `print((5 > 10) or (10 == 10))` → `True` |
| `not (15 != 15)`         | `True`                   | `print(not (15 != 15))` → `True`         |

---

### **Exercice 3 : Tables de vérité**

#### **Table de vérité pour `A and B`**

| **A**   | **B**   | **A and B** (à la main) | **Vérification avec Python**       |
|---------|---------|-------------------------|------------------------------------|
| `True`  | `True`  | `True`                  | `print(True and True)` → `True`    |
| `True`  | `False` | `False`                 | `print(True and False)` → `False`  |
| `False` | `True`  | `False`                 | `print(False and True)` → `False`  |
| `False` | `False` | `False`                 | `print(False and False)` → `False` |

---

#### **Table de vérité pour `A or B`**

| **A**   | **B**   | **A or B** (à la main) | **Vérification avec Python**      |
|---------|---------|------------------------|-----------------------------------|
| `True`  | `True`  | `True`                 | `print(True or True)` → `True`    |
| `True`  | `False` | `True`                 | `print(True or False)` → `True`   |
| `False` | `True`  | `True`                 | `print(False or True)` → `True`   |
| `False` | `False` | `False`                | `print(False or False)` → `False` |

---

#### **Table de vérité pour `not A`**

| **A**   | **not A** (à la main) | **Vérification avec Python** |
|---------|-----------------------|------------------------------|
| `True`  | `False`               | `print(not True)` → `False`  |
| `False` | `True`                | `print(not False)` → `True`  |

---

### **Exercice 4 : Combinaisons d'expressions**

| **Expression**                         | **Résultat (à la main)** | **Vérification avec Python**                           |
|----------------------------------------|--------------------------|--------------------------------------------------------|
| `(5 < 10) and (10 < 15)`               | `True`                   | `print((5 < 10) and (10 < 15))` → `True`               |
| `(5 > 10) or (10 == 10)`               | `True`                   | `print((5 > 10) or (10 == 10))` → `True`               |
| `not ((5 == 5) and (10 != 10))`        | `True`                   | `print(not ((5 == 5) and (10 != 10)))` → `True`        |
| `(15 <= 15) and not (20 >= 30)`        | `True`                   | `print((15 <= 15) and not (20 >= 30))` → `True`        |
| `(5 < 10) or (15 > 20) and (10 == 10)` | `True`                   | `print((5 < 10) or (15 > 20) and (10 == 10))` → `True` |

---

## **Exercices de programmation**

---

### **Exercice 5 : Vérification des réponses**

```python
# Vérification des réponses des exercices 1 à 4
print(5 == 5)  # True
print(10 != 10)  # False
print(7 < 15)  # True
print(20 > 30)  # False
print(15 <= 15)  # True
print(25 >= 20)  # True

print(True and False)  # False
print(True or False)  # True
print(not True)  # False
print((5 < 10) and (10 > 5))  # True
print((5 > 10) or (10 == 10))  # True
print(not (15 != 15))  # True

print((5 < 10) and (10 < 15))  # True
print((5 > 10) or (10 == 10))  # True
print(not ((5 == 5) and (10 != 10)))  # True
print((15 <= 15) and not (20 >= 30))  # True
print((5 < 10) or (15 > 20) and (10 == 10))  # True
```

---

### **Exercice 6 : Évaluation d'expressions personnalisées**

Voici 5 exemples d'expressions booléennes personnalisées :

| **Expression**                    | **Résultat (à la main)** | **Vérification avec Python**                      |
|-----------------------------------|--------------------------|---------------------------------------------------|
| `(10 > 5) and (5 < 10)`           | `True`                   | `print((10 > 5) and (5 < 10))` → `True`           |
| `not (20 == 20)`                  | `False`                  | `print(not (20 == 20))` → `False`                 |
| `(15 >= 10) or (15 <= 10)`        | `True`                   | `print((15 >= 10) or (15 <= 10))` → `True`        |
| `(3 * 5 == 15) and (15 / 3 == 5)` | `True`                   | `print((3 * 5 == 15) and (15 / 3 == 5))` → `True` |
| `not (10 != 10)`                  | `True`                   | `print(not (10 != 10))` → `True`                  |

---

### **Exercice 7 : Vérification de conditions**

```python
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

print(nombre1 == nombre2)
print(nombre1 > nombre2)
print(nombre2 <= nombre1)
print((nombre1 > 10) or (nombre2 > 10))
```

---

### **Exercice 8 : Tables de vérité avec des variables**

```python
A = True
B = False

print(A and B)  # False
print(A or B)  # True
print(not A)  # False
print(not B)  # True
```

---

### **Exercice 9 : Expressions booléennes complexes**

Voici 3 exemples d'expressions booléennes complexes :

| **Expression**                            | **Résultat (à la main)** | **Vérification avec Python**                               |
|-------------------------------------------|--------------------------|------------------------------------------------------------|
| `(10 > 5) and not (15 < 10)`              | `True`                   | `print((10 > 5) and not (15 < 10))` → `True`               |
| `(20 == 20) or ((5 * 2) != 10)`           | `True`                   | `print((20 == 20) or ((5 * 2) != 10))` → `True`            |
| `not ((10 + 5) == 15) and (20 / 2 == 10)` | `False`                  | `print(not ((10 + 5) == 15) and (20 / 2 == 10))` → `False` |

---

### **Exercice 10 : Vérification de conditions multiples**

```python
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))
nombre3 = float(input("Entrez le troisième nombre : "))

print(nombre1 == nombre2 == nombre3)
print(nombre1 > nombre2 and nombre1 > nombre3)
print(nombre3 < nombre1 and nombre3 < nombre2)
print((nombre1 + nombre2 + nombre3) > 50)
```

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
