---
icon: material/checkbox-blank-outline
---

# **5. Les dictionnaires**

---

## **1. Introduction aux dictionnaires**

Un **dictionnaire** est une collection **non ordonnée**, **modifiable** et **indexée** par des **clés**. Chaque élément
d'un dictionnaire est une paire **clé-valeur**.

### **1.1 Pourquoi utiliser un dictionnaire ?**

- **Accès rapide** : Les dictionnaires permettent un accès rapide aux valeurs via des clés.
- **Flexibilité** : Les clés et les valeurs peuvent être de n'importe quel type (mais les clés doivent être
  **immuables**).
- **Efficacité** : Les opérations de recherche, d'insertion et de suppression sont très rapides.

---

## **2. Création et accès aux éléments**

### **2.1 Créer un dictionnaire**

```python
# Dictionnaire vide
mon_dictionnaire = {}

# Dictionnaire avec des éléments
etudiant = {
    "nom": "Alice",
    "âge": 25,
    "cours": ["Maths", "Informatique", "Physique"]
}

# Autre exemple
capitales = {
    "France": "Paris",
    "Canada": "Ottawa",
    "Japon": "Tokyo"
}
```

---

### **2.2 Accéder à une valeur**

```python
print(etudiant["nom"])  # Affiche "Alice"
print(capitales["Canada"])  # Affiche "Ottawa"
```

---

### **2.3 Ajouter ou modifier une valeur**

```python
# Ajouter une nouvelle paire clé-valeur
etudiant["ville"] = "Montréal"

# Modifier une valeur existante
etudiant["âge"] = 26

print(etudiant)
# Affiche : {'nom': 'Alice', 'âge': 26, 'cours': ['Maths', 'Informatique', 'Physique'], 'ville': 'Montréal'}
```

---

### **2.4 Supprimer une paire clé-valeur**

```python
del etudiant["ville"]  # Supprime la clé "ville" et sa valeur
print(etudiant)
# Affiche : {'nom': 'Alice', 'âge': 26, 'cours': ['Maths', 'Informatique', 'Physique']}
```

---

## **3. Parcourir un dictionnaire**

### **3.1 Parcourir les clés**

```python
for cle in capitales:
    print(cle)
# Affiche :
# France
# Canada
# Japon
```

---

### **3.2 Parcourir les valeurs**

```python
for valeur in capitales.values():
    print(valeur)
# Affiche :
# Paris
# Ottawa
# Tokyo
```

---

### **3.3 Parcourir les paires clé-valeur**

```python
for cle, valeur in capitales.items():
    print(f"{cle} : {valeur}")
# Affiche :
# France : Paris
# Canada : Ottawa
# Japon : Tokyo
```

---

## **4. Vérifier l'existence d'une clé**

### **4.1 Avec l'opérateur `in`**

```python
if "France" in capitales:
    print("La France est dans le dictionnaire.")
# Affiche : La France est dans le dictionnaire.
```

---

### **4.2 Méthode `get()` pour éviter les erreurs**

```python
pays = "Allemagne"
capitale = capitales.get(pays, "Inconnu")
print(f"La capitale de {pays} est {capitale}.")
# Affiche : La capitale de Allemagne est Inconnu.
```


!!! note "Remarque"
    Si on tente d'accéder à une clé qui n'existe pas dans un dictionnaire, Python lève une exception `KeyError`. On peut
    utiliser `try/except` pour gérer cette erreur potentielle, mais ce n'est pas la méthode à privilégier. Il est
    préférable d'utiliser la méthode `get()` comme dans cet exemple, ou sinon, on peut utiliser `in` comme dans 
    l'exemple précédent.


---

## **5. Exemples pratiques**

### **5.1 Compter les occurrences de mots**

```python
texte = "bonjour tout le monde bonjour"
mots = texte.split() # sépare le texte en une liste de mots
occurrences = {}

for mot in mots:
    if mot in occurrences:
        occurrences[mot] += 1
    else:
        occurrences[mot] = 1

print(occurrences)
# Affiche : {'bonjour': 2, 'tout': 1, 'le': 1, 'monde': 1}
```

---

### **5.2 Stocker des informations sur des étudiants**

```python
etudiants = {
    "Alice": {"âge": 25, "cours": ["Maths", "Informatique"]},
    "Bob": {"âge": 22, "cours": ["Physique", "Chimie"]},
    "Charlie": {"âge": 24, "cours": ["Biologie", "Maths"]}
}

for nom, infos in etudiants.items():
    print(f"{nom} a {infos['âge']} ans et suit les cours : {', '.join(infos['cours'])}")
# Affiche :
# Alice a 25 ans et suit les cours : Maths, Informatique
# Bob a 22 ans et suit les cours : Physique, Chimie
# Charlie a 24 ans et suit les cours : Biologie, Maths
```

---

### **5.3 Fusionner deux dictionnaires**

```python
dictionnaire1 = {"a": 1, "b": 2}
dictionnaire2 = {"b": 3, "c": 4}

# Méthode 1 : Utiliser update()
dictionnaire_fusionne = dictionnaire1.copy()
dictionnaire_fusionne.update(dictionnaire2)
print(dictionnaire_fusionne)
# Affiche : {'a': 1, 'b': 3, 'c': 4}

# Méthode 2 : Utiliser {**d1, **d2} (Python 3.5+)
dictionnaire_fusionne = {**dictionnaire1, **dictionnaire2}
print(dictionnaire_fusionne)
# Affiche : {'a': 1, 'b': 3, 'c': 4}
```

---

## **6. Méthodes utiles des dictionnaires**

| **Méthode**               | **Description**                                                                       |
|---------------------------|---------------------------------------------------------------------------------------|
| `clear()`                 | Supprime tous les éléments du dictionnaire.                                           |
| `copy()`                  | Retourne une copie du dictionnaire.                                                   |
| `get(clé, valeur)`        | Retourne la valeur associée à la clé. Si la clé n'existe pas, retourne `valeur`.      |
| `items()`                 | Retourne une vue des paires clé-valeur.                                               |
| `keys()`                  | Retourne une vue des clés du dictionnaire.                                            |
| `pop(clé)`                | Supprime la paire clé-valeur et retourne la valeur.                                   |
| `popitem()`               | Supprime et retourne une paire clé-valeur aléatoire.                                  |
| `setdefault(clé, valeur)` | Retourne la valeur associée à la clé. Si la clé n'existe pas, l'ajoute avec `valeur`. |
| `update(dictionnaire)`    | Met à jour le dictionnaire avec les paires clé-valeur d'un autre dictionnaire.        |
| `values()`                | Retourne une vue des valeurs du dictionnaire.                                         |

---
