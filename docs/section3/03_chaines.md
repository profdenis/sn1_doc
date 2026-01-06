# **3. Les chaînes de caractères**

Les **chaînes de caractères** (ou *strings*) sont des séquences **immuables** de caractères utilisées pour représenter
du texte. En Python, elles sont délimitées par des guillemets simples (`'`) ou doubles (`"`).

---

## **1. Création et manipulation de base**

### **1.1 Créer une chaîne de caractères**

```python
chaine1 = "Bonjour"  # Avec des guillemets doubles
chaine2 = 'Python'  # Avec des guillemets simples
chaine3 = """Chaîne
multi-ligne"""  # Chaîne multi-ligne (guillemets triples)
```

---

### **1.2 Accéder aux caractères**

Les chaînes sont des **séquences indexées** (comme les listes). L'index commence à `0`.

```python
mot = "Python"
print(mot[0])  # Affiche 'P' (premier caractère)
print(mot[-1])  # Affiche 'n' (dernier caractère)
```

---

### **1.3 Longueur d'une chaîne**

```python
print(len("Python"))  # Affiche 6
```

---

### **1.4 Concatenation et répétition**

```python
# Concatenation
salutation = "Bonjour, " + "monde!"  # "Bonjour, monde!"

# Répétition
echo = "Écho! " * 3  # "Écho! Écho! Écho! "
```

---

## **2. Slicing (découpage)**

Le **slicing** fonctionne comme pour les listes.

```python
mot = "Programmation"

# Extraire une sous-chaîne
print(mot[0:4])  # "Prog" (indices 0 à 3)
print(mot[:7])  # "Program" (du début à l'index 6)
print(mot[7:])  # "mation" (de l'index 7 à la fin)
print(mot[::2])  # "Pormtion" (un caractère sur deux)
print(mot[::-1])  # "noitammargorP" (inverse la chaîne)
```

---

## **3. Méthodes essentielles pour les chaînes**

| **Méthode**                     | **Description**                                                        | **Exemple**                       | **Résultat**              |
|---------------------------------|------------------------------------------------------------------------|-----------------------------------|---------------------------|
| `str.upper()`                   | Convertit en majuscules.                                               | `"python".upper()`                | `"PYTHON"`                |
| `str.lower()`                   | Convertit en minuscules.                                               | `"PYTHON".lower()`                | `"python"`                |
| `str.capitalize()`              | Met la première lettre en majuscule.                                   | `"python".capitalize()`           | `"Python"`                |
| `str.title()`                   | Met la première lettre de chaque mot en majuscule.                     | `"bonjour tout le monde".title()` | `"Bonjour Tout Le Monde"` |
| `str.strip()`                   | Supprime les espaces au début et à la fin.                             | `"  Python  ".strip()`            | `"Python"`                |
| `str.lstrip()` / `str.rstrip()` | Supprime les espaces à gauche/droite.                                  | `"  Python  ".lstrip()`           | `"Python  "`              |
| `str.replace(old, new)`         | Remplace une sous-chaîne par une autre.                                | `"Python".replace("P", "J")`      | `"Jython"`                |
| `str.split(sep)`                | Divise la chaîne en une liste selon un séparateur.                     | `"1,2,3".split(",")`              | `["1", "2", "3"]`         |
| `str.join(iterable)`            | Concatène les éléments d'un itérable avec la chaîne comme séparateur.  | `",".join(["a", "b", "c"])`       | `"a,b,c"`                 |
| `str.find(sub)`                 | Trouve l'index de la première occurrence de `sub` (-1 si introuvable). | `"Python".find("th")`             | `2`                       |
| `str.count(sub)`                | Compte le nombre d'occurrences de `sub`.                               | `"banana".count("a")`             | `3`                       |
| `str.startswith(prefix)`        | Vérifie si la chaîne commence par `prefix`.                            | `"Python".startswith("Py")`       | `True`                    |
| `str.endswith(suffix)`          | Vérifie si la chaîne se termine par `suffix`.                          | `"Python".endswith("on")`         | `True`                    |
| `str.isdigit()`                 | Vérifie si tous les caractères sont des chiffres.                      | `"123".isdigit()`                 | `True`                    |
| `str.isalpha()`                 | Vérifie si tous les caractères sont des lettres.                       | `"Python".isalpha()`              | `True`                    |

---

### **Exemples d'utilisation des méthodes**

```python
texte = "   bonjour tout le monde   "

# Nettoyage et formatage
texte_nettoye = texte.strip().capitalize()
print(texte_nettoye)  # "Bonjour tout le monde"

# Remplacement
texte_modifie = texte.replace("bonjour", "salut")
print(texte_modifie)  # "salut tout le monde"

# Division et jointure
mots = texte.strip().split()
texte_reconstitue = " ".join(mots)
print(texte_reconstitue)  # "bonjour tout le monde"
```

---

## **4. Boucles et chaînes de caractères**

### **4.1 Parcourir une chaîne avec une boucle**

```python
mot = "Python"
for lettre in mot:
    print(lettre)
# Affiche chaque lettre sur une nouvelle ligne
```

---

### **4.2 Compter les voyelles**

```python
mot = "Programmation"
voyelles = "aeiouyAEIOUY"
compte = 0

for lettre in mot:
    if lettre in voyelles:
        compte += 1

print(f"Nombre de voyelles : {compte}")  # Affiche 5
```

---

## **5. Chaînes et validation**

### **5.1 Vérifier si une chaîne est un nombre**

```python
def est_nombre(chaine):
    return chaine.isdigit() or (chaine.startswith("-") and chaine[1:].isdigit())


print(est_nombre("123"))  # True
print(est_nombre("-456"))  # True
print(est_nombre("12.34"))  # False
```

---

### **5.2 Valider une adresse e-mail (simplifiée)**

```python
def est_email_valide(email):
    return "@" in email and "." in email.split("@")[-1]


print(est_email_valide("alice@example.com"))  # True
print(est_email_valide("mauvais.email"))  # False
```

---

## **6. Chaînes et conversions**

### **6.1 Convertir une chaîne en nombre**

```python
nombre_str = "123"
nombre_int = int(nombre_str)  # Conversion en entier
nombre_float = float(nombre_str)  # Conversion en flottant
```

---

### **6.2 Convertir un nombre en chaîne**

```python
nombre = 123
chaine = str(nombre)  # "123"
```

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
