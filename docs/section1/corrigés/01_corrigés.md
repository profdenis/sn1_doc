# **Corrigés 1 : Affichage sur la sortie standard**

---

## **Partie 1 : Utilisation de `print()`**

### **Exercice 1 : Affichage simple**

```python
# 1.
print("Bonjour, monde !")

# 2.
print("La réponse est 42.")

# 3.
print("Python", "est", "génial", sep="-")
```

---

### **Exercice 2 : Paramètres `sep` et `end`**

```python
# 1.
print("Science", "Nature", "Programmation", sep="/")

# 2.
print("Chargement", end="")
print(".", end="")
print(".", end="")
print(".")

# 3.
print(25, end="/")
print(12, end="/")
print(2025)
```

---

### **Exercice 3 : Combinaison de `sep` et `end`**

```python
# 1.
print("Les notes :", 15, 18, 12, sep=", ", end=".\n")

# 2.
print("3", end=">")
print("2", end=">")
print("1", end=">")
print("Décollage !")
```

---

## **Partie 2 : Utilisation de `.format()` et des _f-strings_**

### **Exercice 4 : Formatage de base**

```python
prenom = "Denis"

# Avec .format()
print("Bonjour, {} !".format(prenom))

# Avec f-strings
print(f"Bonjour, {prenom} !")

# 2.
a = 5
b = 3
resultat = a + b

# Avec .format()
print("Le résultat de {} + {} est {}.".format(a, b, resultat))

# Avec f-strings
print(f"Le résultat de {a} + {b} est {resultat}.")
```

---
**Réponse bonus** :
Les _f-strings_ sont souvent préférées pour leur lisibilité et leur concision, surtout quand on utilise des variables
existantes.

---

### **Exercice 5 : Formatage avancé**

```python
prix = 12.3456

# Avec .format()
print("Le prix est {:.2f} $".format(prix))

# Avec f-strings
print(f"Le prix est {prix:.2f} $")

# 2. (f-strings uniquement)
print(f"Le carré de 5 est {5 ** 2}.")
```

---
**Réponse bonus** :
Les _f-strings_ permettent d’insérer directement des expressions (comme `5**2`), ce qui les rend plus pratiques pour les
calculs dans la chaîne.

---

### **Exercice 6 : Alignement et remplissage**

```python
# Avec .format()
print("{:#^20}".format("Python"))

# Avec f-strings
print(f"{'Python':#^20}")
```

---
**Réponse bonus** :
Les deux méthodes sont aussi intuitives l’une que l’autre pour cet exercice, mais les _f-strings_ évitent d’appeler une
méthode supplémentaire.

---

### **Exercice 7 : Choix personnel**

```python
nom = "Jean Tremblay"
note = 18

# Exemple avec f-strings (choix personnel)
print(f"L’étudiant {nom} a obtenu {note}/20.")

# Exemple avec .format()
print("L’étudiant {} a obtenu {}/20.".format(nom, note))

# 2.
temperature = 22.5

# Exemple avec f-strings
print(f"La température moyenne est de {temperature}°C.")
```

---
**Réponse bonus** :
Les _f-strings_ sont souvent choisies pour leur simplicité, surtout quand on utilise des variables déjà définies.

---

### **Exercice 8 : Conversion et formatage**

```python
minutes = 125
heures = minutes // 60
restantes = minutes % 60

# Avec .format()
print("La durée est {}h{:02d}.".format(heures, restantes))

# Avec f-strings
print(f"La durée est {heures}h{restantes:02d}.")

# 2. (exemple avec f-strings)
notes = [12, 15, 18]
print(f"Notes : {notes[0]}, {notes[1]}, {notes[2]}.")
```

---
**Réponse bonus** :
Les _f-strings_ sont plus adaptées pour formater des listes dynamiques, car elles permettent d’accéder directement aux
éléments et d’insérer des expressions.

---

## **Partie 3 : Exercices de base sur les _f-strings_**

Fichier Python contenant tout le code : [formatage.py](formatage.py)

### **Exercice 1 : Affichage simple**

```python
nom = "Alice"
age = 25
print(f"{nom} a {age} ans.")
# Résultat : "Alice a 25 ans."
```

