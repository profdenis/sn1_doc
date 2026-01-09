# **Corrigés 4 : Boucles `while`**

---

### **Exercice 1 : Prédire la sortie**

1.

```python
i = 1
while i <= 3:
    print(i)
    i += 1
```

**Sortie** :

```
1
2
3
```

2.

```python
mot = "bonjour"
while mot != "au revoir":
    print(mot)
    mot = "au revoir"
```

**Sortie** :

```
bonjour
```

3.

```python
compteur = 0
while compteur < 5:
    compteur += 1
    if compteur == 3:
        continue
    print(compteur)
```

**Sortie** :

```
1
2
4
5
```

---

### **Exercice 2 : Compte à rebours**

```python
n = int(input("Entrez un nombre : "))
while n >= 0:
    print(n)
    n -= 1
```

**Exemple d'exécution** :

```
Entrez un nombre : 5
5
4
3
2
1
0
```

---

### **Exercice 3 : Validation d'entrée**

```python
nombre = int(input("Entrez un nombre entier entre 1 et 10 : "))
while nombre < 1 or nombre > 10:
    nombre = int(input("Nombre invalide. Entrez un nombre entier entre 1 et 10 : "))
print(f"Nombre valide : {nombre}.")
```

**Exemple d'exécution** :

```
Entrez un nombre entier entre 1 et 10 : 15
Nombre invalide. Entrez un nombre entier entre 1 et 10 : 0
Nombre invalide. Entrez un nombre entier entre 1 et 10 : 5
Nombre valide : 5.
```

---

### **Exercice 4 : Somme avec sentinelle**

```python
somme = 0
nombre = float(input("Entrez un nombre (ou 0 pour arrêter) : "))
while nombre != 0:
    somme += nombre
    nombre = float(input("Entrez un nombre (ou 0 pour arrêter) : "))
print(f"La somme est {somme}.")
```

**Exemple d'exécution** :

```
Entrez un nombre (ou 0 pour arrêter) : 5
Entrez un nombre (ou 0 pour arrêter) : 10
Entrez un nombre (ou 0 pour arrêter) : 0
La somme est 15.0.
```

---

### **Exercice 5 : Jeu de devinette**

```python
import random

nombre_a_deviner = random.randint(1, 20)
devine = 0
while devine != nombre_a_deviner:
    devine = int(input("Devinez le nombre entre 1 et 20 : "))
    if devine < nombre_a_deviner:
        print("Trop petit !")
    elif devine > nombre_a_deviner:
        print("Trop grand !")
print("Bravo ! Vous avez trouvé.")
```

**Exemple d'exécution** :

```
Devinez le nombre entre 1 et 20 : 10
Trop grand !
Devinez le nombre entre 1 et 20 : 5
Trop petit !
Devinez le nombre entre 1 et 20 : 7
Bravo ! Vous avez trouvé.
```

---

### **Exercice 6 : Mot de passe**

```python
mot_de_passe = ""
while mot_de_passe != "python123":
    mot_de_passe = input("Entrez le mot de passe : ")
print("Accès autorisé.")
```

**Exemple d'exécution** :

```
Entrez le mot de passe : mauvais
Entrez le mot de passe : python123
Accès autorisé.
```

---

### **Exercice 7 : Calcul de la moyenne**

```python
somme = 0
compteur = 0
note = float(input("Entrez une note (ou -1 pour arrêter) : "))
while note != -1:
    if 0 <= note <= 100:
        somme += note
        compteur += 1
    else:
        print("Note invalide. Veuillez entrer une note entre 0 et 100.")
    note = float(input("Entrez une note (ou -1 pour arrêter) : "))
if compteur > 0:
    moyenne = somme / compteur
    print(f"La moyenne est {moyenne:.2f}.")
else:
    print("Aucune note entrée.")
```

**Exemple d'exécution** :

```
Entrez une note (ou -1 pour arrêter) : 12
Entrez une note (ou -1 pour arrêter) : 15
Entrez une note (ou -1 pour arrêter) : 123
Note invalide. Veuillez entrer une note entre 0 et 100.
Entrez une note (ou -1 pour arrêter) : 18
Entrez une note (ou -1 pour arrêter) : -1
La moyenne est 15.00.
```

---

### **Exercice 8 : Affichage des nombres pairs**

```python
n = int(input("Entrez un nombre : "))
i = 0
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1
```

**Exemple d'exécution** :

```
Entrez un nombre : 10
0
2
4
6
8
10
```

---

### **Exercice 9 : Saisie de nombres positifs**

```python
somme = 0
nombre = float(input("Entrez un nombre positif (ou un nombre négatif pour arrêter) : "))
while nombre >= 0:
    somme += nombre
    nombre = float(input("Entrez un nombre positif (ou un nombre négatif pour arrêter) : "))
print(f"La somme des nombres positifs est {somme}.")
```

**Exemple d'exécution** :

```
Entrez un nombre positif (ou un nombre négatif pour arrêter) : 5
Entrez un nombre positif (ou un nombre négatif pour arrêter) : 10
Entrez un nombre positif (ou un nombre négatif pour arrêter) : -1
La somme des nombres positifs est 15.0.
```

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
