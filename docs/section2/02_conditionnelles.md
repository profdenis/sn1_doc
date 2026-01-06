# **Les structures conditionnelles**

Les structures conditionnelles permettent d'exécuter des blocs de code en fonction de conditions spécifiques. Elles sont
essentielles pour créer des programmes dynamiques et réactifs.

---

## **1. Structure `if` seule**

La structure `if` permet d'exécuter un bloc de code **uniquement si une condition est vraie**.

### **Syntaxe**

```
if condition:
    # Instructions à exécuter si la condition est vraie
```

### **Exemple 1 : Vérification d'un nombre positif**

```python
nombre = 10
if nombre > 0:
    print(f"{nombre} est un nombre positif.")
```

**Sortie** :

```
10 est un nombre positif.
```

---

### **Exemple 2 : Vérification de l'égalité**

```python
mot_de_passe = "secret123"
entree_utilisateur = input("Entrez le mot de passe : ")
if mot_de_passe == entree_utilisateur:
    print("Accès autorisé.")
```

**Sortie possible** :

```
Entrez le mot de passe : secret123
Accès autorisé.
```

---

## **2. Structure `if ... else ...`**

La structure `if ... else ...` permet d'exécuter un bloc de code si la condition est vraie, et un autre bloc si elle est
fausse.

### **Syntaxe**

```
if condition:
    # Instructions si la condition est vraie
else:
    # Instructions si la condition est fausse
```

---

### **Exemple 1 : Vérification de la majorité**

```python
age = 17
if age >= 18:
    print("Vous êtes majeur.")
else:
    print("Vous êtes mineur.")
```

**Sortie** :

```
Vous êtes mineur.
```

---

### **Exemple 2 : Comparaison de deux nombres**

```python
a = 10
b = 20
if a > b:
    print(f"{a} est supérieur à {b}.")
else:
    print(f"{a} n'est pas supérieur à {b}.")
```

**Sortie** :

```
10 n'est pas supérieur à 20.
```

---

## **3. Structure `if ... elif ... else`**

La structure `if ... elif ... else` permet de tester plusieurs conditions et d'exécuter le bloc de code correspondant à
la première condition vraie.

### **Syntaxe**

```
if condition1:
    # Instructions si condition1 est vraie
elif condition2:
    # Instructions si condition2 est vraie
else:
    # Instructions si aucune condition n'est vraie
```

---

### **Exemple 1 : Catégorisation d'un nombre**

```python
nombre = 0
if nombre > 0:
    print(f"{nombre} est positif.")
elif nombre < 0:
    print(f"{nombre} est négatif.")
else:
    print(f"{nombre} est nul.")
```

**Sortie** :

```
0 est nul.
```

---

### **Exemple 2 : Évaluation d'une note**

```python
note = 85
if note >= 90:
    print("Très bien !")
elif note >= 80:
    print("Bien.")
elif note >= 70:
    print("Assez bien.")
elif note >= 60:
    print("Passable.")
else:
    print("Insuffisant.")
```

**Sortie** :

```
Bien.
```

---

### **Exemple 3 : Vérification de conditions multiples**

```python
a = 10
b = 15
c = 20
if a > b and a > c:
    print(f"{a} est le plus grand.")
elif b > a and b > c:
    print(f"{b} est le plus grand.")
else:
    print(f"{c} est le plus grand.")
```

**Sortie** :

```
20 est le plus grand.
```

---

### **Exemple 4 : Utilisation d'expressions booléennes complexes**

```python
temperature = 25
if temperature > 30:
    print("Il fait très chaud.")
elif temperature > 20:
    print("Il fait chaud.")
elif temperature > 10:
    print("Il fait doux.")
else:
    print("Il fait froid.")
```

**Sortie** :

```
Il fait chaud.
```

---

## **4. Résumé des structures conditionnelles**

| **Structure**          | **Utilisation**                                                                            |
|------------------------|--------------------------------------------------------------------------------------------|
| `if`                   | Exécute un bloc de code si une condition est vraie.                                        |
| `if ... else ...`      | Exécute un bloc de code si une condition est vraie, sinon exécute un autre bloc.           |
| `if ... elif ... else` | Teste plusieurs conditions et exécute le bloc correspondant à la première condition vraie. |

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
