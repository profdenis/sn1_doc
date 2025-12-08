# **Boucles imbriquées**

Les boucles imbriquées consistent à placer une boucle **à l'intérieur d'une autre boucle**. Elles sont utiles pour
traiter des structures de données en deux dimensions, comme des matrices, ou pour générer des motifs complexes.

---

## **1. Boucles `for` imbriquées**

### **1.1 Table de multiplication**

Un exemple classique est la génération d'une table de multiplication.

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end="")  # :4 pour aligner les colonnes
    print()  # Saut de ligne après chaque ligne de la table
```

**Sortie** :

```
   1   2   3   4   5   6   7   8   9  10
   2   4   6   8  10  12  14  16  18  20
   3   6   9  12  15  18  21  24  27  30
   4   8  12  16  20  24  28  32  36  40
   5  10  15  20  25  30  35  40  45  50
   6  12  18  24  30  36  42  48  54  60
   7  14  21  28  35  42  49  56  63  70
   8  16  24  32  40  48  56  64  72  80
   9  18  27  36  45  54  63  72  81  90
  10  20  30  40  50  60  70  80  90 100
```

---

### **1.2 Affichage d'un carré avec des `*`**

```python
n = 5  # Taille du carré
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
```

**Sortie** :

```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

---

### **1.3 Affichage d'un rectangle avec des `*`**

```python
lignes = 4
colonnes = 6
for i in range(lignes):
    for j in range(colonnes):
        print("*", end=" ")
    print()
```

**Sortie** :

```
* * * * * *
* * * * * *
* * * * * *
* * * * * *
```

---

### **1.4 Affichage d'un triangle rectangle**

```python
n = 5  # Hauteur du triangle
for i in range(1, n + 1):
    for j in range(i):
        print("*", end=" ")
    print()
```

**Sortie** :

```
*
* *
* * *
* * * *
* * * * *
```

---

### **1.5 Affichage d'un triangle isocèle**

```python
n = 5  # Hauteur du triangle
for i in range(1, n + 1):
    # Espaces pour centrer le triangle
    print(" " * (n - i), end="")
    # Étoiles pour le triangle
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

**Sortie** :

```
    *
   ***
  *****
 *******
*********
```

---

### **1.6 Affichage d'un losange**

```python
n = 5  # Taille du losange
# Partie supérieure
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
# Partie inférieure
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    for j in range(2 * i - 1):
        print("*", end="")
    print()
```

**Sortie** :

```
    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *
```

---

## **2. Boucles `while` imbriquées**

### **2.1 Table de multiplication avec `while`**

```python
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i * j:4}", end="")
        j += 1
    print()
    i += 1
```

**Sortie** : Identique à la table de multiplication avec `for`.

---

### **2.2 Jeu de devinette avec tentatives limitées**

```python
import random

nombre_a_deviner = random.randint(1, 20)
tentatives_max = 5
tentatives = 0
trouve = False

while tentatives < tentatives_max and not trouve:
    devine = int(input("Devinez le nombre entre 1 et 20 : "))
    tentatives += 1
    if devine == nombre_a_deviner:
        trouve = True
        print(f"Bravo ! Vous avez trouvé en {tentatives} tentatives.")
    elif devine < nombre_a_deviner:
        print("Trop petit !")
    else:
        print("Trop grand !")
else:
    if not trouve:
        print(f"Désolé, vous avez épuisé vos {tentatives_max} tentatives. Le nombre était {nombre_a_deviner}.")
```

**Exemple d'exécution** :

```
Devinez le nombre entre 1 et 20 : 10
Trop grand !
Devinez le nombre entre 1 et 20 : 5
Trop petit !
Devinez le nombre entre 1 et 20 : 7
Bravo ! Vous avez trouvé en 3 tentatives.
```

---

## **3. Exemples avancés**

### **3.1 Matrice d'entiers**

```python
lignes = 3
colonnes = 4
valeur = 1
for i in range(lignes):
    for j in range(colonnes):
        print(f"{valeur:3}", end="")
        valeur += 1
    print()
```

**Sortie** :

```
  1  2  3  4
  5  6  7  8
  9 10 11 12
```

---

### **3.2 Affichage d'un damier**

```python
n = 8  # Taille du damier
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("□", end=" ")
        else:
            print("■", end=" ")
    print()
```

**Sortie** :

```
□ ■ □ ■ □ ■ □ ■
■ □ ■ □ ■ □ ■ □
□ ■ □ ■ □ ■ □ ■
■ □ ■ □ ■ □ ■ □
□ ■ □ ■ □ ■ □ ■
■ □ ■ □ ■ □ ■ □
□ ■ □ ■ □ ■ □ ■
■ □ ■ □ ■ □ ■ □
```

---

### **3.3 Génération de combinaisons**

```python
elements = ["a", "b", "c"]
for i in range(len(elements)):
    for j in range(len(elements)):
        if i != j:
            print(f"{elements[i]}{elements[j]}")
