# **Corrigés 5 : Boucles `for`**

---

### **Exercice 1 : Prédire la sortie**

1.

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

2.

```python
for fruit in ["pomme", "banane", "cerise"]:
    print(fruit)
```

**Sortie** :

```
pomme
banane
cerise
```

3.

```python
for i in range(2, 6):
    print(i * 2)
```

**Sortie** :

```
4
6
8
10
```

4.

```python
for i in range(0, 10, 3):
    print(i)
```

**Sortie** :

```
0
3
6
9
```

---

### **Exercice 2 : Compléter le code**

1. **Sortie attendue :**
   ```
   10
   9
   8
   ```
   **Code complété :**
   ```python
   for i in range(10, 7, -1):
       print(i)
   ```

2. **Sortie attendue :**
   ```
   0
   2
   4
   6
   ```
   **Code complété :**
   ```python
   for i in range(0, 7, 2):
       print(i)
   ```

---

### **Exercice 3 : Afficher les éléments d'une liste**

```python
couleurs = ["rouge", "vert", "bleu", "jaune"]
for couleur in couleurs:
    print(couleur)
```

**Sortie** :

```
rouge
vert
bleu
jaune
```

---

### **Exercice 4 : Calculer la somme des éléments d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
somme = 0
for nombre in nombres:
    somme += nombre
print(f"La somme est {somme}.")
```

**Sortie** :

```
La somme est 150.
```

---

### **Exercice 5 : Afficher les nombres pairs de 0 à 20**

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

### **Exercice 6 : Compter à rebours de 10 à 0**

```python
for i in range(10, -1, -1):
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
0
```

---

### **Exercice 7 : Calculer la factorielle d'un nombre**

```python
n = int(input("Entrez un nombre entier positif : "))
factorielle = 1
for i in range(1, n + 1):
    factorielle *= i
print(f"La factorielle de {n} est {factorielle}.")
```

**Exemple de sortie pour `n = 5`** :

```
La factorielle de 5 est 120.
```

---

### **Exercice 8 : Afficher les multiples de 5 de 0 à 50**

```python
for i in range(0, 51, 5):
    print(i)
```

**Sortie** :

```
0
5
10
15
20
25
30
35
40
45
50
```

---

### **Exercice 9 : Calculer la moyenne d'une liste**

```python
notes = [12, 15, 18, 9, 20]
somme = 0
for note in notes:
    somme += note
moyenne = somme / len(notes)
print(f"La moyenne est {moyenne:.2f}.")
```

**Sortie** :

```
La moyenne est 14.80.
```

---

### **Exercice 10 : Afficher un motif simple**

```python
for i in range(1, 6):
    print('*' * i)
```

**Sortie** :

```
*
**
***
****
*****
```

---

### **Exercice 11 : Afficher les carrés des nombres de 1 à 10**

```python
for i in range(1, 11):
    print(f"{i} au carré est {i ** 2}.")
```

**Sortie** :

```
1 au carré est 1.
2 au carré est 4.
3 au carré est 9.
4 au carré est 16.
5 au carré est 25.
6 au carré est 36.
7 au carré est 49.
8 au carré est 64.
9 au carré est 81.
10 au carré est 100.
```

---

### **Exercice 12 : Trouver le plus grand élément d'une liste**

```python
nombres = [12, 45, 67, 23, 9, 56, 78]
plus_grand = nombres[0]
for nombre in nombres:
    if nombre > plus_grand:
        plus_grand = nombre
print(f"Le plus grand élément est {plus_grand}.")
```

**Sortie** :

```
Le plus grand élément est 78.
```

---

### **Exercice 13 : Afficher les éléments d'une liste à l'envers**

```python
villes = ["Paris", "Lyon", "Marseille", "Toulouse"]
for i in range(len(villes) - 1, -1, -1):
    print(villes[i])
```

**Sortie** :

```
Toulouse
Marseille
Lyon
Paris
```

---

### **Exercice 14 : Calculer la somme des carrés des nombres de 1 à 10**

```python
somme = 0
for i in range(1, 11):
    somme += i ** 2
print(f"La somme des carrés est {somme}.")
```

**Sortie** :

```
La somme des carrés est 385.
```

---

### **Exercice 15 : Afficher les éléments d'une liste avec leur index**

```python
fruits = ["pomme", "banane", "cerise", "orange"]
for index in range(len(fruits)):
    print(f"{index} : {fruits[index]}")
```

**Sortie** :

```
0 : pomme
1 : banane
2 : cerise
3 : orange
```

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
