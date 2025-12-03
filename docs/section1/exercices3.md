# **Exercices pratiques 3 : Utilisation des modules `random`, `math` et `datetime`**

---

## **Exercices avec le module `random`**

### **Exercice 1 : Lancer de dé**

Écrivez un programme qui simule un **lancer de dé à 6 faces** en utilisant `random.randint()`. Affichez le résultat.

---

### **Exercice 2 : Nombre aléatoire flottant**

Générez un **nombre flottant aléatoire** entre 5.0 et 10.0 en utilisant `random.uniform()`. Affichez le résultat avec 2
décimales.

---

### **Exercice 3 : Choix aléatoire**

Créez une liste de 5 fruits (ex. : `["pomme", "banane", "orange", "kiwi", "fraise"]`). Utilisez `random.choice()` pour
sélectionner un fruit aléatoire et affichez-le.

---

### **Exercice 4 : Mélanger une liste**

Créez une liste de 5 nombres entiers. Utilisez `random.shuffle()` pour mélanger cette liste, puis affichez-la avant et
après le mélange.

---

### **Exercice 5 : Échantillon aléatoire**

Créez une liste de nombres de 1 à 20. Utilisez `random.sample()` pour tirer un échantillon de 5 nombres aléatoires *
*sans répétition**, puis affichez cet échantillon.

---

### **Exercice 6 : Jeu de pile ou face**

Simulez un **lancer de pièce** (pile ou face) en utilisant `random.choice()`. Affichez le résultat.

---

---

## **Exercices avec le module `math`**

### **Exercice 7 : Calcul de racine carrée**

Demandez à l’utilisateur d’entrer un nombre. Utilisez `math.sqrt()` pour calculer sa racine carrée et affichez le
résultat avec 2 décimales.

---

### **Exercice 8 : Calcul de l’hypoténuse**

Demandez à l’utilisateur les longueurs des deux côtés d’un triangle rectangle. Utilisez `math.sqrt()` pour calculer
l’hypoténuse et affichez le résultat.

---

### **Exercice 9 : Calcul de sinus**

Demandez à l’utilisateur un angle en degrés. Convertissez-le en radians, puis utilisez `math.sin()` pour calculer son
sinus. Affichez le résultat avec 4 décimales.

*(Indice : Pour convertir des degrés en radians, utilisez `math.radians(degres)`.)*

---

### **Exercice 10 : Calcul de logarithme**

Demandez à l’utilisateur un nombre. Utilisez `math.log10()` pour calculer son logarithme en base 10 et affichez le
résultat.

---

### **Exercice 11 : Calcul de la circonférence d’un cercle**

Demandez à l’utilisateur le rayon d’un cercle. Utilisez `math.pi` pour calculer sa circonférence (formule :
`2 * π * rayon`) et affichez le résultat avec 2 décimales.

---

---

## **Exercices avec le module `datetime`**

### **Exercice 12 : Date et heure actuelles**

Utilisez `datetime.now()` pour afficher la **date et l’heure actuelles** au format `YYYY-MM-DD HH:MM:SS`.

---

### **Exercice 13 : Date formatée**

Utilisez `datetime.now()` et `strftime()` pour afficher la date actuelle au format `DD/MM/YYYY`.

---

### **Exercice 14 : Calcul de durée**

Demandez à l’utilisateur une date future (ex. : `2025-12-25`). Calculez le nombre de jours restants jusqu’à cette date
en utilisant `datetime` et `timedelta`. Affichez le résultat.

*(Indice : Soustrayez la date actuelle de la date future pour obtenir un objet `timedelta`, puis utilisez `.days`.)*

---

### **Exercice 15 : Âge en jours**

Demandez à l’utilisateur sa date de naissance (ex. : `YYYY-MM-DD`). Calculez son âge en jours et affichez-le.

---

### **Exercice 16 : Heure de fin d’un événement**

Demandez à l’utilisateur :

- Une heure de début (ex. : `14:30`).
- Une durée en heures et minutes (ex. : `2h45`).
  Calculez et affichez l’heure de fin de l’événement.

*(Indice : Utilisez `timedelta` pour ajouter la durée à l’heure de début.)*

---

---

## **Exercices combinés**

### **Exercice 17 : Simulation de lancer de dés**

Simulez 10 lancers d’un dé à 6 faces en utilisant `random.randint()`. Stockez les résultats dans une liste et affichez :

- La liste des résultats.
- La moyenne des lancers (utilisez `sum()` et `len()`).

---

### **Exercice 18 : Calcul de date aléatoire**

Générez une **date aléatoire** entre le 1er janvier 2020 et le 31 décembre 2025 en utilisant `random` et `datetime`.
Affichez cette date au format `DD/MM/YYYY`.

*(Indice : Générez un nombre aléatoire de jours entre les deux dates, puis ajoutez-le à la date de début.)*

---

### **Exercice 19 : Calcul de volume d’une sphère**

Demandez à l’utilisateur le rayon d’une sphère. Utilisez `math.pi` pour calculer son volume (formule :
`V = (4/3) * π * r^3`). Affichez le résultat avec 2 décimales.

---

### **Exercice 20 : Jeu de devinette amélioré**

Générez un nombre aléatoire entre 1 et 100. Demandez à l’utilisateur de deviner ce nombre. Utilisez une boucle pour :

- Donner des indices ("Trop grand" ou "Trop petit").
- Compter le nombre de tentatives.
- Afficher un message de félicitations une fois le nombre trouvé.

*(Indice : Utilisez `random.randint()` pour générer le nombre aléatoire.)*

---
