# **Exercices 1 : Affichage sur la sortie standard**

---

## **Partie 1 : Utilisation de `print()` (sans `.format()` ni _f-strings_)**

### **Exercice 1 : Affichage simple**

Affiche les phrases suivantes en utilisant uniquement `print()` :

1. `Bonjour, monde !`
2. `La réponse est 42.`
3. `Python` et `est` et `génial` sur la même ligne, séparés par un tiret (`-`), en passant chaque mot un par un à la
   fonction `print`.

---

### **Exercice 2 : Paramètres `sep` et `end`**

1. Affiche les mots `"Science"`, `"Nature"`, et `"Programmation"` séparés par un slash (`/`), en passant chaque mot un
   par un à la fonction `print`.
2. Affiche `"Chargement"` suivi de trois points (`...`) **sans sauter de ligne** entre chaque point, en utilisant 
   quatre `print` différents.
3. Affiche la date du jour sous la forme `25/12/2025` en utilisant trois `print()` différents (un pour le jour, un pour
   le mois, un pour l’année), sans saut de ligne entre eux.

---

### **Exercice 3 : Combinaison de `sep` et `end`**

1. Affiche la phrase suivante en une seule instruction `print()` :
   `Les notes : 15, 18, 12.`
   (Les notes doivent être donnés sous forme d'entiers, et utilise `sep` pour les virgules et `end` pour le point 
   final.)
2. Affiche un compte à rebours de 3 à 1, chaque nombre sur la même ligne, séparé par `>`, suivi de `"Décollage !"` sur
   une nouvelle ligne, en utilisant 
   quatre `print` différents.

---

## **Partie 2 : Utilisation de `.format()` et des _f-strings_**

### **Exercice 4 : Formatage de base**

Réécris les instructions suivantes en utilisant **à la fois `.format()` et les _f-strings_** :

1. Affiche : `Bonjour, [prénom] !` où `[prénom]` est une variable `prenom = "Denis"`.
2. Affiche : `Le résultat de 5 + 3 est 8.` en utilisant des variables pour les nombres et le résultat.

---
**Question bonus** : Quelle méthode préfères-tu pour ces exemples ? Pourquoi ?

---

### **Exercice 5 : Formatage avancé**

1. **Avec `.format()` et _f-strings_** :
   Affiche la phrase suivante en utilisant une variable `prix = 12.3456` :
   `Le prix est 12.35 $.` (Arrondis à deux décimales.)

2. **Avec _f-strings_ uniquement** :
   Affiche : `Le carré de 5 est 25.` en calculant le carré directement dans la f-string.

---
**Question bonus** : Pourquoi les _f-strings_ sont-elles plus adaptées pour le calcul direct dans la chaîne ?

---

### **Exercice 6 : Alignement et remplissage**

1. **Avec `.format()`** :
   Affiche le mot `"Python"` centré dans une chaîne de 20 caractères, avec des `#` comme caractère de remplissage :
   `######Python######`

2. **Avec _f-strings_** :
   Affiche la même chose que ci-dessus.

---
**Question bonus** : Trouves-tu une méthode plus intuitive que l’autre pour cet exercice ?

---

### **Exercice 7 : Choix personnel**

Réécris les instructions suivantes en utilisant **la méthode de ton choix** (`.format()` ou _f-strings_) :

1. Affiche : `L’étudiant Jean Tremblay a obtenu 18/20.`
   (Utilise les variables `nom = "Jean Tremblay"` et `note = 18`.)

2. Affiche : `La température moyenne est de 22.5°C.`
   (Utilise la variable `temperature = 22.5`.)

---
**Question bonus** : Justifie ton choix de méthode pour chaque cas.

---

### **Exercice 8 : Conversion et formatage**

1. Convertis la variable `minutes = 125` en heures et minutes (2h05), puis affiche :
   `La durée est 2h05.`
   (Fais-le avec `.format()` **et** avec _f-strings_.)

2. Affiche la liste `notes = [12, 15, 18]` sous la forme :
   `Notes : 12, 15, 18.`
   (Utilise la méthode de ton choix.)

---
**Question bonus** : Quelle méthode est la plus adaptée pour formater des listes ? Pourquoi ?

