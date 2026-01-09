# **Corrigés 2 : Listes**

---

## **Exercices sur le slicing et les index**

### **Exercice 1 : Accéder aux éléments d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
print(nombres[0])  # Affiche 10
print(nombres[2])  # Affiche 30
print(nombres[-1])  # Affiche 50
```

---

### **Exercice 2 : Extraire une sous-liste**

```python
nombres = [5, 10, 15, 20, 25, 30, 35]
print(nombres[:3])  # Affiche [5, 10, 15]
print(nombres[-3:])  # Affiche [25, 30, 35]
print(nombres[2:5])  # Affiche [15, 20, 25]
```

---

### **Exercice 3 : Inverser une liste avec le slicing**

```python
nombres = [1, 2, 3, 4, 5]
nombres_inverses = nombres[::-1]
print(nombres_inverses)  # Affiche [5, 4, 3, 2, 1]
```

---

### **Exercice 4 : Extraire les éléments pairs avec le slicing**

```python
nombres = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pairs = nombres[::2]
print(pairs)  # Affiche [0, 2, 4, 6, 8]
```

---

### **Exercice 5 : Gérer les index invalides**

```python
nombres = [10, 20, 30]
try:
    print(nombres[10])
except IndexError:
    print("Erreur : Index invalide.")
```

**Sortie** :

```
Erreur : Index invalide.
```

---

### **Exercice 6 : Utiliser les index négatifs**

```python
lettres = ["a", "b", "c", "d", "e"]
print(lettres[-1])  # Affiche "e"
print(lettres[-3:])  # Affiche ["c", "d", "e"]
```

---

## **Exercices sur les listes en général**

### **Exercice 7 : Calculer la somme des éléments d'une liste**

```python
nombres = [12, 23, 34, 45, 56]
somme = 0
for nombre in nombres:
    somme += nombre
print(f"La somme est {somme}.")  # Affiche "La somme est 170."
```

---

### **Exercice 8 : Trouver le maximum et le minimum d'une liste**

```python
nombres = [45, 12, 67, 23, 89, 34]
maximum = max(nombres)
minimum = min(nombres)
print(f"Le maximum est {maximum} et le minimum est {minimum}.")
# Affiche "Le maximum est 89 et le minimum est 12."
```

---

### **Exercice 9 : Compter les occurrences d'un élément**

```python
nombres = [1, 2, 3, 2, 4, 2, 5]
element = 2
compteur = 0
for nombre in nombres:
    if nombre == element:
        compteur += 1
print(f"Le nombre {element} apparaît {compteur} fois.")  # Affiche "Le nombre 2 apparaît 3 fois."
```

---

### **Exercice 10 : Supprimer les doublons d'une liste**

```python
nombres = [1, 2, 2, 3, 4, 4, 5]
sans_doublons = []
for nombre in nombres:
    if nombre not in sans_doublons:
        sans_doublons.append(nombre)
print(sans_doublons)  # Affiche [1, 2, 3, 4, 5]
```

---

### **Exercice 11 : Fusionner deux listes**

```python
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
liste_fusionnee = liste1 + liste2
print(liste_fusionnee)  # Affiche [1, 2, 3, 4, 5, 6]
```

---

### **Exercice 12 : Trier une liste de chaînes de caractères**

```python
fruits = ["pomme", "banane", "cerise", "datte"]
fruits.sort()
print(fruits)  # Affiche ["banane", "cerise", "datte", "pomme"]
```

---

### **Exercice 13 : Rechercher un élément dans une liste**

```python
nombres = [10, 20, 25, 30, 40]
recherche = 25
if recherche in nombres:
    print(f"L'élément {recherche} est présent.")
else:
    print(f"L'élément {recherche} n'est pas présent.")
```

**Sortie** :

```
L'élément 25 est présent.
```

---

### **Exercice 14 : Filtrer les éléments d'une liste**

```python
nombres = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pairs = []
for nombre in nombres:
    if nombre % 2 == 0:
        pairs.append(nombre)
print(pairs)  # Affiche [2, 4, 6, 8, 10]
```

---

### **Exercice 15 : Calculer la moyenne d'une liste de nombres**

```python
nombres = [15, 25, 35, 45, 55]
somme = sum(nombres)
moyenne = somme / len(nombres)
print(f"La moyenne est {moyenne}.")  # Affiche "La moyenne est 35.0."
```

---

### **Exercice 16 : Inverser l'ordre des éléments d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
nombres.reverse()
print(nombres)  # Affiche [50, 40, 30, 20, 10]
```

---

### **Exercice 17 : Ajouter un élément à une liste**

```python
nombres = [10, 20, 30, 40, 50]
nombres.append(60)
print(nombres)  # Affiche [10, 20, 30, 40, 50, 60]
```

---

### **Exercice 18 : Supprimer un élément d'une liste**

```python
nombres = [10, 20, 30, 40, 50]
nombres.remove(30)
print(nombres)  # Affiche [10, 20, 40, 50]
```

---

### **Exercice 19 : Afficher les éléments d'une liste avec leur index**

```python
fruits = ["pomme", "banane", "cerise", "datte"]
for index, fruit in enumerate(fruits):
    print(f"{index} : {fruit}")
```

**Sortie** :

```
0 : pomme
1 : banane
2 : cerise
3 : datte
```

---

### **Exercice 20 : Créer une liste à partir d'une chaîne de caractères**

```python
chaine = "Python"
liste_caracteres = list(chaine)
print(liste_caracteres)  # Affiche ['P', 'y', 't', 'h', 'o', 'n']
```

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
