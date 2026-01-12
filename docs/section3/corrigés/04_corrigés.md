# **Corrigés 4 : Lecture et écriture de fichiers**

---

## **Exercices de compréhension**

### **Exercice 1 : Prédire la sortie**

1.

```python
with open("test.txt", "w") as fichier:
    fichier.write("Bonjour\n")
    fichier.write("Python\n")

with open("test.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
```

**Sortie** :

```
Bonjour
Python
```

2.

```python
with open("nombres.txt", "w") as fichier:
    fichier.write("10\n")
    fichier.write("20\n")
    fichier.write("30\n")

with open("nombres.txt", "r") as fichier:
    for ligne in fichier:
        print(int(ligne) * 2)
```

**Sortie** :

```
20
40
60
```

3.

```python
with open("nombres.txt", "w") as fichier:
    fichier.write("10\n")
    fichier.write("20\n")
    fichier.write("30\n")

with open("nombres.txt", "r") as fichier:
    for ligne in fichier:
        print(ligne * 2)
```

**Sortie** :

```
10
10

20
20

30
30

```

!!! note "Remarque"
    Sans conversion en entier, `ligne * 2` double la chaîne de caractères `ligne`, qui est `10\n` pour la première 
    ligne, donc qui devient `10\n10\n`. Avec le `\n` supplémentaire ajouté à la fin par `print`, chaque appel à `print`
    affiche 3 lignes sur la sortie standard.

---

## **Exercices de lecture de fichiers**

### **Exercice 2 : Lire un fichier texte**

```python
with open("poeme.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
```

---

### **Exercice 3 : Lire un fichier ligne par ligne**

```python
index = 1
with open("villes.txt", "r") as fichier:
    for ligne in fichier:
        print(f"{index}: {ligne.strip()}")
        index += 1
```

#### Avec `enumerate`

```python
with open("villes.txt", "r") as fichier:
    for index, ligne in enumerate(fichier, start=1):
        print(f"{index}: {ligne.strip()}")
```

---

### **Exercice 4 : Calculer la somme des nombres dans un fichier**

```python
somme = 0.0
compteur = 0 # Pour compter le nombre de nombres valides

with open("nombres.txt", "r") as fichier:
    for ligne in fichier:
        try:
            nombre = float(ligne)
            somme += nombre
            compteur += 1 # On incrémente à chaque nombre valide trouvé
        except ValueError:
            print(f"Ligne ignorée : {ligne.strip()} (n'est pas un nombre)")

# On vérifie que le compteur n'est pas à zéro pour éviter une division par zéro
if compteur > 0:
    moyenne = somme / compteur
    print(f"La moyenne est {moyenne}.")
else:
    print("Aucun nombre valide n'a été trouvé pour calculer une moyenne.")
```

---

### **Exercice 5 : Lire une liste de nombres**

```python
def lire_nombres(nom_fichier):
    nombres = []
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            try:
                nombre = float(ligne)
                nombres.append(nombre)
            except ValueError:
                print(f"Ligne ignorée : {ligne.strip()} (n'est pas un nombre)")
    return nombres


nombres = lire_nombres("nombres.txt")
print(f"Liste des nombres : {nombres}")
```

---

### **Exercice 6 : Compter les mots dans un fichier**

```python
with open("texte.txt", "r") as fichier:
    contenu = fichier.read()
    mots = contenu.split()
    print(f"Nombre de mots : {len(mots)}")
```

---

### **Exercice 7 : Trouver le mot le plus long**

```python
mot_le_plus_long = ""
with open("mots.txt", "r") as fichier:
    for ligne in fichier:
        mot = ligne.strip()
        if len(mot) > len(mot_le_plus_long):
            mot_le_plus_long = mot
print(f"Mot le plus long : {mot_le_plus_long}")
```

---

## **Exercices d'écriture de fichiers**

### **Exercice 8 : Écrire dans un fichier**

```python
with open("utilisateur.txt", "w") as fichier:
    for i in range(3):
        ligne = input(f"Entrez la ligne {i + 1} : ")
        fichier.write(ligne + "\n")
```

---

### **Exercice 9 : Ajouter à un fichier**

```python
with open("journal.txt", "a") as fichier:
    for i in range(3):
        ligne = input(f"Entrez la ligne {i + 1} à ajouter : ")
        fichier.write(ligne + "\n")
```

---

### **Exercice 10 : Écrire une liste de nombres**

```python
nombres = [1.5, 2.5, 3.5, 4.5]
with open("nombres_sortie.txt", "w") as fichier:
    for nombre in nombres:
        fichier.write(f"{nombre}\n")
```

---

### **Exercice 11 : Écrire une liste de chaînes**

```python
mots = ["pomme", "banane", "cerise", "datte"]
with open("fruits.txt", "w") as fichier:
    for mot in mots:
        fichier.write(f"{mot}\n")
```

---

## **Exercices combinés (lecture et écriture)**

### **Exercice 12 : Copier un fichier**

```python
with open("source.txt", "r") as source, open("destination.txt", "w") as destination:
    contenu = source.read()
    destination.write(contenu)
```

---

### **Exercice 13 : Inverser les lignes d'un fichier**

```python
with open("entree.txt", "r") as entree:
    lignes = entree.readlines()

with open("sortie.txt", "w") as sortie:
    for ligne in reversed(lignes):
        sortie.write(ligne)
```

---

### **Exercice 14 : Filtrer les nombres pairs**

```python
with open("nombres.txt", "r") as entree, open("pairs.txt", "w") as sortie:
    for ligne in entree:
        try:
            nombre = int(ligne)
            if nombre % 2 == 0:
                sortie.write(ligne)
        except ValueError:
            continue
```

---


### **Exercice 15 : Fusionner deux fichiers**

```python
with open("fichier1.txt", "r") as f1, open("fichier2.txt", "r") as f2, open("fusion.txt", "w") as fusion:
    fusion.write(f1.read())
    fusion.write(f2.read())
```

---

### **Exercice 16 : Lire et écrire des chaînes formatées**

```python
with open("noms.txt", "r") as entree, open("salutations.txt", "w") as sortie:
    for ligne in entree:
        nom = ligne.strip()
        sortie.write(f"Bonjour {nom}\n")
```

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
