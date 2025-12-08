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
while True:
    try:
        age = int(input("Entrez votre âge : "))
        break
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

### **Exercice 6 : Validation d'un code postal**

Écrivez une fonction `demander_code_postal()` qui demande à l'utilisateur d'entrer un code postal de 5 chiffres.
Utilisez une boucle et une gestion d'exception pour valider l'entrée.

---

### **Exercice 7 : Validation d'une adresse e-mail**

Écrivez une fonction `demander_email()` qui demande à l'utilisateur d'entrer une adresse e-mail valide (contenant un `@`
et un `.`). Utilisez une boucle et une gestion d'exception pour valider l'entrée.

---

### **Exercice 8 : Division sécurisée**

Écrivez une fonction `division_securisee()` qui demande à l'utilisateur d'entrer deux nombres et effectue la division du
premier par le second. Gérez les exceptions possibles (`ValueError` et `ZeroDivisionError`).

---

### **Exercice 9 : Lecture sécurisée d'un fichier**

Écrivez une fonction `lire_fichier()` qui demande à l'utilisateur d'entrer le nom d'un fichier et tente de lire son
contenu. Gérez l'exception `FileNotFoundError`.

---

### **Exercice 10 : Validation d'une liste d'entiers**

Écrivez une fonction `demander_liste_entiers()` qui demande à l'utilisateur d'entrer une liste d'entiers séparés par des
espaces. Validez chaque entier et retournez la liste.

---

### **Exercice 11 : Validation d'une date**

Écrivez une fonction `demander_date()` qui demande à l'utilisateur d'entrer une date sous la forme `JJ/MM/AAAA`. Validez
que la date est correcte (ex. : le jour est entre 1 et 31, le mois entre 1 et 12, etc.).

---

### **Exercice 12 : Validation d'un mot de passe**

Écrivez une fonction `demander_mot_de_passe()` qui demande à l'utilisateur d'entrer un mot de passe contenant au moins 8
caractères, une majuscule et un chiffre. Utilisez une boucle et des conditionnelles pour valider l'entrée.

---

### **Exercice 13 : Validation d'une heure**

Écrivez une fonction `demander_heure()` qui demande à l'utilisateur d'entrer une heure sous la forme `HH:MM`. Validez
que l'heure est correcte (ex. : les heures entre 0 et 23, les minutes entre 0 et 59).

---

### **Exercice 14 : Validation d'une liste de notes**

Écrivez une fonction `demander_liste_notes()` qui demande à l'utilisateur d'entrer une liste de notes (entre 0 et 100)
séparées par des virgules. Validez chaque note et retournez la liste.

---

### **Exercice 15 : Validation d'un numéro de téléphone**

Écrivez une fonction `demander_numero_telephone()` qui demande à l'utilisateur d'entrer un numéro de téléphone de 10
chiffres. Utilisez une boucle et des conditionnelles pour valider l'entrée.

---

---
**Conseils pour les exercices** :

- Utilisez des boucles (`while`) pour demander à l'utilisateur de réessayer en cas d'erreur.
- Utilisez des conditionnelles (`if`) pour valider les entrées.
- Utilisez des exceptions (`try`/`except`) pour gérer les erreurs de conversion ou d'accès.

---
