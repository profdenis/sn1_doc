# **Les boucles `while`**

---

## **1. Pourquoi utiliser des boucles ?**

### **1.1 Illustration du besoin d'une boucle**

Imaginons que nous voulons calculer la somme de plusieurs nombres :

- **Sans boucle** :
    - Pour 3 nombres, on peut écrire :
      ```python
      somme = nombre1 + nombre2 + nombre3
      ```
    - Mais pour **100 nombres**, il faudrait écrire une ligne très longue et répétitive :
      ```python
      somme = nombre1 + nombre2 + nombre3 + ... + nombre100
      ```
    - Cela devient **fastidieux, long et source d'erreurs**.

- **Avec une boucle** :
    - On peut écrire un code **concis et réutilisable** pour additionner 100 nombres (ou même 1000 !) sans répéter
      manuellement chaque addition.


---

## **2. Boucle `while` avec condition simple**

### **2.1 Syntaxe de base**

```
while condition:
    # Instructions à répéter tant que la condition est vraie
```

---

### **2.2 Exemple : Compte à rebours**

```python
compteur = 5
while compteur > 0:
    print(compteur)
    compteur -= 1
```

**Sortie** :

```
5
4
3
2
1
```

---

### **2.3 Exemple : Demander une entrée valide**

```python
mot_de_passe = ""
while mot_de_passe != "secret":
    mot_de_passe = input("Entrez le mot de passe : ")
print("Accès autorisé.")
```

**Exemple d'exécution** :

```
Entrez le mot de passe : mauvais
Entrez le mot de passe : secret
Accès autorisé.
```

---

## **3. Boucle `while` avec sentinelle**

Une **sentinelle** est une valeur spéciale qui indique la fin d'une boucle.

### **3.1 Exemple : Somme de nombres jusqu'à une sentinelle**

```python
somme = 0
nombre = 0
while nombre != -1:  # -1 est la sentinelle
    nombre = int(input("Entrez un nombre (ou -1 pour arrêter) : "))
    if nombre != -1:
        somme += nombre
print(f"La somme est {somme}.")
```

**Exemple d'exécution** :

```
Entrez un nombre (ou -1 pour arrêter) : 5
Entrez un nombre (ou -1 pour arrêter) : 10
Entrez un nombre (ou -1 pour arrêter) : -1
La somme est 15.
```

### **3.2 Variations sur l'exemple précédent**

Un léger problème avec le problème précédent est que la condition `nombre != -1` doit être utilisée deux fois : la
première pour la condition de la boucle, et l'autre pour s'assurer de ne pas ajouter `-1` à la somme. Une
alternative serait de remplacer la condition `nombre != -1` par `nombre != 0`, parce qu'ajouter 0 à une somme ne
change pas sa valeur de toute façon. Dans ce cas, la sentinelle devient 0 et le `if` dans la boucle devient inutile.

```python
somme = 0
nombre = -1
while nombre != 0:  # 0 est la sentinelle
    nombre = int(input("Entrez un nombre (ou 0 pour arrêter) : "))
    somme += nombre
print(f"La somme est {somme}.")
```

Une autre alternative serait de remplacer la condition de la boucle par `not terminé`, avec `terminé` initialisée à
`False` avant la boucle, comme dans le code suivant :

```python
somme = 0
terminé = False
while not terminé:
    nombre = int(input("Entrez un nombre (ou 0 pour arrêter) : "))
    if nombre == 0:
        terminé = True
    else:
        somme += nombre
print(f"La somme est {somme}.")
```

!!! warning "Nom des variables"
    Même s'il est possible d'utiliser des caractères accentués dans les noms de variables en Python, il est 
    généralement préférable d'utiliser des noms sans accents et sans caractères autres que les lettres de l'alphabet 
    (minuscules ou majuscules, de `a` à `z`) et le souligné (`_`), pour s'assurer que le code est facile à lire et à 
    comprendre, et qu'il n'y aie pas de problèmes d'encodage des caractères.

!!! note "Erreurs d'entrée"
    La gestion des erreurs d'entrée sera présentée dans une section ultérieure.

---

## **4. Boucle `while True` avec `break` et `continue`**

### **4.1 Utilisation de `break`**

- **`break`** : Sort immédiatement de la boucle.

```python
while True:
    nom = input("Entrez un nom (ou 'quitter' pour arrêter) : ")
    if nom.lower() == "quitter":
        break
    print(f"Bonjour, {nom} !")
```

**Exemple d'exécution** :

```
Entrez un nom (ou 'quitter' pour arrêter) : Alice
Bonjour, Alice !
Entrez un nom (ou 'quitter' pour arrêter) : quitter
```

---

### **4.2 Utilisation de `continue`**

- **`continue`** : Passe à l'itération suivante sans exécuter le reste du bloc.