```

**Sortie** :

```
ab
ac
ba
bc
ca
cb
```

---

## **4. Conseils pour utiliser les boucles imbriquées**

### **4.1 Indentation et lisibilité**

- **Indentation claire** : Les boucles imbriquées doivent être **correctement indentées** pour éviter les erreurs de
  syntaxe et améliorer la lisibilité.
- **Commentaires** : Ajoutez des commentaires pour expliquer la logique de chaque niveau de boucle, surtout si les
  boucles sont complexes.

---

### **4.2 Complexité algorithmique**

- **Attention à la complexité** : Les boucles imbriquées augmentent la complexité algorithmique. Par exemple, deux
  boucles imbriquées de taille \( n \) ont une complexité de \( O(n^2) \).
- **Optimisation** : Si possible, cherchez des alternatives pour réduire la complexité (ex. : utiliser des structures de
  données plus efficaces).

---

### **4.3 Éviter les boucles imbriquées profondes**

- **Limitez la profondeur** : Évitez les boucles imbriquées à plus de 2 ou 3 niveaux, car elles rendent le code
  difficile à lire et à maintenir.
- **Refactorisation** : Si une boucle imbriquée devient trop complexe, envisagez de la diviser en fonctions distinctes.

---

## **5. Recommandations pour tester et déboguer les boucles imbriquées**

### **5.1 Tester avec des cas simples**

- **Cas minimaux** : Commencez par tester vos boucles imbriquées avec des **petites tailles** (ex. : `n = 2` ou `n = 3`)
  pour vérifier que la logique de base fonctionne.
- **Exemple** : Pour une table de multiplication, testez d'abord avec `range(1, 4)` au lieu de `range(1, 11)`.

---

### **5.2 Utiliser des `print` pour le débogage**

- **Affichage intermédiaire** : Ajoutez des instructions `print` **à l'intérieur des boucles** pour afficher les valeurs
  des variables à chaque itération. Cela permet de suivre l'exécution pas à pas.
- **Exemple** :
  ```python
  for i in range(3):
      for j in range(2):
          print(f"i = {i}, j = {j}")  # Affiche les valeurs de i et j
  ```
  **Sortie** :
  ```
  i = 0, j = 0
  i = 0, j = 1
  i = 1, j = 0
  i = 1, j = 1
  i = 2, j = 0
  i = 2, j = 1
  ```

---

### **5.3 Utiliser un débogueur**

- **Débogueur intégré** : Utilisez un débogueur (comme celui de **PyCharm** ou **VS Code**) pour exécuter votre code *
  *pas à pas** et inspecter les valeurs des variables.
- **Points d'arrêt** : Placez des points d'arrêt (*breakpoints*) au début des boucles imbriquées pour observer leur
  comportement.

---

### **5.4 Vérifier les conditions de sortie**

- **Boucles infinies** : Assurez-vous que les boucles `while` imbriquées ont une **condition de sortie claire** pour
  éviter les boucles infinies.
- **Exemple de problème** :
  ```python
  i = 0
  while i < 5:
      j = 0
      while j < 5:
          print(f"i = {i}, j = {j}")
          # Oubli de j += 1 → boucle infinie !
  ```
- **Solution** : Toujours mettre à jour les variables de contrôle (`i += 1`, `j += 1`).

---

### **5.5 Tester les cas limites**

- **Valeurs extrêmes** : Testez vos boucles avec des **valeurs extrêmes** (ex. : `n = 0`, `n = 1`, ou des valeurs très
  grandes).
- **Exemple** : Pour un triangle, testez avec `n = 0` et `n = 1` pour vérifier que le programme ne plante pas.

---

### **5.6 Utiliser des assertions**

- **Assertions** : Ajoutez des assertions (`assert`) pour vérifier des invariants ou des conditions attendues à
  l'intérieur des boucles.
- **Exemple** :
  ```python
  somme = 0
  for i in range(10):
      for j in range(i + 1):
          somme += 1
          assert somme <= 55, "La somme dépasse la valeur attendue !"
  print(somme)  # Doit afficher 55 (somme des 10 premiers entiers)
  ```

---

### **5.7 Documenter les boucles complexes**

- **Docstrings et commentaires** : Documentez les boucles imbriquées complexes avec des **commentaires clairs** ou des
  *docstrings* pour expliquer leur objectif et leur logique.
- **Exemple** :
  ```python
  # Génère un triangle isocèle de taille n
  # Chaque ligne contient (2*i - 1) étoiles, centrées avec des espaces
  for i in range(1, n + 1):
      print(" " * (n - i), end="")  # Espaces pour le centrage
      for j in range(2 * i - 1):
          print("*", end="")  # Étoiles pour le triangle
      print()  # Saut de ligne
  ```

---

### **5.8 Exemple complet : Débogage d'une boucle imbriquée**

Voici un exemple de code avec des `print` de débogage pour afficher un carré :

```python
n = 3  # Taille du carré
for i in range(n):
    for j in range(n):
        print(f"({i}, {j})", end=" ")  # Affiche les indices pour déboguer
    print()
```

**Sortie** :

```
(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)
```

---

