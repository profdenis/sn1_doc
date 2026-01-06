# **Exercices pratiques 3 : Importation de modules**

---

## **Exercices avec le module `random`**

### **Exercice 1 : Lancer de dé**

Écrivez un programme qui simule un **lancer de dé à 6 faces** en utilisant `random.randint()`. Affichez le résultat.

---

### **Exercice 2 : Nombre aléatoire flottant**

Générez un **nombre flottant aléatoire** entre 5.0 et 10.0 en utilisant `random.uniform()`. Affichez le résultat avec 2
décimales.

---



---

## **Exercices avec le module `math`**

### **Exercice 3 : Calcul de racine carrée**

Demandez à l’utilisateur d’entrer un nombre. Utilisez `math.sqrt()` pour calculer sa racine carrée et affichez le
résultat avec 2 décimales.

---

### **Exercice 4 : Calcul de l’hypoténuse**

Demandez à l’utilisateur les longueurs des deux côtés d’un triangle rectangle. Utilisez `math.sqrt()` pour calculer
l’hypoténuse et affichez le résultat.

---

### **Exercice 5 : Calcul de sinus**

Demandez à l’utilisateur un angle en degrés. Convertissez-le en radians, puis utilisez `math.sin()` pour calculer son
sinus. Affichez le résultat avec 4 décimales.

*(Indice : Pour convertir des degrés en radians, utilisez `math.radians(degres)`.)*

---

### **Exercice 6 : Calcul de logarithme**

Demandez à l’utilisateur un nombre. Utilisez `math.log10()` pour calculer son logarithme en base 10 et affichez le
résultat.

---

### **Exercice 7 : Calcul de la circonférence d’un cercle**

Demandez à l’utilisateur le rayon d’un cercle. Utilisez `math.pi` pour calculer sa circonférence (formule :
`2 * π * rayon`) et affichez le résultat avec 2 décimales.

---

---

## **Exercices avec le module `datetime`**

### **Exercice 8 : Date et heure actuelles**

Utilisez `datetime.now()` pour afficher la **date et l’heure actuelles** au format `YYYY-MM-DD HH:MM:SS`.

---

### **Exercice 9 : Date formatée**

Utilisez `datetime.now()` et `strftime()` pour afficher la date actuelle au format `DD/MM/YYYY`.

---

### **Exercice 10 : Calcul de durée**

Demandez à l’utilisateur une date future (ex. : `2025-12-25`). Calculez le nombre de jours restants jusqu’à cette date
en utilisant `datetime` et `timedelta`. Affichez le résultat.

*(Indice : Soustrayez la date actuelle de la date future pour obtenir un objet `timedelta`, puis utilisez `.days`.)*

---

### **Exercice 11 : Âge en jours**

Demandez à l’utilisateur sa date de naissance (ex. : `YYYY-MM-DD`). Calculez son âge en jours et affichez-le.

---

### **Exercice 12 : Heure de fin d’un événement**

Demandez à l’utilisateur :

- Une heure de début (ex. : `14:30`).
- Une durée en heures et minutes (ex. : `2h45`).
  Calculez et affichez l’heure de fin de l’événement.

*(Indice : Utilisez `timedelta` pour ajouter la durée à l’heure de début.)*

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
