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

#### **2.5 Affichage sans saut de ligne**

```python
print("Chargement", end="")
print(".", end="")
print(".", end="")
print(".")
# Affiche : Chargement...
```

#### **2.6 Combinaison de `sep` et `end`**

```python
print("Valeurs : ", end="")
print(1, 2, 3, sep=", ", end=".\n")
# Affiche : Valeurs : 1, 2, 3.
```

---

## **3. La méthode `.format()` en Python**

**Formatage de chaînes avec `.format()`**

Avant l’introduction des _f-strings_ (Python 3.6), la méthode `.format()` était la manière la plus courante de formater
des chaînes de caractères en Python. Elle permet d’insérer des valeurs dans une chaîne en utilisant des
**placeholders** (marqueurs de position) `{}`.

### **Syntaxe**

```python
"texte {} texte {} ...".format(valeur1, valeur2, ...)
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
| Plus lisible que l’ancien formatage avec `%`.    | Moins concis que les _f-strings_.                |
| Permet des formatages complexes.                 | Légèrement moins performant que les _f-strings_. |
| Compatible avec toutes les versions de Python 3. | Syntaxe plus verbeuse.                         |

!!! note "Note"
    Le formatage avec `%` n'est pas recommandé en Python 3. C'est la raison pourquoi il n'est pas présenté dans ce
    chapitre.

---

### **Comparaison avec les _f-strings_**

Les *f-strings* sont généralement préférées aujourd’hui pour leur **simplicité** et leur **performance**, mais
`.format()` reste utile dans certains cas, notamment :

- Pour du code devant être compatible avec des versions de Python antérieures à 3.6.
- Pour des formatages dynamiques où les placeholders sont construits à la volée.

---

## **4. Les _f-strings_ en Python**

**Chaînes de caractères formatées**

Les **f-strings** (ou *formatted string literals*) sont une syntaxe introduite en Python 3.6 pour faciliter le formatage
des chaînes de caractères. Elles permettent d’insérer directement des expressions Python, entre accolades `{}`, dans
une chaîne précédée du préfixe `f`.

### **Syntaxe**

```python
f"texte {expression} texte"
```

- Les expressions entre `{}` sont évaluées et converties en chaînes de caractères.
- Les _f-strings_ sont **plus rapides** et **plus lisibles** que les méthodes traditionnelles comme `.format()` ou `%`.

---

### **Exemples d’utilisation**

#### **4.1 Insertion de variables**

```python
nom = "Alice"
age = 25
print(f"{nom} a {age} ans.")
# Affiche : Alice a 25 ans.
```

#### **4.2 Calculs dans les _f-strings_**

```python
rayon = 5
print(f"L'aire d'un cercle de rayon {rayon} est {3.14159 * rayon ** 2:.2f}.")
# Affiche : L'aire d'un cercle de rayon 5 est 78.54.
```

!!! tip "Astuce"
    Quoiqu'il est possible de faire des calculs dans les _f-strings_, comme montré ci-dessus, il est recommandé de les
    utiliser uniquement pour des expressions simples et éviter de les utiliser pour des calculs complexes. Dans
    l'exemple ci-dessus, il serait préférable de placer le résultat du calcul dans une variable et d'utiliser cette
    variable dans la _f-string_.

    ```python
    rayon = 5
    aire = 3.14159 * rayon ** 2
    print(f"L'aire d'un cercle de rayon {rayon} est {aire:.2f}.")
    # Affiche : L'aire d'un cercle de rayon 5 est 78.54.
    ```

#### **4.3 Formatage des nombres**

```python
prix = 12.3456
print(f"Prix : {prix:.2f} $")
# Affiche : Prix : 12.35 $
```

#### **4.4 Appels de fonctions**

```python
def carre(x):
    return x ** 2


nombre = 4
print(f"Le carré de {nombre} est {carre(nombre)}.")
# Affiche : Le carré de 4 est 16.
```

#### **4.5 Alignement et remplissage**

```python
mot = "Python"
print(f"{mot:*^10}")
# Affiche : **Python** (centré avec des * autour)
```

---

### **Avantages des _f-strings_**

- **Lisibilité** : Le code est plus clair et plus concis.
- **Performance** : Les _f-strings_ sont plus rapides que les autres méthodes de formatage.
- **Flexibilité** : Permet d’insérer n’importe quelle expression Python valide.

---

## **5. Tableau récapitulatif : `.format()` vs. _f-strings_**

Comparaison entre `.format()` et les _f-strings_

| **Critère**             | **`.format()`**                                   | **_f-strings_**                                      |
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

- **Utilise les _f-strings_ si** :
    - Tu utilises Python 3.6 ou une version plus récente.
    - Tu veux un code plus lisible et concis.
    - Tu as besoin de performances optimales (ex. : dans des boucles ou des calculs intensifs).

---

**Exemple comparatif** :

```python
# Avec .format()
nom = "Alice"
age = 25
print("{} a {} ans.".format(nom, age))

