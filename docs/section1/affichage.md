# **1. Affichage sur la sortie standard**

---

## **1. La sortie standard**

**Concept général**

La **sortie standard** (ou *standard output*, souvent abrégée **stdout**) est un mécanisme utilisé par les programmes
pour afficher des informations à l’utilisateur. Dans la plupart des systèmes, la sortie standard est généralement
associée à l’écran (le terminal ou la console).

### **Caractéristiques principales**

- **Destination par défaut** : Affiche le texte dans le terminal ou la console.
- **Utilisation universelle** : Tous les langages de programmation offrent un moyen d’écrire sur la sortie standard (
  ex. : `printf` en C, `console.log` en JavaScript, `print` en Python).
- **Redirection possible** : La sortie standard peut être redirigée vers un fichier ou un autre programme (ex. :
  `mon_programme > sortie.txt` dans un terminal).

### **Exemple d’utilisation dans différents langages**

| Langage    | Instruction pour afficher "Bonjour" |
|------------|-------------------------------------|
| C          | `printf("Bonjour\n");`              |
| Java       | `System.out.println("Bonjour");`    |
| JavaScript | `console.log("Bonjour");`           |
| Python     | `print("Bonjour")`                  |

---

## **2. La fonction `print` en Python**

**Syntaxe et utilisation de base**

En Python, la fonction `print()` est utilisée pour afficher des données sur la sortie standard. Elle peut prendre un ou
plusieurs arguments, qu’elle affichera séparés par un espace par défaut.

### **Syntaxe**

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

- **`objects`** : Les valeurs à afficher (peuvent être de n’importe quel type : chaînes, nombres, listes, etc.).
- **`sep`** (optionnel) : Chaîne utilisée pour séparer les objets. Par défaut : `' '` (un espace).
- **`end`** (optionnel) : Chaîne ajoutée à la fin de la sortie. Par défaut : `'\n'` (un saut de ligne).
- **`file`** (optionnel) : Destination de la sortie (par défaut : `sys.stdout`).
- **`flush`** (optionnel) : Si `True`, force l’affichage immédiat (utile pour les sorties en temps réel).

---

### **Exemples d’utilisation**

#### **2.1 Affichage simple**

```python
print("Bonjour, monde!")
# Affiche : Bonjour, monde!
```

#### **2.2 Affichage de plusieurs valeurs**

```python
print("La valeur de pi est environ", 3.14159)
# Affiche : La valeur de pi est environ 3.14159
```

#### **2.3 Utilisation du paramètre `sep`**

```python
print("Python", "est", "génial", sep="-")
# Affiche : Python-est-génial
```

#### **2.4 Utilisation du paramètre `end`**

```python
print("Première ligne", end=" ")
print("Deuxième ligne")
# Affiche : Première ligne Deuxième ligne
```

#### **2.5 Combinaison de `sep` et `end`**

```python
print("Valeurs :", 1, 2, 3, sep=", ", end=".\n")
# Affiche : Valeurs : 1, 2, 3.
```

#### **2.6 Affichage sans saut de ligne**

```python
print("Chargement", end="")
print(".", end="")
print(".", end="")
print(".")
# Affiche : Chargement...
```

---

Voici la section à ajouter avant la partie sur les **f-strings**, pour offrir une comparaison complète des méthodes de
formatage en Python.

---

## **3. La méthode `.format()` en Python**

**Formatage de chaînes avec `.format()`**

Avant l’introduction des f-strings (Python 3.6), la méthode `.format()` était la manière la plus courante de formater
des chaînes de caractères en Python. Elle permet d’insérer des valeurs dans une chaîne en utilisant des **placeholders
** (marqueurs de position) `{}`.

### **Syntaxe**

```python
"texte {} texte".format(valeur1, valeur2, ...)
```

- Les `{}` sont remplacés par les valeurs passées à `.format()`, dans l’ordre.
- On peut aussi utiliser des **indices** ou des **noms** pour identifier les placeholders.

---

### **Exemples d’utilisation**

#### **3.1 Placeholders simples**

```python
print("Bonjour, {} !".format("Alice"))
# Affiche : Bonjour, Alice !
```

#### **3.2 Plusieurs valeurs**

```python
print("{} a {} ans.".format("Alice", 25))
# Affiche : Alice a 25 ans.
```

#### **3.3 Utilisation d’indices**

```python
print("{1} a {0} ans.".format(25, "Alice"))
# Affiche : Alice a 25 ans.
```

#### **3.4 Placeholders nommés**

```python
print("{nom} a {age} ans.".format(nom="Alice", age=25))
# Affiche : Alice a 25 ans.
```

#### **3.5 Formatage des nombres**

```python
prix = 12.3456
print("Prix : {:.2f} $".format(prix))
# Affiche : Prix : 12.35 $
```

#### **3.6 Alignement et remplissage**

```python
mot = "Python"
print("{:*^10}".format(mot))
# Affiche : **Python** (centré avec des * autour)
```

#### **3.7 Remplissage avec des dictionnaires**

```python
personne = {"nom": "Alice", "age": 25}
print("{nom} a {age} ans.".format(**personne))
# Affiche : Alice a 25 ans.
```

---

### **Avantages et inconvénients de `.format()`**

