Voici les **corrigés détaillés** pour les 20 exercices combinant les chaînes de caractères avec les listes, boucles, conditionnelles et fonctions, sans utiliser NumPy.

---

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

### **Exercice 4 : Majuscules alternées**
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
    return " ".join([f"{mot[0]}." for mot in mots])

print(initiales("Denis Rinfret"))  # "D. R."
```

---

### **Exercice 7 : Valider un code postal**
```python
import re

def est_code_postal_valide(code):
    return bool(re.match(r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$', code))

print(est_code_postal_valide("H3T 1J4"))  # True
print(est_code_postal_valide("H3T1J4"))   # False
```

---

### **Exercice 8 : Extraire les nombres d'une chaîne**
```python
import re

def extraire_nombres(chaine):
    return [int(nombre) for nombre in re.findall(r'\d+', chaine)]

print(extraire_nombres("Il a 3 pommes et 5 bananes."))  # [3, 5]
```

---

## **Exercices combinant chaînes et listes**

### **Exercice 9 : Convertir une chaîne en liste de mots**
```python
def chaine_en_liste(chaine):
    return chaine.split()

print(chaine_en_liste("Bonjour tout le monde"))  # ["Bonjour", "tout", "le", "monde"]
```

---

### **Exercice 10 : Trouver les mots les plus longs**
```python
def mots_les_plus_long(mots):
    if not mots:
        return []

    longueur_max = max(len(mot) for mot in mots)
    return [mot for mot in mots if len(mot) == longueur_max]

print(mots_les_plus_long(["pomme", "banane", "cerise", "ananas"]))  # ["banane", "ananas"]
```

---

### **Exercice 11 : Compter les voyelles dans une liste de mots**
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

### **Exercice 12 : Inverser l'ordre des mots**
```python
def inverser_mots(chaine):
    mots = chaine.split()
    return " ".join(reversed(mots))

print(inverser_mots("Bonjour tout le monde"))  # "monde le tout Bonjour"
```

---

### **Exercice 13 : Filtrer les mots commençant par une lettre**
```python
def filtrer_mots(mots, lettre):
    return [mot for mot in mots if mot.startswith(lettre)]

print(filtrer_mots(["pomme", "banane", "poire", "cerise"], "p"))  # ["pomme", "poire"]
```

---

## **Exercices combinant chaînes et boucles/conditionnelles**

### **Exercice 14 : Valider un mot de passe**
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

### **Exercice 15 : Remplacer les voyelles par un caractère**
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

### **Exercice 16 : Compter les occurrences de chaque lettre**
```python
def compter_occurrences(chaine):
    chaine = chaine.lower().replace(" ", "")
    occurrences = {}
    for lettre in chaine:
        if lettre in occurrences:
            occurrences[lettre] += 1
        else:
            occurrences[lettre] = 1
    return sorted(occurrences.items())

print(compter_occurrences("Bonjour"))  # [('b', 1), ('j', 1), ('n', 1), ('o', 2), ('r', 1), ('u', 1)]
```

---

### **Exercice 17 : Trouver les anagrammes**
```python
def trouver_anagrammes(mots):
    groupes = {}
    for mot in mots:
        cle = "".join(sorted(mot.lower()))
        if cle in groupes:
            groupes[cle].append(mot)
        else:
            groupes[cle] = [mot]
    return list(groupes.values())

print(trouver_anagrammes(["écoute", "couteau", "tac", "cat", "acte"]))
# [['écoute'], ['couteau'], ['tac', 'cat'], ['acte']]
```

---

## **Exercices combinant chaînes et fonctions**

### **Exercice 18 : Fonction de césar**
```python
def cesar(chaine, decalage):
    resultat = []
    for lettre in chaine:
        if lettre.isalpha():
            base = ord('A') if lettre.isupper() else ord('a')
            nouvelle_lettre = chr((ord(lettre) - base + decalage) % 26 + base)
            resultat.append(nouvelle_lettre)
        else:
            resultat.append(lettre)
    return "".join(resultat)

print(cesar("Bonjour", 3))  # "Erqmrxu"
```

---

### **Exercice 19 : Fonction de capitalisation personnalisée**
```python
def capitaliser(chaine, exclus):
    mots = chaine.split()
    resultat = []
    for mot in mots:
        if mot.lower() in [e.lower() for e in exclus]:
            resultat.append(mot.lower())
        else:
            resultat.append(mot.capitalize())
    return " ".join(resultat)

print(capitaliser("bonjour tout le monde", ["le"]))  # "Bonjour Tout le Monde"
```

---

### **Exercice 20 : Fonction de troncature**
```python
def tronquer(chaine, longueur):
    if len(chaine) <= longueur:
        return chaine
    return chaine[:longueur] + "..."

print(tronquer("Bonjour tout le monde", 10))  # "Bonjour..."
```

---


