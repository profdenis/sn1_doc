
# **Corrigés 3 : L'instruction `match`**

---

### **Exercice 1 : Prédire la sortie**
1.
```python
jour = "mardi"
match jour:
    case "lundi":
        print("Début de la semaine.")
    case "vendredi":
        print("Fin de la semaine.")
    case _:
        print("Milieu de la semaine.")
```
**Sortie** :
```
Milieu de la semaine.
```

2.
```python
nombre = 7
match nombre:
    case 1:
        print("Un.")
    case 2:
        print("Deux.")
    case _:
        print("Autre nombre.")
```
**Sortie** :
```
Autre nombre.
```

3.
```python
valeur = 3.14
match valeur:
    case int():
        print("Entier.")
    case float():
        print("Flottant.")
    case _:
        print("Autre type.")
```
**Sortie** :
```
Flottant.
```

---

### **Exercice 2 : Compléter le code**
1.
```python
note = "A"
match note:
    case "A":
        print("C'est un A.")
    case "B":
        print("C'est un B.")
    case _:
        print("Autre note.")
```
**Sortie** :
```
C'est un A.
```

2.
```python
liste = [1, 2]
match liste:
    case []:
        print("La liste est vide.")
    case [x]:
        print(f"La liste contient un seul élément : {x}.")
    case [x, y]:
        print(f"La liste contient deux éléments : {x} et {y}.")
    case _:
        print("La liste contient plus de deux éléments.")
```
**Sortie** :
```
La liste contient deux éléments : 1 et 2.
```

---

### **Exercice 3 : Catégorisation de notes**
```python
note = "B"
match note:
    case "A":
        print("Excellent")
    case "B":
        print("Bien")
    case "C":
        print("Moyen")
    case "D":
        print("Passable")
    case "E":
        print("Insuffisant")
    case _:
        print("Note non reconnue.")
```
**Sortie** :
```
Bien
```

---

### **Exercice 4 : Vérification du type de données**
```python
def verifier_type(valeur):
    match valeur:
        case int():
            print("Entier.")
        case float():
            print("Flottant.")
        case str():
            print("Chaîne de caractères.")
        case list():
            print("Liste.")
        case _:
            print("Autre type.")

verifier_type(42)
verifier_type(3.14)
verifier_type("Bonjour")
verifier_type([1, 2, 3])
```
**Sortie** :
```
Entier.
Flottant.
Chaîne de caractères.
Liste.
```

---

### **Exercice 5 : Traitement d'une liste**
```python
def traiter_liste(liste):
    match liste:
        case []:
            print("La liste est vide.")
        case [x]:
            print(f"La liste contient un seul élément : {x}.")
        case [x, y]:
            print(f"La liste contient deux éléments : {x} et {y}.")
        case _:
            print("La liste contient plusieurs éléments.")

traiter_liste([])
traiter_liste([1])
traiter_liste([1, 2])
traiter_liste([1, 2, 3])
```
**Sortie** :
```
La liste est vide.
La liste contient un seul élément : 1.
La liste contient deux éléments : 1 et 2.
La liste contient plusieurs éléments.
```

---

### **Exercice 6 : Conversion de température**
```python
def convertir_temperature(valeur, unite):
    match unite:
        case "C":
            return valeur * 9/5 + 32
        case "F":
            return (valeur - 32) * 5/9
        case _:
            return None

print(convertir_temperature(25, "C"))  # Conversion de Celsius en Fahrenheit
print(convertir_temperature(77, "F"))  # Conversion de Fahrenheit en Celsius
```
**Sortie** :
```
77.0
25.0
```

---

### **Exercice 7 : Traitement d'un dictionnaire**
```python
def traiter_personne(personne):
    match personne:
        case {"nom": nom, "âge": age, "ville": ville}:
            print(f"Nom : {nom}, Âge : {age}, Ville : {ville}.")
        case {"nom": nom, "âge": age}:
            print(f"Nom : {nom}, Âge : {age}. Ville non spécifiée.")
        case {"nom": nom}:
            print(f"Nom : {nom}. Âge et ville non spécifiés.")
        case _:
            print("Format de personne non reconnu.")

traiter_personne({"nom": "Alice", "âge": 30, "ville": "Paris"})
traiter_personne({"nom": "Bob", "âge": 25})
traiter_personne({"nom": "Charlie"})
```
**Sortie** :
```
Nom : Alice, Âge : 30, Ville : Paris.
Nom : Bob, Âge : 25. Ville non spécifiée.
Nom : Charlie. Âge et ville non spécifiés.
```

---

### **Exercice 8 : Calculatrice simple**
```python
def calculer(operation, a, b):
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b != 0:
                return a / b
            else:
                return "Erreur : division par zéro."
        case _:
            return "Opération non reconnue."

print(calculer("+", 5, 3))
print(calculer("-", 5, 3))
print(calculer("*", 5, 3))
print(calculer("/", 5, 3))
print(calculer("/", 5, 0))
```
**Sortie** :
```
8
2
15
1.6666666666666667
Erreur : division par zéro.
```

---

### **Exercice 9 : Vérification de conditions météorologiques**
```python
meteo = "pluvieux"
match meteo:
    case "ensoleillé":
        print("Il fait beau !")
    case "pluvieux":
        print("Prenez un parapluie.")
    case "nuageux":
        print("Ciel couvert.")
    case "neigeux":
        print("Il neige !")
    case _:
        print("Condition météo non reconnue.")
```
**Sortie** :
```
Prenez un parapluie.
```

---

### **Exercice 10 : Traitement d'une commande**
```python
def traiter_commande(commande):
    match commande:
        case {"action": "ajouter", "element": element}:
            print(f"Ajout de l'élément : {element}.")
        case {"action": "supprimer", "element": element}:
            print(f"Suppression de l'élément : {element}.")
        case {"action": "afficher"}:
            print("Affichage des éléments.")
        case _:
            print("Commande non reconnue.")

traiter_commande({"action": "ajouter", "element": "pomme"})
traiter_commande({"action": "supprimer", "element": "banane"})
traiter_commande({"action": "afficher"})
```
**Sortie** :
```
Ajout de l'élément : pomme.
Suppression de l'élément : banane.
Affichage des éléments.
```

---
