# **Exercices 5 : Les dictionnaires**

---

## **Exercices de compréhension**

### **Exercice 1 : Prédire la sortie**

Pour chaque bloc de code, prédisez la sortie **sans utiliser Python**. Ensuite, vérifiez vos réponses en exécutant le
code.

1.

```python
mon_dictionnaire = {"a": 1, "b": 2, "c": 3}
print(mon_dictionnaire["b"])
```

2.

```python
capitales = {"France": "Paris", "Canada": "Ottawa"}
capitales["Japon"] = "Tokyo"
print(capitales)
```

---

## **Exercices de base**

### **Exercice 2 : Créer un dictionnaire**

Créez un dictionnaire `etudiant` contenant les informations suivantes :

- Nom : "Alice"
- Âge : 25
- Cours : ["Maths", "Informatique", "Physique"]

Affichez le dictionnaire.

---

### **Exercice 3 : Accéder aux valeurs**

À partir du dictionnaire `etudiant` créé dans l'exercice 2, affichez :

- Le nom de l'étudiant.
- Le deuxième cours suivi par l'étudiant.

---

### **Exercice 4 : Ajouter et modifier des éléments**

À partir du dictionnaire `etudiant` :

- Ajoutez une clé `"ville"` avec la valeur `"Montréal"`.
- Modifiez la valeur de la clé `"âge"` pour qu'elle soit `26`.

Affichez le dictionnaire modifié.

---

### **Exercice 5 : Supprimer un élément**

À partir du dictionnaire `etudiant` :

- Supprimez la clé `"ville"`.

Affichez le dictionnaire après suppression.

---

### **Exercice 6 : Parcourir un dictionnaire**

Créez un dictionnaire `capitales` contenant les paires suivantes :

- "France" : "Paris"
- "Canada" : "Ottawa"
- "Japon" : "Tokyo"

Parcourez le dictionnaire et affichez chaque paire clé-valeur sous la forme : `Pays : Capitale`.

---

### **Exercice 7 : Vérifier l'existence d'une clé**

À partir du dictionnaire `capitales` de l'exercice 6, vérifiez si la clé `"Allemagne"` existe. Si elle n'existe pas,
ajoutez-la avec la valeur `"Berlin"`.

---

### **Exercice 8 : Utiliser la méthode `get()`**

À partir du dictionnaire `capitales`, utilisez la méthode `get()` pour obtenir la capitale de `"Italie"`. Si la clé
n'existe pas, retournez `"Inconnu"`.

---

## **Exercices intermédiaires**

### **Exercice 9 : Compter les occurrences de mots**

Écrivez un programme qui compte les occurrences de chaque mot dans la phrase suivante :
`"le chat est sur le tapis le chat est noir"`

Affichez le dictionnaire des occurrences.

---

### **Exercice 10 : Fusionner deux dictionnaires**

Créez deux dictionnaires :

- `dictionnaire1 = {"a": 1, "b": 2}`
- `dictionnaire2 = {"b": 3, "c": 4}`

Fusionnez-les en un seul dictionnaire. En cas de conflit de clés, conservez la valeur du deuxième dictionnaire.

---

### **Exercice 11 : Inverser un dictionnaire**

Créez un dictionnaire `capitales` comme dans l'exercice 6, puis créez un nouveau dictionnaire où les capitales
deviennent les clés et les pays deviennent les valeurs.

---

### **Exercice 12 : Trouver la clé avec la valeur maximale**

Créez un dictionnaire `notes` contenant les paires suivantes :

- "Alice" : 15
- "Bob" : 12
- "Charlie" : 18
- "David" : 14

Trouvez le nom de l'étudiant avec la note la plus élevée.

---

## **Exercices avancés**

### **Exercice 13 : Créer un dictionnaire à partir de deux listes**

Vous avez deux listes :

- `cles = ["nom", "âge", "ville"]`
- `valeurs = ["Alice", 25, "Montréal"]`

Créez un dictionnaire `personne` à partir de ces deux listes.

---

### **Exercice 14 : Filtrer un dictionnaire**

À partir du dictionnaire `notes` de l'exercice 12, créez un nouveau dictionnaire contenant uniquement les étudiants avec
une note supérieure ou égale à 15.

---

### **Exercice 15 : Calculer la moyenne des valeurs**

À partir du dictionnaire `notes` de l'exercice 12, calculez la moyenne des notes.

---

### **Exercice 16 : Dictionnaire imbriqué**

Créez un dictionnaire `ecole` contenant les informations suivantes :

- "Classe A" : {"nombre_etudiants" : 25, "professeur" : "M. Dupont"}
- "Classe B" : {"nombre_etudiants" : 22, "professeur" : "Mme Martin"}

Affichez le nombre total d'étudiants dans l'école.

---

### **Exercice 17 : Mettre à jour un dictionnaire imbriqué**

À partir du dictionnaire `ecole` de l'exercice 16, modifiez le professeur de la "Classe B" pour qu'il soit "M. Bernard".

---

### **Exercice 18 : Parcourir un dictionnaire imbriqué**

À partir du dictionnaire `ecole` de l'exercice 16, parcourez-le et affichez chaque classe avec son nombre d'étudiants et
son professeur.

---

### **Exercice 19 : Créer un dictionnaire de listes**

Créez un dictionnaire `cours` où chaque clé est un nom de cours et chaque valeur est une liste d'étudiants inscrits à ce
cours. Par exemple :

```python
cours = {
    "Maths": ["Alice", "Bob", "Charlie"],
    "Informatique": ["Alice", "David"],
    "Physique": ["Bob", "Charlie", "David"]
}
```

Affichez tous les étudiants inscrits au cours de "Maths".

---

### **Exercice 20 : Trouver les étudiants communs à deux cours**

À partir du dictionnaire `cours` de l'exercice 19, trouvez les étudiants inscrits à la fois en "Maths" et en "
Informatique".

---

---
**Conseils pour les exercices** :

- Utilisez les méthodes des dictionnaires comme `keys()`, `values()`, et `items()` pour parcourir les éléments.
- Utilisez `get()` pour éviter les erreurs lors de l'accès à des clés inexistantes.
- Testez vos programmes avec différentes valeurs pour vérifier leur bon fonctionnement.

---