# Avec f-strings
print(f"{nom} a {age} ans.")
```

---

## **6. : Formatage avancé avec les _f-strings_**

Les **_f-strings_** (chaînes formatées) en Python permettent d'insérer des expressions dans des chaînes de caractères de
manière concise et lisible. Elles offrent également des **options de formatage** puissantes pour contrôler l'affichage
des nombres, chaînes, et autres types de données.

---

### **Tableau récapitulatif des spécificateurs de format**

| **Spécificateur** | **Description**                                                                               | **Exemple**          | **Résultat**   |
|-------------------|-----------------------------------------------------------------------------------------------|----------------------|----------------|
| `:d`              | Format entier (décimal)                                                                       | `f"{123456789:d}"`   | `123456789`    |
| `:f`              | Format flottant (décimal)                                                                     | `f"{3.14159:.2f}"`   | `3.14`         |
| `:e`              | Format scientifique (notation exponentielle)                                                  | `f"{123456789:e}"`   | `1.234568e+08` |
| `:g`              | Format flottant ou scientifique (le plus court)                                               | `f"{123456789:g}"`   | `1.23457e+08`  |
| `:%`              | Format pourcentage (multiplie par 100 et ajoute %)                                            | `f"{0.75:%}"`        | `75.000000%`   |
| `:s`              | Format chaîne de caractères                                                                   | `f"{'Bonjour':s}"`   | `Bonjour`      |
| `:c`              | Format caractère (Unicode)                                                                    | `f"{65:c}"`          | `A`            |
| `:b`              | Format binaire                                                                                | `f"{10:b}"`          | `1010`         |
| `:o`              | Format octal                                                                                  | `f"{10:o}"`          | `12`           |
| `:x`              | Format hexadécimal (minuscules)                                                               | `f"{255:x}"`         | `ff`           |
| `:X`              | Format hexadécimal (majuscules)                                                               | `f"{255:X}"`         | `FF`           |
| `:n`              | Format nombre avec séparateurs de milliers (selon la locale)                                  | `f"{1000000:n}"`     | `1,000,000`    |
| `:>`              | Alignement à droite (par défaut) (`_` pour remplacer les espaces pour bien voir l'alignement) | `f"{'Bonjour':>10}"` | `___Bonjour`   |
| `:<`              | Alignement à gauche                                                                           | `f"{'Bonjour':<10}"` | `Bonjour___`   |
| `:^`              | Alignement centré                                                                             | `f"{'Bonjour':^10}"` | `_Bonjour__`   |
| `:0`              | Remplissage avec des zéros                                                                    | `f"{123:05d}"`       | `00123`        |
| `:.Nf`            | Nombre de décimales pour les flottants (N)                                                    | `f"{3.14159:.2f}"`   | `3.14`         |
| `:,`              | Séparateurs de milliers                                                                       | `f"{1000000:,.2f}"`  | `1,000,000.00` |
| `:+`              | Afficher le signe (positif ou négatif)                                                        | `f"{123:+d}"`        | `+123`         |
| `: `              | Espace pour les positifs, `-` pour les négatifs                                               | `f"{123: d}"`        | ` 123`         |
| `:#`              | Préfixe alternatif (ex. `0b`, `0o`, `0x`)                                                     | `f"{255:#x}"`        | `0xff`         |

---

### **Exemples d'utilisation**

#### **1. Formatage des nombres flottants**

```python
prix = 12.34567
print(f"Prix : {prix:.2f}")  # Affiche "Prix : 12.35"
```

#### **2. Formatage scientifique**

```python
grand_nombre = 123456789
print(f"Scientifique : {grand_nombre:e}")  # Affiche "Scientifique : 1.234568e+08"
```

#### **3. Pourcentages**

```python
taux = 0.756
print(f"Taux de réussite : {taux:.1%}")  # Affiche "Taux de réussite : 75.6%"
```

#### **4. Alignement et remplissage**

```python
mot = "Bonjour"
print(f"'{mot:>15}'")  # Affiche "'         Bonjour'"
print(f"'{mot:*^15}'")  # Affiche "'***Bonjour*****'"
```

#### **5. Nombres binaires, octaux, hexadécimaux**

```python
nombre = 200
print(f"Binaire : {nombre:b}")  # Affiche "Binaire : 11001000"
print(f"Octal : {nombre:o}")  # Affiche "Octal : 310"
print(f"Hexadécimal : {nombre:#x}")  # Affiche "Hexadécimal : 0xc8"
```

#### **6. Séparateurs de milliers**

```python
grand_nombre = 1000000
print(f"Grand nombre : {grand_nombre:,}")  # Affiche "Grand nombre : 1,000,000"
```

#### **7. Affichage des signes**

```python
positif = 123
negatif = -456
print(f"Positif : {positif:+d}")  # Affiche "Positif : +123"
print(f"Négatif : {negatif:d}")  # Affiche "Négatif : -456"
```

---

### **Combinaison de spécificateurs**

Vous pouvez combiner plusieurs spécificateurs pour un formatage avancé :

```python
nombre = 12345.6789
print(f"Format combiné : {nombre:>+15,.2f}")  # Affiche "Format combiné :      +12,345.68"
```

---

### **Cas pratiques**

#### **Affichage monétaire**

```python
prix = 1234.567
print(f"Prix : {prix:,.2f} $")  # Affiche "Prix : 1,234.57 $"
```

#### **Affichage de durées**

```python
secondes = 3661
heures = secondes // 3600
minutes = (secondes % 3600) // 60
secondes_restantes = secondes % 60
print(f"Durée : {heures:02d}:{minutes:02d}:{secondes_restantes:02d}")  # Affiche "Durée : 01:01:01"
```

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