| **Avantages**                                    | **Inconvénients**                              |
|--------------------------------------------------|------------------------------------------------|
| Plus lisible que l’ancien formatage avec `%`.    | Moins concis que les f-strings.                |
| Permet des formatages complexes.                 | Légèrement moins performant que les f-strings. |
| Compatible avec toutes les versions de Python 3. | Syntaxe plus verbeuse.                         |

---

### **Comparaison avec les f-strings**

Les f-strings sont généralement préférées aujourd’hui pour leur **simplicité** et leur **performance**, mais `.format()`
reste utile dans certains cas, notamment :

- Pour du code devant être compatible avec des versions de Python antérieures à 3.6.
- Pour des formatages dynamiques où les placeholders sont construits à la volée.

---

**Transition vers les f-strings** :
*"Les f-strings, introduites en Python 3.6, offrent une syntaxe encore plus intuitive et performante pour le formatage
de chaînes. Voyons comment les utiliser..."*

## **4. Les f-strings en Python**

**Chaînes de caractères formatées**

Les **f-strings** (ou *formatted string literals*) sont une syntaxe introduite en Python 3.6 pour faciliter le formatage
des chaînes de caractères. Elles permettent d’insérer directement des expressions Python dans une chaîne, entre
accolades `{}` précédées du préfixe `f`.

### **Syntaxe**

```python
f"texte {expression} texte"
```

- Les expressions entre `{}` sont évaluées et converties en chaînes de caractères.
- Les f-strings sont **plus rapides** et **plus lisibles** que les méthodes traditionnelles comme `.format()` ou `%`.

---

### **Exemples d’utilisation**

#### **4.1 Insertion de variables**

```python
nom = "Alice"
age = 25
print(f"{nom} a {age} ans.")
# Affiche : Alice a 25 ans.
```

#### **4.2 Calculs dans les f-strings**

```python
rayon = 5
print(f"L'aire d'un cercle de rayon {rayon} est {3.14159 * rayon ** 2:.2f}.")
# Affiche : L'aire d'un cercle de rayon 5 est 78.54.
```

#### **4.3 Formatage des nombres**

```python
prix = 12.3456
print(f"Prix : {prix:.2f} $")
# Affiche : Prix : 12.35 $
```

#### **4.4 Expressions conditionnelles**

```python
note = 15
print(f"Résultat : {'Réussi' if note >= 10 else 'Échoué'}")
# Affiche : Résultat : Réussi
```

#### **4.5 Appels de fonctions**

```python
def carre(x):
    return x ** 2


nombre = 4
print(f"Le carré de {nombre} est {carre(nombre)}.")
# Affiche : Le carré de 4 est 16.
```

#### **4.6 Alignement et remplissage**

```python
mot = "Python"
print(f"{mot:*^10}")
# Affiche : **Python** (centré avec des * autour)
```

---

### **Avantages des f-strings**

- **Lisibilité** : Le code est plus clair et plus concis.
- **Performance** : Les f-strings sont plus rapides que les autres méthodes de formatage.
- **Flexibilité** : Permet d’insérer n’importe quelle expression Python valide.

---

## **5. Tableau récapitulatif : `.format()` vs. f-strings**

Comparaison entre `.format()` et les f-strings

| **Critère**             | **`.format()`**                                   | **f-strings**                                      |
|-------------------------|---------------------------------------------------|----------------------------------------------------|
| **Syntaxe**             | `"texte {} texte".format(valeur)`                 | `f"texte {expression} texte"`                      |
| **Lisibilité**          | Bonne, mais plus verbeuse.                        | Excellente, plus concise et intuitive.             |
| **Performance**         | Légèrement moins rapide.                          | Plus rapide (optimisée par Python).                |
| **Compatibilité**       | Fonctionne avec toutes les versions de Python 3.  | Disponible à partir de Python 3.6.                 |
| **Expressions**         | Nécessite `.format()` après la chaîne.            | Permet d’insérer n’importe quelle expression.      |
| **Placeholders**        | Utilise `{}` avec indices ou noms.                | Utilise `{expression}` directement.                |
| **Formatage complexe**  | Supporte bien les formats avancés (ex. : `:.2f`). | Supporte aussi les formats avancés.                |
| **Exemple simple**      | `"Bonjour, {} !".format("Alice")`                 | `f"Bonjour, {"Alice"} !"` ou `f"Bonjour, {nom} !"` |
| **Exemple avec calcul** | `"Le carré de {} est {}.".format(5, 5**2)`        | `f"Le carré de {5} est {5**2}."`                   |
| **Exemple avec format** | `"Prix : {:.2f} $".format(12.3456)`               | `f"Prix : {12.3456:.2f} $"`                        |

---

### **Quand utiliser l’un ou l’autre ?**

- **Utilise `.format()` si** :
    - Tu travailles avec une version de Python antérieure à 3.6.
    - Tu as besoin de construire dynamiquement les placeholders (ex. : avec des boucles).

- **Utilise les f-strings si** :
    - Tu utilises Python 3.6 ou une version plus récente.
    - Tu veux un code plus lisible et concis.
    - Tu as besoin de performances optimales (ex. : dans des boucles ou des calculs intensifs).

---

**Exemple comparatif complet** :

```python
# Avec .format()
nom = "Alice"
age = 25
print("{} a {} ans.".format(nom, age))

# Avec f-strings
print(f"{nom} a {age} ans.")
```

---