```python
compteur = 0
while compteur < 5:
    compteur += 1
    if compteur == 3:
        continue  # Saute l'itération où compteur == 3
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

!!! warning "Remarque sur `while True`"
    - **À utiliser avec parcimonie** : Peut rendre le code moins lisible.
    - **Préférer une condition claire** quand c'est possible.
    - En général, **if faut donc éviter les boucles `while True`, et essayer d'utiliser `break` et `continue` le moins 
    possible**, pour écrire du code plus lisible et moins complexe.

---

## **5. Exemples pratiques**

### **5.1 Boucle `while` pour valider une entrée**

```python
age = -1
while age < 0 or age > 120:
    age = int(input("Entrez un âge valide (0-120) : "))
print(f"Âge valide : {age}.")
```

**Exemple d'exécution** :

```
Entrez un âge valide (0-120) : -5
Entrez un âge valide (0-120) : 150
Entrez un âge valide (0-120) : 30
Âge valide : 30.
```

---

### **5.2 Boucle `while` pour un jeu de devinette**

```python
import random

nombre_a_deviner = random.randint(1, 10)
devine = 0
while devine != nombre_a_deviner:
    devine = int(input("Devinez le nombre entre 1 et 10 : "))
    if devine < nombre_a_deviner:
        print("Trop petit !")
    elif devine > nombre_a_deviner:
        print("Trop grand !")
print("Bravo ! Vous avez trouvé.")
```

**Exemple d'exécution** :

```
Devinez le nombre entre 1 et 10 : 5
Trop grand !
Devinez le nombre entre 1 et 10 : 2
Trop petit !
Devinez le nombre entre 1 et 10 : 3
Bravo ! Vous avez trouvé.
```

---

### **5.3 Boucle `while` avec `break` pour une recherche**

```python
nombres = [2, 5, 8, 12, 16]
recherche = 12
trouve = False
index = 0
while index < len(nombres):
    if nombres[index] == recherche:
        trouve = True
        break
    index += 1
print(f"Nombre trouvé : {trouve}")
```

**Sortie** :

```
Nombre trouvé : True
```

!!! note "Remarque"
    Dans cet exemple, il est justifié d'utiliser `break`, car nous voulons sortir de la boucle dès que nous trouvons le 
    nombre recherché. De cette façon, nous évitons de parcourir la liste entière, potentiellement très grande, 
    inutilement si le nombre est trouvé rapidement. Également, en sortant immédiatement de la boucle, on trouvera la 
    première occurrence du nombre recherché.

---

## **6. Boucle `while ... else ...`**

En Python, la boucle `while` peut être suivie d'un bloc `else`. Ce bloc `else` est exécuté **uniquement si la
boucle `while` se termine sans rencontrer de `break`**.

### **Syntaxe**

```
while condition:
    # Instructions à exécuter tant que la condition est vraie
else:
    # Instructions à exécuter si la boucle se termine sans `break`
```

---

### **Exemple 1 : Recherche d'un élément dans une liste**

Imaginons que nous voulons vérifier si un nombre est présent dans une liste. Si le nombre est trouvé, nous utilisons
`break` pour sortir de la boucle. Sinon, le bloc `else` est exécuté pour indiquer que le nombre n'a pas été trouvé.

```python
nombres = [2, 5, 8, 12, 16]
recherche = 10
index = 0
trouve = False

while index < len(nombres):
    if nombres[index] == recherche:
        trouve = True
        print(f"Le nombre {recherche} a été trouvé à l'index {index}.")
        break
    index += 1
else:
    print(f"Le nombre {recherche} n'a pas été trouvé dans la liste.")
```

**Sortie** :

```
Le nombre 10 n'a pas été trouvé dans la liste.
```

---

### **Exemple 2 : Validation d'une entrée utilisateur**

Dans cet exemple, nous demandons à l'utilisateur d'entrer un nombre pair. Si l'utilisateur entre un nombre impair, la
boucle continue. Si l'utilisateur entre un nombre pair, la boucle se termine et le bloc `else` est exécuté.

```python
nombre = int(input("Entrez un nombre pair : "))
while nombre % 2 != 0:
    print(f"{nombre} est impair. Essayez encore.")
    nombre = int(input("Entrez un nombre pair : "))
else:
    print(f"Merci ! {nombre} est un nombre pair.")
```

**Exemple d'exécution** :

```
Entrez un nombre pair : 3
3 est impair. Essayez encore.
Entrez un nombre pair : 5
5 est impair. Essayez encore.
Entrez un nombre pair : 4
Merci ! 4 est un nombre pair.
```

---

### **Cas d'utilisation typiques**

1. **Recherche d'un élément** : Le bloc `else` permet d'indiquer que l'élément recherché n'a pas été trouvé.
2. **Validation d'une entrée** : Le bloc `else` permet de confirmer que l'entrée est valide après plusieurs tentatives.

---

### **Remarques importantes**

- Le bloc `else` **ne s'exécute pas** si la boucle `while` est interrompue par un `break`.
- Cette structure est **unique à Python** et n'existe pas dans la plupart des autres langages de programmation.

---
