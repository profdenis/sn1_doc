Voici une **liste combinée et adaptée d'exercices** sur les chaînes de caractères, intégrant ceux de la section de
présentation et ceux du document d'exercices, **sans utiliser NumPy** et en remplaçant les tableaux NumPy par des
listes.

---

# **Exercices pratiques : Chaînes de caractères**

---

## **Exercices de base**

### **Exercice 1 : Inverser une chaîne**

Écrivez une fonction qui inverse une chaîne de caractères.
**Exemple** : `"Python"` → `"nohtyP"`

---

### **Exercice 2 : Compter les mots**

Écrivez une fonction qui compte le nombre de mots dans une chaîne.
**Exemple** : `"Bonjour tout le monde"` → `4`

---

### **Exercice 3 : Palindrome**

Écrivez une fonction qui vérifie si une chaîne est un palindrome (se lit pareil à l'endroit et à l'envers).
**Exemple** : `"radar"` → `True`

---

### **Exercice 4 : Majuscules alternées**

Écrivez une fonction qui retourne une chaîne avec des majuscules alternées.
**Exemple** : `"python"` → `"pYtHoN"`

---

### **Exercice 5 : Censure de mots**

Écrivez une fonction qui remplace un mot interdit par des astérisques.
**Exemple** : `censurer("Ce mot est interdit.", "interdit")` → `"Ce mot est ********"`

---

### **Exercice 6 : Initiales**

Écrivez une fonction qui retourne les initiales d'une chaîne composée de mots.
**Exemple** : `"Denis Rinfret"` → `"D. R."`

---

### **Exercice 7 : Valider un code postal**

Écrivez une fonction qui valide un code postal canadien (format : `A1A 1A1`).
**Exemple** : `est_code_postal_valide("H3T 1J4")` → `True`

---

### **Exercice 8 : Extraire les nombres d'une chaîne**

Écrivez une fonction qui extrait tous les nombres d'une chaîne et les retourne dans une liste.
**Exemple** : `"Il a 3 pommes et 5 bananes."` → `[3, 5]`

---

## **Exercices combinant chaînes et listes**

### **Exercice 9 : Convertir une chaîne en liste de mots**

Écrivez une fonction qui prend une chaîne de caractères et retourne une liste de mots.
**Exemple** : `"Bonjour tout le monde"` → `["Bonjour", "tout", "le", "monde"]`

---

### **Exercice 10 : Trouver les mots les plus longs**

Écrivez une fonction qui prend une liste de mots et retourne une liste des mots les plus longs (il peut y en avoir
plusieurs de même longueur).
**Exemple** : `["pomme", "banane", "cerise", "ananas"]` → `["banane", "ananas"]`

---

### **Exercice 11 : Compter les voyelles dans une liste de mots**

Écrivez une fonction qui prend une liste de mots et retourne le nombre total de voyelles.
**Exemple** : `["pomme", "banane", "kiwi"]` → `7`

---

### **Exercice 12 : Inverser l'ordre des mots**

Écrivez une fonction qui prend une chaîne de caractères et retourne une nouvelle chaîne avec les mots dans l'ordre
inverse.
**Exemple** : `"Bonjour tout le monde"` → `"monde le tout Bonjour"`

---

### **Exercice 13 : Filtrer les mots commençant par une lettre**

Écrivez une fonction qui prend une liste de mots et une lettre, et retourne une nouvelle liste contenant uniquement les
mots commençant par cette lettre.
**Exemple** : `["pomme", "banane", "poire", "cerise"], "p"` → `["pomme", "poire"]`

---

## **Exercices combinant chaînes et boucles/conditionnelles**

### **Exercice 14 : Valider un mot de passe**

Écrivez une fonction qui vérifie si un mot de passe respecte les règles suivantes :

- Au moins 8 caractères.
- Contient au moins une majuscule.
- Contient au moins un chiffre.
  **Exemple** : `est_mot_de_passe_valide("MotDePasse123")` → `True`

---

### **Exercice 15 : Remplacer les voyelles par un caractère**

Écrivez une fonction qui remplace toutes les voyelles d'une chaîne par un caractère donné.
**Exemple** : `remplacer_voyelles("Bonjour", "*")` → `"B*nj**r"`

---

### **Exercice 16 : Compter les occurrences de chaque lettre**

Écrivez une fonction qui prend une chaîne et retourne une liste de tuples, chaque tuple contenant une lettre et son
nombre d'occurrences (sans distinction de casse et en ignorant les espaces).
**Exemple** : `"Bonjour"` → `[('b', 1), ('o', 2), ('n', 1), ('j', 1), ('u', 1), ('r', 1)]`

---

### **Exercice 17 : Trouver les anagrammes**

Écrivez une fonction qui prend une liste de mots et retourne une liste de groupes d'anagrammes (mots formés des mêmes
lettres).
**Exemple** : `["écoute", "couteau", "tac", "cat", "acte"]` → `[["écoute"], ["couteau"], ["tac", "cat"], ["acte"]]`

---

## **Exercices combinant chaînes et fonctions**

### **Exercice 18 : Fonction de césar**

Écrivez une fonction qui applique un chiffrement de César (décalage de `n` lettres) à une chaîne.
**Exemple** : `cesar("Bonjour", 3)` → `"Erqmrxu"`

---

### **Exercice 19 : Fonction de capitalisation personnalisée**

Écrivez une fonction qui capitalise chaque mot d'une chaîne sauf une liste de mots exclus.
**Exemple** : `capitaliser("bonjour tout le monde", ["le"])` → `"Bonjour Tout le Monde"`

---

### **Exercice 20 : Fonction de troncature**

Écrivez une fonction qui tronque une chaîne à une longueur donnée et ajoute `"..."` si elle est plus longue.
**Exemple** : `tronquer("Bonjour tout le monde", 10)` → `"Bonjour..."`

---

---
**Conseils pour les exercices** :

- Utilisez les **méthodes de chaînes** (`split`, `join`, `replace`, etc.) et les **boucles/conditionnelles** pour
  résoudre les problèmes.
- Testez vos fonctions avec différents cas pour vérifier leur robustesse.

---