---
icon: material/checkbox-outline
---

# 1. Qu’est-ce que la programmation ?

## **1. Définitions et analogies**

**Objectif** : Expliquer la programmation comme un outil pour résoudre des problèmes.

### **1.1 Qu’est-ce qu’un programme ?**

- **Définition** : Un programme est une **séquence d’instructions** écrites dans un langage compréhensible par un
  ordinateur, pour accomplir une tâche spécifique.
- **Analogie** :
    - Une recette de cuisine : les ingrédients sont les **données**, les étapes sont les **instructions**, et le plat
      final est le **résultat**.
    - Un protocole de laboratoire : chaque étape est une instruction, et le résultat est l’observation ou la mesure.

### **1.2 Pourquoi programmer ?**

- **Automatisation** : Éviter les tâches répétitives (ex. : calculer la moyenne de 1000 mesures).
- **Précision** : Éviter les erreurs humaines (ex. : calculs complexes en physique).
- **Modélisation** : Simuler des phénomènes naturels (ex. : croissance d’une population, trajectoire d’un projectile).

### **1.3 Qu’est-ce qu’un algorithme ?**

- **Définition** : Un algorithme est une **méthode étape par étape** pour résoudre un problème ou accomplir une tâche.
  C’est une **recette logique**, indépendante du langage de programmation.
- **Exemple** :
    - **Algorithme pour faire un café** :
        1. Faire bouillir de l’eau.
        2. Mettre du café moulu dans une tasse.
        3. Verser l’eau bouillante sur le café.
        4. Attendre 3 minutes.
        5. Boire le café.

### **1.3 Algorithme vs. Programme**

| **Algorithme**                                             | **Programme**                                                         |
|------------------------------------------------------------|-----------------------------------------------------------------------|
| Description abstraite des étapes.                          | Implémentation concrète dans un langage (ex. : Python).               |
| Indépendant de la machine.                                 | Dépend du langage et de l’ordinateur.                                 |
| Exemple : « Trouver le plus grand nombre dans une liste. » | Exemple : Code Python qui utilise une boucle pour trouver le maximum. |

---

## **2. Langages de programmation et Python**

**Objectif** : Présenter Python comme un outil accessible et puissant.

### **2.1 Qu’est-ce qu’un langage de programmation ?**

- **Langage naturel** vs **langage machine** :
    - Les humains parlent français, anglais, etc.
    - Les ordinateurs comprennent le **binaire** (0 et 1).
    - Un langage de programmation est un **intermédiaire** entre les deux.

### **2.2 Pourquoi Python ?**

- **Simple et lisible** : Syntaxe proche de l’anglais.
- **Polyvalent** : Utilisé en sciences, ingénierie, data science, IA, etc.
- **Communauté active** : Beaucoup de ressources et de bibliothèques (ex. : NumPy pour les calculs scientifiques).

**Exemple simple** :

```python
# Calcul de la vitesse moyenne
distance = 100  # en mètres
temps = 10  # en secondes
vitesse = distance / temps
print(f"La vitesse est de {vitesse} m/s.")
```

---

## **3. Concepts de base en programmation**

**Objectif** : Introduire les briques fondamentales.

### **3.1 Variables et types de données**

- **Variable** : Une « boîte » qui contient une information (ex. : `temperature = 25.5`).
- **Types de données** :
    - **Entiers** (`int`) : `42`
    - **Nombres à virgule** (`float`) : `3.14`
    - **Texte** (`str`) : `"ADN"`
    - **Booléens** (`bool`) : `True` ou `False`

### **3.2 Instructions et séquences**

- Un programme est une **séquence d’instructions** exécutées dans l’ordre.
- Exemple :
  ```python
  # Calcul de l'aire d'un cercle
  rayon = 5
  aire = 3.14 * rayon ** 2
  print(f"L'aire est {aire}.")
  ```

### **3.3 Structures de contrôle**

- **Conditions** (`if/else`) : Prendre des décisions.
  ```python
  temperature = 22
  if temperature > 20:
      print("Il fait chaud !")
  else:
      print("Il fait frais.")
  ```
- **Boucles** (`for`, `while`) : Répéter des actions.
  ```python
  # Afficher les nombres de 1 à 5
  for i in range(1, 6):
      print(i)
  ```

---

## **4. Applications en sciences de la nature**

**Objectif** : Montrer l’utilité concrète de la programmation.

### **4.1 Exemples d’utilisation**

- **Biologie** :
    - Analyser des séquences d’ADN pour identifier des gènes.
    - Simuler la croissance d’une population de bactéries en fonction des ressources disponibles.
    - Automatiser le traitement de données de séquençage (ex. : trouver des mutations).
- **Physique** :
    - Calculer la trajectoire d’un projectile en tenant compte de la gravité et de la résistance de l’air.
    - Simuler le comportement d’un circuit électrique (lois de Kirchhoff).
    - Analyser des données expérimentales pour valider une hypothèse.
- **Chimie** :
    - Calculer les concentrations molaires dans une solution après une réaction.
    - Prédire les produits d’une réaction chimique à partir des réactifs.
    - Automatiser le calcul du pH d’une solution tampon.
- **Environnement** :
    - Modéliser l’évolution de la concentration de CO₂ dans l’atmosphère.
    - Analyser des données météorologiques pour prédire les changements climatiques.
    - Simuler la dispersion d’un polluant dans un cours d’eau.