---

### **Exercice 2 : Calculs dans les _f-strings_**

```python
a = 10
b = 3
print(f"{a} divisé par {b} est égal à {a / b}.")
# Résultat : "10 divisé par 3 est égal à 3.3333333333333335."
```

---

### **Exercice 3 : Formatage des flottants**

```python
prix = 12.3456789
taux = 0.123456789
print(f"Prix : {prix:.2f} $")
print(f"Taux : {taux:.2%}")
# Résultat :
# Prix : 12.35 $
# Taux : 12.35 %
```

---

### **Exercice 4 : Formatage des entiers**

```python
jour = 5
mois = 12
annee = 2023
print(f"{jour:03d}/{mois:03d}/{annee}")
# Résultat : "005/012/2023"
```

---

### **Exercice 5 : Alignement du texte**

```python
mot = "Bonjour"
print(f"{mot:<15}")  # Aligné à gauche
print(f"{mot:^15}")  # Centré
print(f"{mot:>15}")  # Aligné à droite
# Résultat :
# Bonjour______
# ___Bonjour___
# ______Bonjour
```

### **Exercice 6 : Formatage scientifique**

```python
grand_nombre = 123456789
print(f"{grand_nombre:.3e}")
# Résultat : "1.235e+08"
```

---

### **Exercice 7 : Formatage binaire, octal et hexadécimal**

```python
nombre = 255
print(f"Binaire : {nombre:b}")
print(f"Octal : {nombre:o}")
print(f"Hexadécimal : {nombre:#x}")
# Résultat :
# Binaire : 11111111
# Octal : 377
# Hexadécimal : 0xff
```

---

### **Exercice 8 : Séparateurs de milliers**

```python
grand_nombre = 1000000
print(f"{grand_nombre:,}")
# Résultat : "1,000,000"
```

---

### **Exercice 9 : Affichage des signes**

```python
positif = 123
negatif = -456
print(f"Positif : {positif:+d}")
print(f"Négatif : {negatif: d}")
# Résultat :
# Positif : +123
# Négatif : -456
```

!!! note "Note"
    Le signe `+` est obligatoire pour les nombres positifs. Pour les nombres négatifs, il est optionnel : on pourrait 
    écrire `negatif:d` ou `negatif:+d`, ou même `negatif: d`. Il n'y aura pas de différence de sortie pour un nombre 
    négatif. Mais pour un nombre positif, il y aura une différence : le signe `+` sera affiché seulement avec 
    `positif:+d`. Pas de signe avec `positif:d` ni avec `positif: d`. Il y aura un espace inséré à la place du signe avec
    `positif: d`, mais pas avec `positif:d`. 

---

### **Exercice 10 : Formatage des pourcentages**

```python
taux = 0.7563
print(f"{taux:.2%}")
# Résultat : "75.63%"
```

---

### **Exercice 11 : Formatage des durées**

```python
secondes = 3661
heures = secondes // 3600
minutes = (secondes % 3600) // 60
secondes_restantes = secondes % 60
print(f"{heures:02d}:{minutes:02d}:{secondes_restantes:02d}")
# Résultat : "01:01:01"
```

---

### **Exercice 12 : Formatage monétaire**

```python
prix = 1234.56789
print(f"{prix:,.2f} $")
# Résultat : "1,234.57 $"
```

---

### **Exercice 13 : Combinaison de spécificateurs**

```python
nombre = 12345.6789
print(f"{nombre:+15,.2f}")
# Résultat : "   +12,345.68"
```


---

### **Exercice 14 : Formatage personnalisé**

```python
client = "Jean Dupont"
montant_ht = 123.456
taux_tva = 0.15
montant_ttc = montant_ht * (1 + taux_tva)

print(f"Facture pour {client}")
print(f"Montant HT : {montant_ht:.2f} $")
print(f"Taxes ({taux_tva:.2%}) : {montant_ht * taux_tva:.2f} $")
print(f"Montant TTC : {montant_ttc:.2f} $")
# Résultat :
# Facture pour Jean Dupont
# Montant HT : 123.46 $
# Taxes (15.00 %) : 18.52 $
# Montant TTC : 141.98 $
```

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.