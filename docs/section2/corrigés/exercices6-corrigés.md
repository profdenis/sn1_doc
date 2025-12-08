# **Corrigés 6 : Boucles imbriquées**

---

## **Exercice 1 : Prédire la sortie**

1.

```python
for i in range(2):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
```

**Sortie** :

```
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
```

2.

```python
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"{i}*{j}={i * j}", end=" ")
        j += 1
    print()
    i += 1
```

**Sortie** :

```
1*1=1 1*2=2
2*1=2 2*2=4
3*1=3 3*2=6
```

---

## **Exercice 2 : Table de multiplication personnalisée**

```python
n = int(input("Entrez un nombre : "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

**Exemple d'exécution** :

```
Entrez un nombre : 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

## **Exercice 3 : Affichage d'un carré**

```python
n = int(input("Entrez la taille du carré : "))
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

**Exemple d'exécution** :

```
Entrez la taille du carré : 4
* * * *
* * * *
* * * *
* * * *
```

---

## **Exercice 4 : Affichage d'un triangle rectangle**

```python
n = int(input("Entrez la hauteur du triangle : "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Exemple d'exécution** :

```
Entrez la hauteur du triangle : 5
*
* *
* * *
* * * *
* * * * *
```

---

## **Exercice 5 : Affichage d'un triangle isocèle**

```python
n = int(input("Entrez la hauteur du triangle : "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

**Exemple d'exécution** :

```
Entrez la hauteur du triangle : 4
   *
  ***
 *****
*******
```

---

## **Exercice 6 : Matrice d'entiers**

```python
for i in range(3):
    for j in range(4):
        print(f"{i + j:3}", end="")
    print()
```

**Sortie** :

```
  0  1  2  3
  1  2  3  4
  2  3  4  5
```

---

## **Exercice 7 : Damier**

```python
n = int(input("Entrez la taille du damier : "))
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("□", end=" ")
        else:
            print("■", end=" ")
    print()
```

**Exemple d'exécution** :

```
Entrez la taille du damier : 4
□ ■ □ ■
■ □ ■ □
□ ■ □ ■
■ □ ■ □
```

---

## **Exercice 8 : Boucle `while` imbriquée pour un compte à rebours**

```python
compteur_externe = 3
while compteur_externe > 0:
    compteur_interne = 3
    while compteur_interne > 0:
        print(compteur_interne, end=" ")
        compteur_interne -= 1
    print()
    compteur_externe -= 1
```

**Sortie** :

```
3 2 1
3 2 1
3 2 1
```

---

## **Exercice 9 : Recherche dans une matrice**

```python
matrice = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
recherche = int(input("Entrez un nombre à rechercher : "))
trouve = False
for i in range(3):
    for j in range(3):
        if matrice[i][j] == recherche:
            trouve = True
            break
    if trouve:
        break
if trouve:
    print(f"Le nombre {recherche} a été trouvé.")
else:
    print(f"Le nombre {recherche} n'a pas été trouvé.")
```

**Exemple d'exécution** :

```
Entrez un nombre à rechercher : 5
Le nombre 5 a été trouvé.
```

---

## **Exercice 10 : Débogage d'une boucle imbriquée**

**Problème** : Le code affiche un triangle rectangle de hauteur `n-1` au lieu de `n`.
**Correction** : La boucle interne doit aller jusqu'à `i+1` pour inclure la dernière ligne.

```python
n = 4
for i in range(n):
    for j in range(i + 1):  # Correction : i + 1 au lieu de i
        print("*", end="")
    print()
```

**Sortie corrigée** :

```
*
**
***
****
```

---

## **Exercice 11 : Tester et corriger**

**Problème** : La boucle interne n'incrémente pas `j`, ce qui crée une boucle infinie.
**Correction** : Ajouter `j += 1` dans la boucle interne.

```python
n = 3
i = 0
while i < n:
    j = 0
    while j < n:
        print("*", end=" ")
        j += 1  # Correction : Incrémentation de j
    print()
    i += 1
```

**Sortie corrigée** :

```
* * *
* * *
* * *
```

---

## **Exercice 12 : Ajouter des `print` de débogage**

```python
for i in range(2):
    for j in range(3):
        print(f"(i={i}, j={j})", end=" ")  # Ajout des valeurs de i et j
        print("*", end=" ")
    print()
```

**Sortie** :

```
(i=0, j=0) * (i=0, j=1) * (i=0, j=2) *
(i=1, j=0) * (i=1, j=1) * (i=1, j=2) *
```

---

## **Exercice 13 : Vérifier les conditions de sortie**

**Problème** : La boucle interne n'incrémente pas `j`, ce qui crée une boucle infinie.
**Correction** : Ajouter `j += 1` dans la boucle interne.

```python
i = 0
while i < 5:
    j = 0
    while j < 5:
        print(f"({i}, {j})", end=" ")
        j += 1  # Correction : Incrémentation de j
    print()
    i += 1
```

**Sortie corrigée** :

```
(0, 0) (0, 1) (0, 2) (0, 3) (0, 4)
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4)
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4)
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4)
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4)
```

---
**Conseils pédagogiques** :

- Encouragez les étudiants à **tester chaque programme** avec différentes valeurs pour vérifier leur bon fonctionnement.
- Ils peuvent aussi **modifier les exercices** pour explorer d'autres cas ou ajouter des fonctionnalités.

---
