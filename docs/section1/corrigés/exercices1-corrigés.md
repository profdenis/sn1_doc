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

## **Partie 2 : Utilisation de `.format()` et des f-strings**

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
Les f-strings sont souvent préférées pour leur lisibilité et leur concision, surtout quand on utilise des variables existantes.

---

### **Exercice 5 : Formatage avancé**
```python
prix = 12.3456

# Avec .format()
print("Le prix est {:.2f} $".format(prix))

# Avec f-strings
print(f"Le prix est {prix:.2f} $")

# 2. (f-strings uniquement)
print(f"Le carré de 5 est {5**2}.")
```

---
**Réponse bonus** :
Les f-strings permettent d’insérer directement des expressions (comme `5**2`), ce qui les rend plus pratiques pour les calculs dans la chaîne.

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
Les deux méthodes sont aussi intuitives l’une que l’autre pour cet exercice, mais les f-strings évitent d’appeler une méthode supplémentaire.

---

### **Exercice 7 : Choix personnel**
```python
nom = "Denis Rinfret"
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
Les f-strings sont souvent choisies pour leur simplicité, surtout quand on utilise des variables déjà définies.

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
Les f-strings sont plus adaptées pour formater des listes dynamiques, car elles permettent d’accéder directement aux éléments et d’insérer des expressions.

---

## **Partie 3 : Défis combinés**

### **Exercice 9 : Tableau de multiplication**
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")
```

---
**Réponse bonus** :
Pour aligner les résultats à droite, on peut utiliser :
```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j:2d}")
```

---

### **Exercice 10 : Menu interactif**
```python
print("Menu :", "1. Afficher la date", "2. Calculer une moyenne", "3. Quitter", sep="\n")

choix = 1  # Exemple
print(f"Vous avez choisi l'option {choix}.")
```