---



## **Partie 3 : Exercices sur les _f-strings_**

### **Exercice 1 : Affichage simple**

Créez une _f-string_ pour afficher la phrase suivante en utilisant les variables fournies :

- `nom = "Alice"`
- `age = 25`

Résultat attendu : `"Alice a 25 ans."`

---

### **Exercice 2 : Calculs dans les _f-strings_**

Utilisez une _f-string_ pour afficher le résultat de l'opération suivante :

- `a = 10`
- `b = 3`

Résultat attendu : `"10 divisé par 3 est égal à 3.3333333333333335."`

---

### **Exercice 3 : Formatage des flottants**

Formatez les variables suivantes pour afficher les valeurs avec **2 décimales** :

- `prix = 12.3456789`
- `taux = 0.123456789`

Résultat attendu :

```
Prix : 12.35 $
Taux : 12.35 %
```

---

### **Exercice 4 : Formatage des entiers**

Formatez les variables suivantes pour afficher les valeurs avec **3 chiffres et un remplissage de zéros** :

- `jour = 5`
- `mois = 12`
- `annee = 2023`

Résultat attendu : `"005/012/2023"`

---

### **Exercice 5 : Alignement du texte**

Utilisez les _f-strings_ pour aligner les mots suivants dans une colonne de **15 caractères** (alignement à gauche,
centré, et à droite) :

- `mot = "Bonjour"`

Résultat attendu :

```
Bonjour______   (aligné à gauche)
___Bonjour___   (centré)
______Bonjour   (aligné à droite)
```

---

### **Exercice 6 : Formatage scientifique**

Formatez la variable suivante en notation scientifique avec **3 décimales** :

- `grand_nombre = 123456789`

Résultat attendu : `"1.235e+08"`

---

### **Exercice 7 : Formatage binaire, octal et hexadécimal**

Formatez la variable suivante en **binaire**, **octal** et **hexadécimal** :

- `nombre = 255`

Résultat attendu :

```
Binaire : 11111111
Octal : 377
Hexadécimal : 0xff
```

---

### **Exercice 8 : Séparateurs de milliers**

Formatez la variable suivante avec des **séparateurs de milliers** :

- `grand_nombre = 1000000`

Résultat attendu : `"1,000,000"`

---

### **Exercice 9 : Affichage des signes**

Formatez les variables suivantes pour afficher le signe (positif ou négatif) :

- `positif = 123`
- `negatif = -456`

Résultat attendu :

```
Positif : +123
Négatif : -456
```

---

### **Exercice 10 : Formatage des pourcentages**

Formatez la variable suivante pour afficher un **pourcentage avec 2 décimales** :

- `taux = 0.7563`

Résultat attendu : `"75.63%"`

---

### **Exercice 11 : Formatage des durées**

Formatez les variables suivantes pour afficher une durée sous la forme `HH:MM:SS` :

- `secondes = 3661`

Résultat attendu : `"01:01:01"`

---

### **Exercice 12 : Formatage monétaire**

Formatez la variable suivante pour afficher un montant monétaire avec **2 décimales et un symbole $** :

- `prix = 1234.56789`

Résultat attendu : `"1,234.57 $"`

---

### **Exercice 13 : Combinaison de spécificateurs**

Formatez la variable suivante en combinant plusieurs spécificateurs :

- `nombre = 12345.6789`

Résultat attendu : `"   +12,345.68"`


---

### **Exercice 14 : Formatage personnalisé**

Créez une _f-string_ pour afficher une facture avec les informations suivantes :

- `client = "Jean Dupont"`
- `montant_ht = 123.456`
- `taux_tva = 0.15`
- `montant_ttc = montant_ht * (1 + taux_tva)`

Résultat attendu :

```
Facture pour Jean Dupont
Montant HT : 123.46 $
Taxes (15.00 %) : 18.52 $
Montant TTC : 141.98 $
```

---

---
**Conseils pour les exercices** :

- Utilisez les **_f-strings_** pour formater les chaînes de caractères.
- Consultez le **tableau récapitulatif des spécificateurs de format** pour vous aider.
- Testez vos solutions avec différentes valeurs pour vérifier leur robustesse.


----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.