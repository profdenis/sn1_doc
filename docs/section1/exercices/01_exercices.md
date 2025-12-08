# **Exercices 1 : Affichage sur la sortie standard**

---

## **Partie 1 : Utilisation de `print()` (sans `.format()` ni f-strings)**

### **Exercice 1 : Affichage simple**

Affiche les phrases suivantes en utilisant uniquement `print()` :

1. `Bonjour, monde !`
2. `La réponse est 42.`
3. `Python` et `est` et `génial` sur la même ligne, séparés par un tiret (`-`).

---

### **Exercice 2 : Paramètres `sep` et `end`**

1. Affiche les mots `"Science"`, `"Nature"`, et `"Programmation"` séparés par un slash (`/`).
2. Affiche `"Chargement"` suivi de trois points (`...`) **sans sauter de ligne** entre chaque point.
3. Affiche la date du jour sous la forme `25/12/2025` en utilisant trois `print()` différents (un pour le jour, un pour
   le mois, un pour l’année), sans saut de ligne entre eux.

---

### **Exercice 3 : Combinaison de `sep` et `end`**

1. Affiche la phrase suivante en une seule instruction `print()` :
   `Les notes : 15, 18, 12.`
   (Utilise `sep` pour les virgules et `end` pour le point final.)
2. Affiche un compte à rebours de 3 à 1, chaque nombre sur la même ligne, séparé par `>`, suivi de `"Décollage !"` sur
   une nouvelle ligne.

---

## **Partie 2 : Utilisation de `.format()` et des f-strings**

### **Exercice 4 : Formatage de base**

Réécris les instructions suivantes en utilisant **à la fois `.format()` et les f-strings** :

1. Affiche : `Bonjour, [prénom] !` où `[prénom]` est une variable `prenom = "Denis"`.
2. Affiche : `Le résultat de 5 + 3 est 8.` en utilisant des variables pour les nombres et le résultat.

---
**Question bonus** : Quelle méthode préfères-tu pour ces exemples ? Pourquoi ?

---

### **Exercice 5 : Formatage avancé**

1. **Avec `.format()` et f-strings** :
   Affiche la phrase suivante en utilisant une variable `prix = 12.3456` :
   `Le prix est 12.35 $.` (Arrondis à deux décimales.)

2. **Avec f-strings uniquement** :
   Affiche : `Le carré de 5 est 25.` en calculant le carré directement dans la f-string.

---
**Question bonus** : Pourquoi les f-strings sont-elles plus adaptées pour le calcul direct dans la chaîne ?

---

### **Exercice 6 : Alignement et remplissage**

1. **Avec `.format()`** :
   Affiche le mot `"Python"` centré dans une chaîne de 20 caractères, avec des `#` comme caractère de remplissage :
   `######Python######`

2. **Avec f-strings** :
   Affiche la même chose que ci-dessus.

---
**Question bonus** : Trouves-tu une méthode plus intuitive que l’autre pour cet exercice ?

---

### **Exercice 7 : Choix personnel**

Réécris les instructions suivantes en utilisant **la méthode de ton choix** (`.format()` ou f-strings) :

1. Affiche : `L’étudiant Denis Rinfret a obtenu 18/20.`
   (Utilise les variables `nom = "Denis Rinfret"` et `note = 18`.)

2. Affiche : `La température moyenne est de 22.5°C.`
   (Utilise la variable `temperature = 22.5`.)

---
**Question bonus** : Justifie ton choix de méthode pour chaque cas.

---

### **Exercice 8 : Conversion et formatage**

1. Convertis la variable `minutes = 125` en heures et minutes (2h05), puis affiche :
   `La durée est 2h05.`
   (Fais-le avec `.format()` **et** avec f-strings.)

2. Affiche la liste `notes = [12, 15, 18]` sous la forme :
   `Notes : 12, 15, 18.`
   (Utilise la méthode de ton choix.)

---
**Question bonus** : Quelle méthode est la plus adaptée pour formater des listes ? Pourquoi ?

---

## **Partie 3 : Défis combinés**

### **Exercice 9 : Tableau de multiplication**

Affiche un tableau de multiplication pour les nombres de 1 à 5, sous la forme :

```
1 x 1 = 1
1 x 2 = 2
...
5 x 5 = 25
```

- Utilise une boucle `for` et la méthode de formatage de ton choix.

---
**Question bonus** : Comment ferais-tu pour aligner les résultats à droite ?

---

### **Exercice 10 : Menu interactif**

Crée un menu simple qui affiche :

```
Menu :
1. Afficher la date
2. Calculer une moyenne
3. Quitter
```

- Utilise `print()` avec `sep` et `end` pour formater le menu.
- Pour chaque option, utilise `.format()` ou les f-strings pour afficher un message personnalisé (ex. :
  `"Vous avez choisi l'option 1."`).


