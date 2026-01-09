# **Exercices 6 : Les boucles imbriquées**

---

## **Exercices de compréhension**

### **Exercice 1 : Prédire la sortie**

Pour chaque bloc de code, prédisez la sortie **sans utiliser Python**. Ensuite, vérifiez vos réponses en exécutant le
code.

1.

```python
for i in range(2):
    for j in range(3):
        print(f"({i}, {j})", end=" ")
    print()
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

---

## **Exercices de programmation**

### **Exercice 2 : Table de multiplication personnalisée**

Écrivez un programme qui demande à l'utilisateur un nombre `n` et affiche la table de multiplication de `n` jusqu'à 10.

---

### **Exercice 3 : Affichage d'un carré**

Écrivez un programme qui demande à l'utilisateur une taille `n` et affiche un carré de `n x n` étoiles (`*`).

---

### **Exercice 4 : Affichage d'un triangle rectangle**

Écrivez un programme qui demande à l'utilisateur une hauteur `n` et affiche un triangle rectangle de hauteur `n` avec
des étoiles (`*`).

---

### **Exercice 5 : Affichage d'un triangle isocèle**

Écrivez un programme qui demande à l'utilisateur une hauteur `n` et affiche un triangle isocèle de hauteur `n` avec des
étoiles (`*`).

---

### **Exercice 6 : Matrice d'entiers**

Écrivez un programme qui affiche une matrice de 3 lignes et 4 colonnes, où chaque élément est la somme de son indice de
ligne et de colonne.

---

### **Exercice 7 : Damier**

Écrivez un programme qui demande à l'utilisateur une taille `n` et affiche un damier de taille `n x n` en utilisant les
caractères `□` et `■`.

---

### **Exercice 8 : Boucle `while` imbriquée pour un compte à rebours**

Écrivez un programme qui utilise des boucles `while` imbriquées pour afficher un compte à rebours de 3 à 1, trois fois
de suite.

---


### **Exercice 9 : Débogage d'une boucle imbriquée**

Le code suivant est censé afficher un triangle rectangle de hauteur 4, mais il contient une erreur. Trouvez et corrigez
l'erreur.

```python
n = 4
for i in range(n):
    for j in range(i):
        print("*", end="")
    print()
```

---

## **Exercices de débogage**

### **Exercice 10 : Tester et corriger**

Le code suivant est censé afficher un carré de 3x3 étoiles, mais il ne fonctionne pas correctement. Trouvez et corrigez
l'erreur.

```python
n = 3
i = 0
while i < n:
    j = 0
    while j < n:
        print("*", end=" ")
    print()
```

---

### **Exercice 11 : Ajouter des `print` de débogage**

Ajoutez des instructions `print` dans le code suivant pour afficher les valeurs de `i` et `j` à chaque itération. Cela
vous aidera à comprendre comment les boucles imbriquées fonctionnent.

```python
for i in range(2):
    for j in range(3):
        print("*", end=" ")
    print()
```

---

### **Exercice 12 : Vérifier les conditions de sortie**

Le code suivant contient une boucle infinie. Trouvez et corrigez l'erreur.

```python
i = 0
while i < 5:
    j = 0
    while j < 5:
        print(f"({i}, {j})", end=" ")
```

---

---
**Conseils pour les exercices** :

- Utilisez des boucles `for` et `while` imbriquées pour résoudre ces exercices.
- Testez vos programmes avec différentes valeurs pour vérifier leur bon fonctionnement.
- Utilisez des `print` de débogage pour suivre l'exécution des boucles imbriquées.

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
