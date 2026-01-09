# **Exercices 1 : Gestion des exceptions et validation d'entrées**

---

## **Exercices de compréhension**

### **Exercice 1 : Prédire la sortie**

Pour chaque bloc de code, prédisez la sortie **sans utiliser Python**. Ensuite, vérifiez vos réponses en exécutant le
code.

1.

```python
try:
    nombre = int("vingt")
except ValueError:
    print("Erreur : Ce n'est pas un nombre.")
```

2.

```python
valeur_valide = False
while not valeur_valide:
    try:
        age = int(input("Entrez votre âge : "))
        valeur_valide = True  # La boucle s'arrête si la conversion réussit
    except ValueError:
        print("Erreur : Vous devez entrer un nombre entier.")
print(f"Votre âge est {age}.")
```

*(Entrez "25" comme âge.)*

---

## **Exercices de programmation**

### **Exercice 2 : Validation d'un entier positif**

Écrivez une fonction `demander_entier_positif()` qui demande à l'utilisateur d'entrer un entier positif. Utilisez une
boucle et une gestion d'exception pour valider l'entrée.

---

### **Exercice 3 : Validation d'une note**

Écrivez une fonction `demander_note()` qui demande à l'utilisateur d'entrer une note entre 0 et 100 (inclusivement).
Utilisez une boucle et une gestion d'exception pour valider l'entrée.

---

### **Exercice 4 : Validation d'un choix de menu**

Écrivez une fonction `demander_choix()` qui demande à l'utilisateur de choisir une option entre 1 et 4. Utilisez une
boucle et une gestion d'exception pour valider l'entrée.

---

### **Exercice 5 : Validation d'une année**

Écrivez une fonction `demander_annee()` qui demande à l'utilisateur d'entrer une année entre 1900 et l'année actuelle.
Utilisez une boucle et une gestion d'exception pour valider l'entrée.

---


### **Exercice 6 : Division sécurisée**

Écrivez une fonction `division_securisee()` qui demande à l'utilisateur d'entrer deux nombres et effectue la division du
premier par le second. Gérez les exceptions possibles (`ValueError` et `ZeroDivisionError`).

---



---
**Conseils pour les exercices** :

- Utilisez des boucles (`while`) pour demander à l'utilisateur de réessayer en cas d'erreur.
- Utilisez des conditionnelles (`if`) pour valider les entrées.
- Utilisez des exceptions (`try`/`except`) pour gérer les erreurs de conversion ou d'accès.

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
