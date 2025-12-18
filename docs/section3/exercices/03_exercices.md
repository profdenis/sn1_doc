# **Exercices 3 : Lecture et écriture de fichiers**

---

## **Exercices de compréhension**

### **Exercice 1 : Prédire la sortie**

Pour chaque bloc de code, prédisez la sortie **sans utiliser Python**. Ensuite, vérifiez vos réponses en exécutant le
code.

1.

```python
with open("test.txt", "w") as fichier:
    fichier.write("Bonjour\n")
    fichier.write("Python\n")

with open("test.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
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

---

## **Exercices de lecture de fichiers**

### **Exercice 2 : Lire un fichier texte**

Écrivez un programme qui lit le contenu d'un fichier nommé `poeme.txt` et l'affiche à l'écran.

---

### **Exercice 3 : Lire un fichier ligne par ligne**

Écrivez un programme qui lit un fichier nommé `villes.txt` ligne par ligne et affiche chaque ligne avec un numéro de
ligne.

---

### **Exercice 4 : Calculer la somme des nombres dans un fichier**

Écrivez un programme qui lit un fichier nommé `nombres.txt` contenant un nombre par ligne, calcule la somme de ces
nombres et affiche le résultat. **Gérez les erreurs** si une ligne ne contient pas un nombre valide.

---

### **Exercice 5 : Lire une liste de nombres**

Écrivez une fonction `lire_nombres(nom_fichier)` qui lit un fichier contenant un nombre par ligne et retourne une liste
de ces nombres. **Gérez les erreurs** pour ignorer les lignes non valides.

---

### **Exercice 6 : Compter les mots dans un fichier**

Écrivez un programme qui lit un fichier nommé `texte.txt` et compte le nombre de mots qu'il contient.

---

### **Exercice 7 : Trouver le mot le plus long**

Écrivez un programme qui lit un fichier nommé `mots.txt` contenant un mot par ligne et trouve le mot le plus long.

---

## **Exercices d'écriture de fichiers**

### **Exercice 8 : Écrire dans un fichier**

Écrivez un programme qui demande à l'utilisateur d'entrer trois lignes de texte et écrit ces lignes dans un fichier
nommé `utilisateur.txt`.

---

### **Exercice 9 : Ajouter à un fichier**

Écrivez un programme qui ajoute trois lignes de texte à la fin d'un fichier existant nommé `journal.txt`.

---

### **Exercice 10 : Écrire une liste de nombres**

Écrivez un programme qui écrit une liste de nombres `[1.5, 2.5, 3.5, 4.5]` dans un fichier nommé `nombres_sortie.txt`,
un nombre par ligne.

---

### **Exercice 11 : Écrire une liste de chaînes**

Écrivez un programme qui écrit une liste de chaînes `["pomme", "banane", "cerise", "datte"]` dans un fichier nommé
`fruits.txt`, une chaîne par ligne.

---

## **Exercices combinés (lecture et écriture)**

### **Exercice 12 : Copier un fichier**

Écrivez un programme qui copie le contenu d'un fichier `source.txt` vers un fichier `destination.txt`.

---

### **Exercice 13 : Inverser les lignes d'un fichier**

Écrivez un programme qui lit un fichier `entree.txt` et écrit ses lignes dans un fichier `sortie.txt` dans l'ordre
inverse.

---

### **Exercice 14 : Filtrer les nombres pairs**

Écrivez un programme qui lit un fichier `nombres.txt` contenant un nombre par ligne, filtre les nombres pairs, et écrit
ces nombres pairs dans un fichier `pairs.txt`.

---

### **Exercice 15 : Compter les occurrences de mots**

Écrivez un programme qui lit un fichier `texte.txt`, compte les occurrences de chaque mot, et écrit les résultats dans
un fichier `occurrences.txt`.

---

### **Exercice 16 : Fusionner deux fichiers**

Écrivez un programme qui lit le contenu de deux fichiers `fichier1.txt` et `fichier2.txt`, et écrit leur contenu
fusionné dans un fichier `fusion.txt`.

---

### **Exercice 17 : Lire et écrire des chaînes formatées**

Écrivez un programme qui lit un fichier `noms.txt` contenant un nom par ligne, et écrit dans un fichier
`salutations.txt` une ligne de salutation pour chaque nom (ex. : "Bonjour Alice").

---

### **Exercice 18 : Calculer la moyenne des nombres dans un fichier**

Écrivez un programme qui lit un fichier `notes.txt` contenant une note par ligne, calcule la moyenne de ces notes, et
écrit le résultat dans un fichier `moyenne.txt`.

---

### **Exercice 19 : Lire et écrire des données structurées**

Écrivez un programme qui lit un fichier `etudiants.txt` contenant des lignes au format `nom,note`, calcule la moyenne
des notes, et écrit le résultat dans un fichier `resultats.txt`.

---

### **Exercice 20 : Gestion des erreurs de fichier**

Écrivez un programme qui tente de lire un fichier `inexistant.txt` et gère les erreurs `FileNotFoundError` et
`PermissionError`.

---

---
**Conseils pour les exercices** :

- Utilisez `with open(...)` pour garantir la fermeture des fichiers.
- Gérez les erreurs potentielles avec `try`/`except`.
- Testez vos programmes avec des fichiers existants et inexistants.

---
