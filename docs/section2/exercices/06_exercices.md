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

## Exercices supplémentaires

## 1. Affichage de carrés dans la console

Créez un script qui doit afficher des carrés dans la console à l'aide de la fonction `print`.

Commencez par définir une fonction `def afficher_carre(n):` qui va afficher un carré de largeur `n` dans la console. La
bordure du carré doit être faite avec des astérisques `*`, et à l'intérieur du carré, des points `.` doivent être
affichés. Voici un exemple pour `n = 6` :

```text
* * * * * * 
* . . . . *
* . . . . *
* . . . . *
* . . . . *
* * * * * * 
```

Notez que des espaces ont été ajoutés entre les `*` et les `.`, plus précisément exactement un espace entre chaque `*`
et `.` consécutifs. Sur la première ligne, il y a un `*`, suivi d'un espace, suivi d'un `*`, suivi d'un espace...
Similairement, sur la deuxième ligne, il y a un `*`, suivi d'un espace, suivi d'un `.`, suivi d'un espace, suivi
d'un `.`...

Pour tester votre fonction, votre script doit effectuer une boucle pour afficher des carrés de taille 10, 8, 6, et 4
exactement dans cet ordre. Chaque carré doit être précédé d'une ligne indiquant sa largeur, comme dans l'exemple de
sortie donné plus bas.

Ce script ne doit pas utiliser la fonction `input` pour demander des valeurs à l'utilisateur. La sortie produite 
par votre script doit correspondre **exactement** à la sortie suivante.

```text
largeur = 10
* * * * * * * * * * 
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* . . . . . . . . *
* * * * * * * * * * 

largeur = 8
* * * * * * * * 
* . . . . . . *
* . . . . . . *
* . . . . . . *
* . . . . . . *
* . . . . . . *
* . . . . . . *
* * * * * * * * 

largeur = 6
* * * * * * 
* . . . . *
* . . . . *
* . . . . *
* . . . . *
* * * * * * 

largeur = 4
* * * * 
* . . *
* . . *
* * * * 

```

## 2. Logarithme en base 2

Créez un script qui commence par définir une fonction nommée `log_2` qui calcule le logarithme en base 2 d'un
nombre `n` donné en paramètre. Plus précisément, la valeur retournée par la fonction sera le plafond du logarithme en
base 2 de `n`. Le plafond d'un nombre est le plus petit entier supérieur ou égal au nombre. La valeur retournée est 
toujours un nombre entier positif.

Le logarithme en base 2 est l'inverse de la fonction exponentielle en base 2 :

- Exponentielle : $2^x=y$
- Logarithme : $log_2\  y = x$

Ce script ne doit pas utiliser la fonction `input` pour demander des valeurs à l'utilisateur. Le script teste la 
fonction avec des valeurs fixes, comme dans la sortie suivante. La sortie produite par votre script doit 
correspondre **exactement** à la sortie suivante.

```
log_2(32) = 5
log_2(34) = 6
log_2(64) = 6
log_2(100) = 7
log_2(128) = 7
log_2(150) = 8
```

**Vous devez utiliser une boucle pour effectuer le calcul dans la fonction `log_2`. Vous ne pouvez pas utiliser des 
méthodes des modules `math` ou `numpy` ou tout autre module, sauf pour la fonction `ceil`.**

## 3. Somme des n premiers entiers

Créez un script qui doit vérifier empiriquement si la formule qui détermine la somme de tous les 
entiers de 1 jusqu'à `n` inclusivement est correcte.

$$\sum_{i=1}^n i = 1 + 2 + 3 + \cdots + n-1 + n = \frac{n(n+1)}{2}$$

Définissez une fonction qui calcule la somme à l'aide d'une boucle, et une autre fonction qui calcule la somme à 
partir de la formule. Ensuite, pour tester les 2 façons de faire le calcul, faites une boucle qui teste ces 2 
fonctions pour toutes les valeurs de 0 jusqu'à 100 par saut (ou bond ou pas) de 7, comme démontré dans la sortie 
donnée plus bas.

Ce script ne doit pas utiliser la fonction `input` pour demander des valeurs à l'utilisateur. La sortie produite 
par votre script doit correspondre **exactement** à la sortie suivante.

Sortie :

```
somme_boucle(0) == somme_formule(0) == 0
somme_boucle(7) == somme_formule(7) == 28
somme_boucle(14) == somme_formule(14) == 105
somme_boucle(21) == somme_formule(21) == 231
somme_boucle(28) == somme_formule(28) == 406
somme_boucle(35) == somme_formule(35) == 630
somme_boucle(42) == somme_formule(42) == 903
somme_boucle(49) == somme_formule(49) == 1225
somme_boucle(56) == somme_formule(56) == 1596
somme_boucle(63) == somme_formule(63) == 2016
somme_boucle(70) == somme_formule(70) == 2485
somme_boucle(77) == somme_formule(77) == 3003
somme_boucle(84) == somme_formule(84) == 3570
somme_boucle(91) == somme_formule(91) == 4186
somme_boucle(98) == somme_formule(98) == 4851
```


---
**Conseils pour les exercices** :

- Utilisez des boucles `for` et `while`, imbriquées ou non, pour résoudre ces exercices.
- Testez vos programmes avec différentes valeurs pour vérifier leur bon fonctionnement.
- Utilisez des `print` de débogage pour suivre l'exécution des boucles imbriquées.

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
