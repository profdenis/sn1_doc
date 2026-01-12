# **Exercices 2 : `matplotlib.pyplot`**

---

## **Exercices de base (inspirés des exemples)**

### **Exercice 1 : Tracer un point**

Tracez un point rouge aux coordonnées `(3, 7)` avec une légende "Mon point".

---

### **Exercice 2 : Tracer plusieurs points**

Tracez trois points :

- Un cercle bleu à `(1, 2)`
- Un carré vert à `(3, 5)`
- Un triangle magenta à `(2, 7)`

Ajoutez un titre "Trois points".

---

### **Exercice 3 : Tracer une ligne**

Tracez une ligne bleue reliant les points `(0, 0)`, `(1, 3)`, `(2, 1)`, et `(3, 4)`.

---

### **Exercice 4 : Personnalisation des couleurs et symboles**

Tracez deux courbes :

- Une ligne pointillée rouge reliant `(0, 0)`, `(1, 2)`, `(2, 1)`
- Une ligne en tirets verts reliant `(0, 1)`, `(1, 3)`, `(2, 0)`

Ajoutez des étiquettes aux axes et un titre.

---

### **Exercice 5 : Ajouter une légende**

Tracez deux courbes :

- `y = x` (ligne bleue continue)
- `y = x²` (ligne rouge pointillée)

Ajoutez une légende, des étiquettes aux axes, et un titre.

---

### **Exercice 6 : Diagramme en barres**

Créez un diagramme en barres pour les données suivantes :

- Catégories : `["A", "B", "C", "D"]`
- Valeurs : `[10, 24, 36, 18]`

Ajoutez un titre et des étiquettes aux axes.

---

### **Exercice 7 : Diagramme en secteurs**

Créez un diagramme en secteurs (camembert) pour les données suivantes :

- Catégories : `["Pommes", "Bananes", "Cerises", "Dattes"]`
- Valeurs : `[35, 25, 20, 20]`

Affichez les pourcentages sur chaque secteur.

---

### **Exercice 8 : Diagramme de dispersion**

Générez 50 points aléatoires entre 0 et 1 pour `x` et `y`, puis tracez un diagramme de dispersion avec des cercles
bleus.

---

### **Exercice 9 : Tracer plusieurs courbes**

Tracer les courbes suivantes sur le même graphique :

- `y = x`
- `y = x²`
- `y = x³`

Chaque courbe doit avoir une couleur et un style de ligne différents.

---

### **Exercice 10 : Tracer une fonction conditionnelle**

Tracez la fonction suivante :

- `y = x` si `x < 2`
- `y = 4` si `x >= 2`

pour `x` allant de 0 à 4 avec un pas de 0.1.

---

### **Exercice 11 : Tracer des données depuis un tableau NumPy**

Créez un tableau NumPy `x` contenant 100 valeurs entre 0 et \(2\pi\), puis tracez :

- `y = sin(x)`
- `y = cos(x)`

sur le même graphique avec des légendes et des étiquettes.

---

### **Exercice 12 : Tracer des données avec validation**

Écrivez une fonction qui :

1. Lit un fichier texte contenant des paires `(x, y)` (une paire par ligne).
2. Valide que chaque ligne contient bien deux nombres (utilisez `try/except`).
3. Trace les points valides avec des cercles rouges et ignore les lignes invalides.

Exemple de fichier :

```
1 2
2 3
trois 4
4 5
```

---

### **Exercice 13 : Tracer des sous-graphiques**

Utilisez une boucle pour créer 4 sous-graphiques (2 lignes, 2 colonnes) affichant :

- `y = sin(x)`
- `y = cos(x)`
- `y = tan(x)`
- `y = x²`

pour `x` allant de 0 à \(2\pi\).

---

### **Exercice 14 : Tracer des barres conditionnelles**

Créez un diagramme en barres pour les données suivantes :

- Catégories : `["A", "B", "C", "D", "E"]`
- Valeurs : `[15, 7, 22, 13, 9]`

Colorez les barres en rouge si la valeur est supérieure à 10, sinon en bleu.

---

### :material-checkbox-blank-outline: **Exercice 15 : Tracer des données avec des masques NumPy**

Générez un tableau NumPy `x` de 100 valeurs entre 0 et \(4\pi\), puis :

1. Calculez `y = sin(x)`.
2. Utilisez un masque pour tracer uniquement les points où `y > 0` en rouge et les autres en bleu.

---

### :material-checkbox-blank-outline: **Exercice 16 : Tracer des données avec gestion d'erreurs**

Écrivez une fonction qui :

1. Demande à l'utilisateur d'entrer une liste de valeurs pour `x` et `y` (séparées par des virgules).
2. Valide les entrées (utilisez `try/except`).
3. Trace les points `(x, y)` avec des carrés verts.

---

### :material-checkbox-blank-outline: **Exercice 17 : Tracer une fonction par morceaux**

Tracez la fonction suivante :

- `y = x²` si `x < 0`
- `y = x` si `0 <= x < 2`
- `y = 4` si `x >= 2`

pour `x` allant de -3 à 3 avec un pas de 0.1.

---

### :material-checkbox-blank-outline: **Exercice 18 : Tracer des données depuis un tableau 2D**

Créez un tableau NumPy 2D où chaque ligne représente une série de données, puis tracez chaque série sur le même
graphique avec une couleur et un style différents.

Exemple de tableau :

```python
donnees = np.array([
    [0, 1, 4, 9],
    [0, 1, 2, 3],
    [0, 1, 8, 27]
])
```

---

### **Exercice 19 : Tracer des histogrammes**

Générez 1000 valeurs aléatoires suivant une distribution normale (moyenne = 0, écart-type = 1), puis tracez un
histogramme avec 30 bins.

---

### :material-checkbox-blank-outline: **Exercice 20 : Tracer des données avec des boucles et des conditions**

Tracez les fonctions suivantes sur le même graphique, en utilisant une boucle et des conditions pour choisir les
couleurs :

- `y = sin(x)` en bleu
- `y = cos(x)` en rouge
- `y = sin(x) + cos(x)` en vert

pour `x` allant de 0 à \(2\pi\) avec un pas de 0.1.

---

---
**Conseils pour les exercices** :

- Utilisez `import matplotlib.pyplot as plt` et `import numpy as np`.
- Pour les exercices combinés, utilisez des boucles, des conditionnelles, et la gestion d'erreurs pour rendre vos
  programmes robustes.
- Testez vos programmes avec différentes valeurs pour vérifier leur bon fonctionnement.

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
