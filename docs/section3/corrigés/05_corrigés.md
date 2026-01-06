# **Corrigés 5 : Les dictionnaires**

---

## **Exercices de compréhension**

### **Exercice 1 : Prédire la sortie**

1.

```python
mon_dictionnaire = {"a": 1, "b": 2, "c": 3}
print(mon_dictionnaire["b"])
```

**Sortie** :

```
2
```

2.

```python
capitales = {"France": "Paris", "Canada": "Ottawa"}
capitales["Japon"] = "Tokyo"
print(capitales)
```

**Sortie** :

```
{'France': 'Paris', 'Canada': 'Ottawa', 'Japon': 'Tokyo'}
```

---

## **Exercices de base**

### **Exercice 2 : Créer un dictionnaire**

```python
etudiant = {
    "nom": "Alice",
    "âge": 25,
    "cours": ["Maths", "Informatique", "Physique"]
}
print(etudiant)
```

---

### **Exercice 3 : Accéder aux valeurs**

```python
print(etudiant["nom"])  # Affiche "Alice"
print(etudiant["cours"][1])  # Affiche "Informatique"
```

---

### **Exercice 4 : Ajouter et modifier des éléments**

```python
etudiant["ville"] = "Montréal"  # Ajoute la clé "ville"
etudiant["âge"] = 26  # Modifie la valeur de la clé "âge"
print(etudiant)
```

---

### **Exercice 5 : Supprimer un élément**

```python
del etudiant["ville"]  # Supprime la clé "ville"
print(etudiant)
```

---

### **Exercice 6 : Parcourir un dictionnaire**

```python
capitales = {"France": "Paris", "Canada": "Ottawa", "Japon": "Tokyo"}
for pays in capitales:
    capitale = capitales[pays]
    print(f"{pays} : {capitale}")
```

---

### **Exercice 7 : Vérifier l'existence d'une clé**

```python
if "Allemagne" not in capitales:
    capitales["Allemagne"] = "Berlin"
print(capitales)
```

---

### **Exercice 8 : Utiliser la méthode `get()`**

```python
capitale = capitales.get("Italie", "Inconnu")
print(f"La capitale de l'Italie est {capitale}.")
```

---

## **Exercices intermédiaires**

### **Exercice 9 : Compter les occurrences de mots**

```python
phrase = "le chat est sur le tapis le chat est noir"
mots = phrase.split()
occurrences = {}

for mot in mots:
    if mot in occurrences:
        occurrences[mot] += 1
    else:
        occurrences[mot] = 1

print(occurrences)
```

---

### **Exercice 10 : Fusionner deux dictionnaires**

```python
dictionnaire1 = {"a": 1, "b": 2}
dictionnaire2 = {"b": 3, "c": 4}

dictionnaire_fusionne = dictionnaire1.copy()
for cle, valeur in dictionnaire2.items():
    dictionnaire_fusionne[cle] = valeur

print(dictionnaire_fusionne)
```

---

### **Exercice 11 : Inverser un dictionnaire**

```python
capitales = {"France": "Paris", "Canada": "Ottawa", "Japon": "Tokyo"}
capitales_inversees = {}

for pays, capitale in capitales.items():
    capitales_inversees[capitale] = pays

print(capitales_inversees)
```

---

### **Exercice 12 : Trouver la clé avec la valeur maximale**

```python
notes = {"Alice": 15, "Bob": 12, "Charlie": 18, "David": 14}

nom_max = None
note_max = -1

for nom, note in notes.items():
    if note > note_max:
        note_max = note
        nom_max = nom

print(f"L'étudiant avec la note la plus élevée est {nom_max}.")
```

---

## **Exercices avancés**

### **Exercice 13 : Créer un dictionnaire à partir de deux listes**

```python
cles = ["nom", "âge", "ville"]
valeurs = ["Alice", 25, "Montréal"]

personne = {}
for i in range(len(cles)):
    personne[cles[i]] = valeurs[i]

print(personne)
```

---

### **Exercice 14 : Filtrer un dictionnaire**

```python
notes = {"Alice": 15, "Bob": 12, "Charlie": 18, "David": 14}
notes_filtrees = {}

for nom, note in notes.items():
    if note >= 15:
        notes_filtrees[nom] = note

print(notes_filtrees)
```

---

### **Exercice 15 : Calculer la moyenne des valeurs**

```python
somme = 0
for note in notes.values():
    somme += note

moyenne = somme / len(notes)
print(f"La moyenne des notes est {moyenne:.2f}.")
```

---

### **Exercice 16 : Dictionnaire imbriqué**

```python
ecole = {
    "Classe A": {"nombre_etudiants": 25, "professeur": "M. Dupont"},
    "Classe B": {"nombre_etudiants": 22, "professeur": "Mme Martin"}
}

total_etudiants = 0
for classe in ecole.values():
    total_etudiants += classe["nombre_etudiants"]

print(f"Nombre total d'étudiants : {total_etudiants}.")
```

---

### **Exercice 17 : Mettre à jour un dictionnaire imbriqué**

```python
ecole["Classe B"]["professeur"] = "M. Bernard"
print(ecole)
```

---

### **Exercice 18 : Parcourir un dictionnaire imbriqué**

```python
for classe, infos in ecole.items():
    print(f"{classe} : {infos['nombre_etudiants']} étudiants, professeur : {infos['professeur']}")
```

---

### **Exercice 19 : Créer un dictionnaire de listes**

```python
cours = {
    "Maths": ["Alice", "Bob", "Charlie"],
    "Informatique": ["Alice", "David"],
    "Physique": ["Bob", "Charlie", "David"]
}

print("Étudiants en Maths :", cours["Maths"])
```

---

### **Exercice 20 : Trouver les étudiants communs à deux cours**

```python
maths = cours["Maths"]
informatique = cours["Informatique"]

communs = []
for etudiant in maths:
    if etudiant in informatique:
        communs.append(etudiant)

print("Étudiants communs :", communs)
```

---
