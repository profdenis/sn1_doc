# **L'instruction `match`**

---

## **1. Introduction à `match`**

L'instruction **`match`** est une fonctionnalité introduite dans **Python 3.10** pour simplifier les comparaisons
multiples. Elle est inspirée du **pattern matching** présent dans d'autres langages comme Rust ou Scala.

- **Avantage** : Remplace avantageusement les longues séquences `if...elif...else` pour des comparaisons de valeurs
  discrètes.
- **Utilisation** : Permet de comparer une valeur à plusieurs motifs (*patterns*) et d'exécuter le bloc de code
  correspondant au motif qui correspond.

---

## **2. Syntaxe de base de `match`**

```
match variable:
    case motif1:
        # Instructions si variable correspond à motif1
    case motif2:
        # Instructions si variable correspond à motif2
    case _:
        # Instructions si aucun motif ne correspond (équivalent à `else`)
```

- **`case`** : Définit un motif à comparer.
- **`_`** : Motif générique qui correspond à toute valeur (équivalent au `else` dans une structure `if...elif...else`).

---

## **3. Exemple simple : Comparaison avec `if...elif...else`**

### **3.1 Avec `if...elif...else`**

```python
note = 85
if note >= 90:
    print("Très bien !")
elif note >= 80:
    print("Bien.")
elif note >= 70:
    print("Assez bien.")
elif note >= 60:
    print("Passable.")
else:
    print("Insuffisant.")
```

**Sortie** :

```
Bien.
```

---

### **3.2 Avec `match`**

```python
note = 85

match note:
    case n if n >= 90:
        print("Très bien !")
    case n if n >= 80:
        print("Bien.")
    case n if n >= 70:
        print("Assez bien.")
    case n if n >= 60:
        print("Passable.")
    case _:
        print("Insuffisant.")
```

**Sortie** :

```
Bien.
```

---

### **3.3 Comparaison des deux approches**

| **Critère**     | **`if...elif...else`**                              | **`match`**                                              |
|-----------------|-----------------------------------------------------|----------------------------------------------------------|
| **Lisibilité**  | Peut devenir verbeux pour de nombreuses conditions. | Plus clair et structuré pour des comparaisons multiples. |
| **Flexibilité** | Permet des conditions complexes.                    | Idéal pour des comparaisons de valeurs discrètes.        |
| **Performance** | Aucune différence significative.                    | Aucune différence significative.                         |

---

## **4. Exemples avancés de `match`**

### **4.1 Correspondance de valeurs littérales**

```python
jour = "samedi"

match jour:
    case "lundi":
        print("Première journée de travail.")
    case "vendredi":
        print("Dernière journée de travail.")
    case "samedi" | "dimanche":
        print("Fin de semaine !")
    case _:
        print("Milieu de la semaine.")
```

**Sortie** :

```
Fin de semaine !
```

---

### **4.2 Correspondance avec des types**

```python
def traiter_valeur(valeur):
    match valeur:
        case int():
            print("C'est un entier.")
        case float():
            print("C'est un flottant.")
        case str():
            print("C'est une chaîne de caractères.")
        case _:
            print("Type non reconnu.")


traiter_valeur(42)
traiter_valeur(3.14)
traiter_valeur("Bonjour")
```

**Sortie** :

```
C'est un entier.
C'est un flottant.
C'est une chaîne de caractères.
```

---

### **4.3 Correspondance avec des structures de données**

```python
def traiter_liste(liste):
    match liste:
        case []:
            print("La liste est vide.")
        case [x]:
            print(f"La liste contient un seul élément : {x}.")
        case [x, y]:
            print(f"La liste contient deux éléments : {x} et {y}.")
        case _:
            print("La liste contient plus de deux éléments.")


traiter_liste([])
traiter_liste([1])
traiter_liste([1, 2])
traiter_liste([1, 2, 3])
```

**Sortie** :

```
La liste est vide.
La liste contient un seul élément : 1.
La liste contient deux éléments : 1 et 2.
La liste contient plus de deux éléments.
```

---

### **4.4 Correspondance avec des dictionnaires**

```python
def traiter_dictionnaire(dico):
    match dico:
        case {"nom": nom, "âge": age}:
            print(f"Nom : {nom}, Âge : {age}.")
        case {"nom": nom}:
            print(f"Nom : {nom}, Âge non spécifié.")
        case _:
            print("Format de dictionnaire non reconnu.")


traiter_dictionnaire({"nom": "Alice", "âge": 30})
traiter_dictionnaire({"nom": "Bob"})
traiter_dictionnaire({"ville": "Paris"})
```

**Sortie** :

```
Nom : Alice, Âge : 30.
Nom : Bob, Âge non spécifié.
Format de dictionnaire non reconnu.
```

---

## **5. Cas d'utilisation recommandés**

- **Comparaisons de valeurs discrètes** : `match` est idéal pour comparer une variable à plusieurs valeurs possibles.
- **Filtrage de types** : Utile pour vérifier le type d'une variable et agir en conséquence.
- **Décomposition de structures de données** : Permet de décomposer des listes, dictionnaires, ou objets de manière
  élégante.

---

## **6. Limites de `match`**

- **Pas adapté pour des plages de valeurs** : Pour des comparaisons de plages (ex. : `if 10 <= x < 20`),
  `if...elif...else` reste plus adapté.
- **Moins flexible pour des conditions complexes** : `match` est conçu pour des comparaisons de motifs, pas pour des
  expressions booléennes complexes.

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
