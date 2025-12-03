# **Exercices 2 : Utilisation de l'entrée standard**

---

## **Exercices de base**

### **Exercice 1 : Lecture et affichage simple**

Écrivez un programme qui demande à l’utilisateur :

- Son prénom
- Son nom
  Puis affichez : `Bonjour [prénom] [nom], bienvenue !`

---

### **Exercice 2 : Calcul de surface**

Demandez à l’utilisateur :

- La longueur d’un rectangle (en mètres)
- La largeur du rectangle (en mètres)
  Calculez et affichez la surface du rectangle.

---

### **Exercice 3 : Conversion de température**

Demandez à l’utilisateur une température en degrés Celsius, puis :

- Convertissez-la en Fahrenheit (formule : `F = C * 9/5 + 32`).
- Affichez le résultat **arrondi à 1 décimale**.

---

### **Exercice 4 : Calcul de moyenne**

Demandez à l’utilisateur trois notes (sur 20), puis :

- Calculez la moyenne.
- Affichez la moyenne **arrondie à 2 décimales** et **formatée avec `:.2f`**.

---

### **Exercice 5 : Prix total**

Demandez à l’utilisateur :

- Le prix unitaire d’un produit (en dollars).
- La quantité achetée.
  Calculez et affichez le **prix total** (arrondi à 2 décimales).

---

---

## **Exercices intermédiaires**

### **Exercice 6 : Conversion de devises**

Demandez à l’utilisateur :

- Un montant en euros.
- Le taux de change (ex. : 1 EUR = 1.2 USD).
  Convertissez le montant en dollars et affichez le résultat.

---

### **Exercice 7 : Calcul d’IMC**

Demandez à l’utilisateur :

- Son poids (en kg).
- Sa taille (en mètres).
  Calculez son **Indice de Masse Corporelle (IMC)** avec la formule :
  `IMC = poids / (taille ** 2)`
  Affichez le résultat **arrondi à 1 décimale**.

---

### **Exercice 8 : Lecture de plusieurs valeurs en une ligne**

Demandez à l’utilisateur d’entrer **trois nombres séparés par des espaces** (ex. : `10 20 30`).

- Lisez ces nombres en une seule ligne avec `input().split()`.
- Convertissez-les en entiers.
- Affichez leur somme.

---

### **Exercice 9 : Calcul de périmètre**

Demandez à l’utilisateur le rayon d’un cercle, puis :

- Calculez son périmètre (formule : `2 * π * rayon`).
- Affichez le résultat **formaté avec 2 décimales**.

---

### **Exercice 10 : Gestion de temps**

Demandez à l’utilisateur un nombre de minutes, puis :

- Convertissez ce nombre en **heures et minutes** (ex. : 130 minutes = 2h10).
- Affichez le résultat sous la forme `XhYY`.

---

---

## **Exercices avancés**

### **Exercice 11 : Calcul de factorielle**

Demandez à l’utilisateur un nombre entier positif, puis :

- Calculez sa factorielle (ex. : `5! = 5 * 4 * 3 * 2 * 1 = 120`).
- Affichez le résultat.

---

### **Exercice 12 : Lecture et traitement de liste**

Demandez à l’utilisateur d’entrer **5 nombres séparés par des virgules** (ex. : `1,2,3,4,5`).

- Convertissez ces nombres en une liste d’entiers.
- Calculez et affichez la **somme** et la **moyenne** de ces nombres.

---

### **Exercice 13 : Conversion de temps en secondes**

Demandez à l’utilisateur une durée sous la forme `HH:MM:SS` (ex. : `01:30:45`), puis :

- Convertissez cette durée en **secondes**.
- Affichez le résultat.

---

### **Exercice 14 : Calcul de distance**

Demandez à l’utilisateur :

- La vitesse (en km/h).
- Le temps (en heures).
  Calculez et affichez la distance parcourue (formule : `distance = vitesse * temps`).

---

### **Exercice 15 : Jeu de devinette**

Générez un nombre aléatoire entre 1 et 100.
Demandez à l’utilisateur de deviner ce nombre.

- Si le nombre est trop grand ou trop petit, donnez un indice.
- Répétez jusqu’à ce que l’utilisateur trouve le bon nombre.

---

---

## **Exercices bonus (pour aller plus loin)**

### **Exercice 16 : Calcul de pourcentage**

Demandez à l’utilisateur :

- Un nombre total (ex. : 500).
- Un nombre partiel (ex. : 125).
  Calculez et affichez le pourcentage que représente le nombre partiel par rapport au total.

---

### **Exercice 17 : Lecture et validation**

Demandez à l’utilisateur un nombre entre 1 et 100.

- Tant que l’entrée n’est pas un nombre valide dans cet intervalle, redemandez-lui.
- Affichez le nombre une fois qu’il est valide.

*(Note : Cet exercice nécessite une boucle `while`, mais sans gestion d’exceptions pour l’instant.)*

---

### **Exercice 18 : Calcul de volume**

Demandez à l’utilisateur :

- Le rayon d’une sphère.
  Calculez et affichez son volume (formule : `V = (4/3) * π * r^3`).

---
