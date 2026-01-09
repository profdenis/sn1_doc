# **Corrigés : Chaînes de caractères et notions précédentes**

---

## **Exercices de base**

### **Exercice 1 : Inverser une chaîne**
```python
def inverser(chaine):
    return chaine[::-1]

print(inverser("Python"))  # "nohtyP"
```

---

### **Exercice 2 : Compter les mots**
```python
def compter_mots(chaine):
    return len(chaine.split())

print(compter_mots("Bonjour tout le monde"))  # 4
```

---

### **Exercice 3 : Palindrome**
```python
def est_palindrome(chaine):
    return chaine == chaine[::-1]

print(est_palindrome("radar"))  # True
print(est_palindrome("python"))  # False
```

---

### :material-checkbox-blank-outline: **Exercice 4 : Majuscules alternées**
```python
def majuscules_alternées(chaine):
    resultat = []
    for i, lettre in enumerate(chaine):
        if i % 2 == 0:
            resultat.append(lettre.lower())
        else:
            resultat.append(lettre.upper())
    return "".join(resultat)

print(majuscules_alternées("python"))  # "pYtHoN"
```

---

### **Exercice 5 : Censure de mots**
```python
def censurer(texte, mot_interdit):
    return texte.replace(mot_interdit, "*" * len(mot_interdit))

print(censurer("Ce mot est interdit.", "interdit"))  # "Ce mot est ********""
```

---

### **Exercice 6 : Initiales**
```python
def initiales(nom_complet):
    mots = nom_complet.split()
    resultat = ""

    for mot in mots:
        # On ajoute la première lettre, un point et un espace
        resultat += mot[0] + ". "

    # On retire l'espace final superflu avec .strip()
    return resultat.strip()

print(initiales("Jean Tremblay"))  # "J. T."
```

---



## **Exercices combinant chaînes et listes**

### **Exercice 7 : Convertir une chaîne en liste de mots**
```python
def chaine_en_liste(chaine):
    return chaine.split()

print(chaine_en_liste("Bonjour tout le monde"))  # ["Bonjour", "tout", "le", "monde"]
```

---

### :material-checkbox-blank-outline: **Exercice 8 : Trouver les mots les plus longs**
```python
def mots_les_plus_long(mots):
    if not mots:
        return []

    # 1. Trouver la longueur maximale
    longueur_max = 0
    for mot in mots:
        if len(mot) > longueur_max:
            longueur_max = len(mot)

    # 2. Filtrer les mots qui ont cette longueur
    resultat = []
    for mot in mots:
        if len(mot) == longueur_max:
            resultat.append(mot)

    return resultat

print(mots_les_plus_long(["pomme", "banane", "cerise", "ananas"]))  # ["banane", "ananas"]```
```

---

### **Exercice 9 : Compter les voyelles dans une liste de mots**
```python
def compter_voyelles_liste(mots):
    voyelles = "aeiouyAEIOUY"
    compte = 0
    for mot in mots:
        for lettre in mot:
            if lettre in voyelles:
                compte += 1
    return compte

print(compter_voyelles_liste(["pomme", "banane", "kiwi"]))  # 7
```

---

### **Exercice 10 : Inverser l'ordre des mots**
```python
def inverser_mots(chaine):
    mots = chaine.split()
    return " ".join(mots[::-1])

print(inverser_mots("Bonjour tout le monde"))  # "monde le tout Bonjour"
```

---

### **Exercice 11 : Filtrer les mots commençant par une lettre**
```python
def filtrer_mots(mots, lettre):
    return [mot for mot in mots if mot.startswith(lettre)]

print(filtrer_mots(["pomme", "banane", "poire", "cerise"], "p"))  # ["pomme", "poire"]
```

---

## **Exercices combinant chaînes et boucles/conditionnelles**

### :material-checkbox-blank-outline: **Exercice 12 : Valider un mot de passe**
```python
def est_mot_de_passe_valide(mot_de_passe):
    if len(mot_de_passe) < 8:
        return False
    if not any(c.isupper() for c in mot_de_passe):
        return False
    if not any(c.isdigit() for c in mot_de_passe):
        return False
    return True

print(est_mot_de_passe_valide("MotDePasse123"))  # True
print(est_mot_de_passe_valide("motdepasse"))      # False
```

---

### **Exercice 13 : Remplacer les voyelles par un caractère**
```python
def remplacer_voyelles(chaine, caractere):
    voyelles = "aeiouyAEIOUY"
    resultat = []
    for lettre in chaine:
        if lettre in voyelles:
            resultat.append(caractere)
        else:
            resultat.append(lettre)
    return "".join(resultat)

print(remplacer_voyelles("Bonjour", "*"))  # "B*nj**r"
```

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
