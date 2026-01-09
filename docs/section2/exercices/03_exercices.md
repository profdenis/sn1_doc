# **Exercices 3 : L'instruction `match`**

---

## **Exercices de compréhension**

### **Exercice 1 : Prédire la sortie**

Pour chaque bloc de code utilisant `match`, prédisez la sortie **sans utiliser Python**. Ensuite, vérifiez vos réponses
en exécutant le code.

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

---

### **Exercice 2 : Compléter le code**

Complétez les blocs `match` suivants pour obtenir la sortie indiquée.

1. **Sortie attendue** :
   ```
   C'est un A.
   ```
   **Code à compléter** :
   ```python
   note = "A"
   match note:

       case _:
           print("Autre note.")
   ```

2. **Sortie attendue** :
   ```
   La liste contient deux éléments : 1 et 2.
   ```
   **Code à compléter** :
   ```python
   liste = [1, 2]
   match liste:
       case []:
           print("La liste est vide.")

       case _:
           print("La liste contient plus de deux éléments.")
   ```

---

## **Exercices de programmation**

### **Exercice 3 : Catégorisation de notes**

Écrivez un programme utilisant `match` pour afficher la mention correspondante à une note donnée (A, B, C, D, ou E).

- A : "Excellent"
- B : "Bien"
- C : "Moyen"
- D : "Passable"
- E : "Insuffisant"

---

### **Exercice 4 : Vérification du type de données**

Écrivez une fonction `verifier_type(valeur)` qui utilise `match` pour afficher le type de la valeur passée en argument (
entier, flottant, chaîne de caractères, liste, ou autre).

---

### **Exercice 5 : Traitement d'une liste**

Écrivez une fonction `traiter_liste(liste)` qui utilise `match` pour afficher un message différent selon le nombre
d'éléments dans la liste :

- Liste vide : "La liste est vide."
- Un élément : "La liste contient un seul élément : [élément]."
- Deux éléments : "La liste contient deux éléments : [élément1] et [élément2]."
- Plus de deux éléments : "La liste contient plusieurs éléments."

---

### **Exercice 6 : Conversion de température**

Écrivez une fonction `convertir_temperature(valeur, unite)` qui utilise `match` pour convertir une température entre
Celsius et Fahrenheit selon l'unité spécifiée ("C" ou "F"). La fonction doit retourner la température convertie.

**Formules** :

- De Celsius à Fahrenheit : \( F = C \times \frac{9}{5} + 32 \)
- De Fahrenheit à Celsius : \( C = (F - 32) \times \frac{5}{9} \)

---

### **Exercice 7 : Traitement d'un dictionnaire**

Écrivez une fonction `traiter_personne(personne)` qui utilise `match` pour afficher des informations sur une personne
représentée par un dictionnaire. Le dictionnaire peut contenir les clés "nom", "âge", et "ville". La fonction doit
afficher les informations disponibles et indiquer si certaines informations manquent.

---

### **Exercice 8 : Calculatrice simple**

Écrivez une fonction `calculer(operation, a, b)` qui utilise `match` pour effectuer une opération arithmétique (`+`,
`-`, `*`, `/`) sur deux nombres `a` et `b`. La fonction doit retourner le résultat de l'opération.

---

### **Exercice 9 : Vérification de conditions météorologiques**

Écrivez un programme utilisant `match` pour afficher un message en fonction de la météo (ensoleillé, pluvieux, nuageux,
neigeux).

---

### **Exercice 10 : Traitement d'une commande**

Écrivez une fonction `traiter_commande(commande)` qui utilise `match` pour traiter une commande représentée par un
dictionnaire. La commande peut contenir les clés "action" (ex. : "ajouter", "supprimer", "afficher") et "element". La
fonction doit afficher un message indiquant l'action effectuée.

---

---
**Conseils pour les exercices** :

- Utilisez `match` pour simplifier les comparaisons multiples.
- Testez vos programmes avec différentes valeurs pour vérifier leur bon fonctionnement.


-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