- **Mathématiques** :
    - Résoudre des équations différentielles pour modéliser des phénomènes naturels.
    - Calculer des intégrales numériquement pour déterminer des aires sous des courbes.
    - Générer des graphiques 3D pour visualiser des fonctions complexes.

### **4.2 Exemple : Calcul de la moyenne**

```python
# Liste de mesures de pH
ph_echantillons = [6.2, 6.5, 6.3, 6.7, 6.4]
moyenne = sum(ph_echantillons) / len(ph_echantillons)
print(f"Le pH moyen est {moyenne:.2f}.")
```

---

## **5. Applications de la programmation dans d'autres domaines**

La programmation n'est pas limitée aux sciences naturelles. Elle est un outil polyvalent utilisé dans de nombreux
secteurs. Voici quelques exemples d'applications dans d'autres domaines :

---

### **5.1 Jeux vidéo**

- **Développement de jeux** : Les moteurs de jeu comme Unity (C#) ou Unreal Engine (C++) permettent de créer des mondes
  virtuels interactifs.
    - **Exemple** : Un jeu de plateforme où le joueur doit sauter pour éviter des obstacles.
    - **Concepts clés** : Boucles pour les animations, conditions pour les collisions, variables pour les scores.

---

### **5.2 Développement web**

- **Sites web et applications** : HTML, CSS, et JavaScript sont utilisés pour créer des interfaces interactives.
    - **Exemple** : Un site de commerce en ligne où les utilisateurs peuvent ajouter des produits à un panier.
    - **Concepts clés** : Gestion des événements (clics, soumissions de formulaires), communication avec des bases de
      données.

---

### **5.3 Finances et banques**

- **Gestion des transactions** : Les systèmes bancaires utilisent des langages comme Java ou Python pour gérer les
  comptes, les transactions et la sécurité.
    - **Exemple** : Un programme qui calcule les intérêts composés sur un compte épargne.
    - **Concepts clés** : Boucles pour les calculs récurrents, conditions pour vérifier les soldes, sécurité des
      données.

```python
# Exemple simplifié : Calcul d'intérêts composés
capital_initial = 1000
taux_interet = 0.05  # 5%
annees = 10
capital_final = capital_initial * (1 + taux_interet) ** annees
print(f"Capital final après {annees} ans : {capital_final:.2f} $")
```

---

### **5.4 Ressources humaines (RH)**

- **Gestion des employés** : Les logiciels de RH utilisent des bases de données et des scripts pour gérer les dossiers
  des employés, les paies et les congés.
    - **Exemple** : Un programme qui calcule automatiquement les heures de travail et les salaires.
    - **Concepts clés** : Structures de données pour stocker les informations, boucles pour traiter les données de
      plusieurs employés.

```python
# Exemple simplifié : Calcul du salaire mensuel
heures_travaillees = 160
taux_horaire = 20.50
salaire = heures_travaillees * taux_horaire
print(f"Salaire mensuel : {salaire:.2f} $")
```

---

### **5.5 Intelligence artificielle et apprentissage automatique**

- **Automatisation et prédictions** : Python (avec des bibliothèques comme TensorFlow ou PyTorch) est largement utilisé
  pour créer des modèles d'IA.
    - **Exemple** : Un programme qui prédit les tendances du marché boursier.
    - **Concepts clés** : Traitement des données, algorithmes d'apprentissage, évaluation des modèles.

---

### **5.6 Art et design**

- **Création d'œuvres d'art génératives** : Des programmes comme Processing (Java) ou des scripts Python permettent de
  créer des visuels artistiques.
    - **Exemple** : Un programme qui génère des motifs géométriques aléatoires.
    - **Concepts clés** : Boucles pour les répétitions, fonctions mathématiques pour les formes, aléatoire pour la
      variété.

---

### **5.7 Résumé des applications par domaine**

| **Domaine**               | **Exemples d'applications**          | **Langages/Outils courants**           |
|---------------------------|--------------------------------------|----------------------------------------|
| Jeux vidéo                | Développement de jeux, simulations   | C++, C#, Unity, Unreal Engine          |
| Développement web         | Sites web, applications interactives | HTML, CSS, JavaScript, Python (Django) |
| Finances et banques       | Gestion des comptes, transactions    | Java, Python, SQL                      |
| Ressources humaines       | Gestion des employés, paie           | Python, SQL, Excel                     |
| Intelligence artificielle | Prédictions, automatisation          | Python (TensorFlow, PyTorch)           |
| Art et design             | Œuvres génératives, animations       | Processing, Python (Pygame)            |

---

### **5.8 Pourquoi apprendre la programmation ?**

- **Polyvalence** : La programmation est un outil puissant applicable dans presque tous les domaines.
- **Automatisation** : Elle permet d'automatiser des tâches répétitives et d'augmenter l'efficacité.
- **Créativité** : Elle offre la possibilité de créer des solutions innovantes à des problèmes complexes.
- **Emplois** : Les compétences en programmation sont très recherchées sur le marché du travail.

---

## **6. Résumé et questions**

- **Résumé** :
    - La programmation est un outil pour **automatiser**, **calculer** et **modéliser**.
    - Python est un langage **simple** et **puissant** pour les sciences.
    - Les concepts de base : variables, instructions, conditions, boucles.
- **Questions pour les étudiants** :
    - Quel problème dans votre domaine aimeriez-vous automatiser avec un programme ?
    - Pouvez-vous imaginer un exemple où une boucle serait utile en laboratoire ?

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.


