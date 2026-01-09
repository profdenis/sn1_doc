# **Exercices 1 : Les expressions booléennes**

---

## **Exercices de compréhension**

### **Exercice 1 : Évaluation d'expressions de comparaison**

Calculez mentalement la valeur des expressions suivantes, puis vérifiez vos réponses en utilisant Python si nécessaire.

1. `5 == 5`
2. `10 != 10`
3. `7 < 15`
4. `20 > 30`
5. `15 <= 15`
6. `25 >= 20`

---

### **Exercice 2 : Évaluation d'expressions logiques**

Calculez mentalement la valeur des expressions suivantes, puis vérifiez vos réponses en utilisant Python si nécessaire.

1. `True and False`
2. `True or False`
3. `not True`
4. `(5 < 10) and (10 > 5)`
5. `(5 > 10) or (10 == 10)`
6. `not (15 != 15)`

---

### **Exercice 3 : Tables de vérité**

Complétez les tables de vérité suivantes, puis vérifiez vos réponses en utilisant Python si nécessaire.

#### **Table de vérité pour `A and B`**

| **A**   | **B**   | **A and B** |
|---------|---------|-------------|
| `True`  | `True`  |             |
| `True`  | `False` |             |
| `False` | `True`  |             |
| `False` | `False` |             |

#### **Table de vérité pour `A or B`**

| **A**   | **B**   | **A or B** |
|---------|---------|------------|
| `True`  | `True`  |            |
| `True`  | `False` |            |
| `False` | `True`  |            |
| `False` | `False` |            |

#### **Table de vérité pour `not A`**

| **A**   | **not A** |
|---------|-----------|
| `True`  |           |
| `False` |           |

---

### **Exercice 4 : Combinaisons d'expressions**

Évaluez les expressions suivantes mentalement, puis vérifiez vos réponses en utilisant Python si nécessaire.

1. `(5 < 10) and (10 < 15)`
2. `(5 > 10) or (10 == 10)`
3. `not ((5 == 5) and (10 != 10))`
4. `(15 <= 15) and not (20 >= 30)`
5. `(5 < 10) or (15 > 20) and (10 == 10)`

---

## **Exercices de programmation**

### **Exercice 5 : Vérification des réponses**

Écrivez un programme Python qui évalue les expressions des exercices 1 à 4 et affiche les résultats. Comparez-les avec
vos réponses sans Python.

```python
# Exemple de code pour vérifier les réponses
print(5 == 5)  # True
print(10 != 10)  # False
# Ajoutez les autres expressions ici
```

---

### **Exercice 6 : Évaluation d'expressions personnalisées**

Créez vos propres expressions booléennes (au moins 5) et évaluez-les mentalement. Ensuite, vérifiez vos réponses en
utilisant Python.

---

### **Exercice 7 : Vérification de conditions**

Écrivez un programme qui demande à l'utilisateur deux nombres, puis évalue et affiche les résultats des expressions
suivantes :

1. Les deux nombres sont égaux.
2. Le premier nombre est supérieur au deuxième.
3. Le deuxième nombre est inférieur ou égal au premier.
4. Au moins un des deux nombres est supérieur à 10.

---

### **Exercice 8 : Tables de vérité avec des variables**

Déclarez deux variables booléennes `A` et `B` avec les valeurs `True` et `False`. Évaluez toutes les combinaisons
possibles de `A and B`, `A or B`, et `not A` en utilisant Python.

---

### **Exercice 9 : Expressions booléennes complexes**

Créez des expressions booléennes complexes (au moins 3) en utilisant les opérateurs `and`, `or`, et `not`. Évaluez-les
mentalement, puis vérifiez vos réponses en utilisant Python.

---

### **Exercice 10 : Vérification de conditions multiples**

Écrivez un programme qui demande à l'utilisateur trois nombres, puis évalue et affiche les résultats des expressions
suivantes :

1. Les trois nombres sont égaux.
2. Le premier nombre est le plus grand.
3. Le troisième nombre est le plus petit.
4. La somme des trois nombres est supérieure à 50.

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
