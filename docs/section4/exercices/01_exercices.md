# **Exercices 1 : Introduction à NumPy**

---

## **Exercices sur les constantes et fonctions mathématiques**

### **Exercice 1 : Utiliser les constantes de NumPy**

1. Affichez la valeur de π (`np.pi`) avec 4 décimales.
2. Calculez le périmètre d'un cercle de rayon 5 en utilisant `np.pi`.
3. Affichez la valeur de la constante `e` (`np.e`) et calculez \( e^2 \).

---

### **Exercice 2 : Fonctions trigonométriques**

1. Calculez le sinus, le cosinus et la tangente de \( \frac{\pi}{3} \) (60 degrés).
2. Vérifiez que \( \sin^2(x) + \cos^2(x) = 1 \) pour \( x = \frac{\pi}{4} \).

---

### **Exercice 3 : Fonctions exponentielles et logarithmes**

1. Calculez \( e^{3} \) en utilisant `np.exp`.
2. Calculez le logarithme naturel de 10 et le logarithme base 10 de 100.
3. Vérifiez que \( \log(e^5) = 5 \).

---

### **Exercice 4 : Racines et puissances**

1. Calculez la racine carrée de 16.
2. Calculez \( 3^4 \) en utilisant `np.power`.
3. Calculez la valeur absolue de -7.5.

---

## **Exercices sur les tableaux (`ndarray`)**

### **Exercice 5 : Créer des tableaux**

1. Créez un tableau 1D contenant les valeurs `[2, 4, 6, 8, 10]`.
2. Créez un tableau 2D (matrice) contenant les valeurs :
   ```
   [[1, 2, 3],
    [4, 5, 6]]
   ```
3. Créez un tableau de zéros de taille \( 3 \times 3 \).
4. Créez un tableau de uns de taille \( 2 \times 4 \).
5. Créez un tableau contenant les valeurs de 0 à 9 (inclus) avec un pas de 1.
6. Créez un tableau contenant 5 valeurs régulièrement espacées entre 0 et 1.

---

### **Exercice 6 : Propriétés des tableaux**

Pour chaque tableau créé dans l'exercice 5 :

1. Affichez le nombre de dimensions (`ndim`).
2. Affichez la forme du tableau (`shape`).
3. Affichez le nombre total d'éléments (`size`).
4. Affichez le type des éléments (`dtype`).

---

### **Exercice 7 : Tableaux spéciaux**

1. Créez une matrice identité de taille \( 4 \times 4 \).
2. Créez un tableau contenant les valeurs de 0 à 1 (inclus) avec 11 valeurs régulièrement espacées.

---

## **Exercices sur les fonctions mathématiques appliquées aux tableaux**

### **Exercice 8 : Fonctions élémentaires sur les tableaux**

1. Créez un tableau `angles` contenant les valeurs \( [0, \frac{\pi}{4}, \frac{\pi}{2}] \).
    - Calculez le sinus de chaque angle.
    - Calculez le cosinus de chaque angle.
2. Créez un tableau `nombres` contenant les valeurs `[1, 4, 9, 16]` et calculez leur racine carrée.

---

### **Exercice 9 : Fonctions statistiques**

1. Créez un tableau `notes` contenant les valeurs `[12, 15, 18, 9, 14]`.
    - Calculez la moyenne des notes.
    - Trouvez la note maximale et la note minimale.
    - Calculez l'écart-type des notes.
2. Créez un tableau 2D `matrice` contenant les valeurs :
   ```
   [[1, 2, 3],
    [4, 5, 6]]
   ```
    - Calculez la somme de tous les éléments.
    - Calculez la somme des éléments de chaque ligne.
    - Calculez la somme des éléments de chaque colonne.

---

### **Exercice 10 : Opérations arithmétiques sur les tableaux**

1. Créez deux tableaux `a` et `b` contenant respectivement `[1, 2, 3]` et `[4, 5, 6]` :
    - Calculez \( a + b \).
    - Calculez \( a \times b \) (multiplication élément par élément).
    - Calculez le produit scalaire de `a` et `b` (utilisez `@`).
2. Créez un tableau `c` contenant `[10, 20, 30]` et ajoutez 5 à chaque élément.

---

### **Exercice 11 : Indexation et slicing**

1. À partir du tableau 2D `matrice` de l'exercice 9 :
    - Affichez l'élément à la position (1, 2).
    - Affichez la première ligne.
    - Affichez la deuxième colonne.
    - Affichez la sous-matrice formée par les éléments des lignes 0 à 1 et des colonnes 1 à 2.

---

### **Exercice 12 : Modification des tableaux**

1. Créez un tableau 1D `vecteur` contenant les valeurs de 0 à 5.
    - Redimensionnez-le en un tableau 2D de forme \( 2 \times 3 \).
    - Affichez la transposée de ce tableau.
2. Créez un tableau `d` contenant `[1, 2, 3, 4, 5, 6]` et redimensionnez-le en un tableau 3D de forme \( 2 \times 3
   \times 1 \).

---

### **Exercice 13 : Calculs avancés**

1. Créez un tableau `x` contenant les valeurs de 0 à \( 2\pi \) avec 100 valeurs régulièrement espacées.
    - Calculez \( \sin(x) \) et \( \cos(x) \).
    - Affichez les 5 premières valeurs de \( \sin(x) \).
2. Créez un tableau `y` contenant les valeurs de \( x^2 \) pour \( x \) allant de 0 à 10 avec un pas de 1.

---

### **Exercice 14 : Masques et conditions**

1. Créez un tableau `valeurs` contenant `[5, 10, 15, 20, 25]`.
    - Créez un masque pour sélectionner les valeurs supérieures à 15.
    - Affichez les valeurs qui satisfont cette condition.
2. À partir du tableau `notes` de l'exercice 9, sélectionnez les notes supérieures ou égales à 15.

---

---
**Conseils pour les exercices** :

- Utilisez `import numpy as np` pour importer NumPy.
- Testez vos réponses en affichant les résultats.
- Utilisez les fonctions NumPy présentées dans la section précédente.

---
