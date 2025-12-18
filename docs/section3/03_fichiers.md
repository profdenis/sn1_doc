# 3. **Lecture et écriture de fichiers**

---

## **1. Introduction aux fichiers texte**

### **1.1 Chemins de fichiers**
En Python, vous pouvez spécifier le chemin d'un fichier de deux manières :
- **Chemin relatif** : Relatif au répertoire de travail actuel.
  - Exemple : `fichier.txt`, `dossier/fichier.txt`
- **Chemin absolu** : Chemin complet depuis la racine du système de fichiers.
  - Exemple : `/home/utilisateur/fichier.txt` (Linux/Mac) ou `C:\Users\utilisateur\fichier.txt` (Windows).

---

## **2. Ouverture et lecture d'un fichier**

### **2.1 Ouverture d'un fichier sans `with`**
Si vous n'utilisez pas `with`, vous devez **fermer le fichier manuellement** avec `fichier.close()`.

```python
fichier = open("fichier.txt", "r")  # "r" pour le mode lecture
contenu = fichier.read()
print(contenu)
fichier.close()  # Important pour libérer les ressources
```

---

### **2.2 Ouverture d'un fichier avec `with`**
L'instruction `with` **ferme automatiquement le fichier** à la fin du bloc, même si une erreur survient.

```python
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
# Le fichier est automatiquement fermé ici
```

---

### **2.3 Lecture complète d'un fichier**
```python
with open("fichier.txt", "r") as fichier:
    contenu = fichier.read()  # Lit tout le contenu d'un coup
    print(contenu)
```

---

### **2.4 Lecture ligne par ligne**
```python
with open("fichier.txt", "r") as fichier:
    for ligne in fichier:
        print(ligne, end="")  # `end=""` pour éviter les sauts de ligne supplémentaires
```

---

## **3. Lecture d'un fichier avec un float par ligne**

### **3.1 Sans gestion d'erreurs**
```python
with open("nombres.txt", "r") as fichier:
    somme = 0.0
    for ligne in fichier:
        nombre = float(ligne)
        somme += nombre
    print(f"La somme est {somme}.")
```
**Problème** : Si une ligne ne contient pas un nombre valide, le programme plante avec une erreur `ValueError`.

---

### **3.2 Avec gestion complète des erreurs**
```python
with open("nombres.txt", "r") as fichier:
    somme = 0.0
    for ligne in fichier:
        try:
            nombre = float(ligne)
            somme += nombre
        except ValueError:
            print(f"Ligne ignorée : {ligne.strip()} (n'est pas un nombre)")
    print(f"La somme est {somme}.")
```

---

## **4. Fonction qui retourne une liste de nombres**

### **4.1 Fonction `lire_nombres`**
```python
def lire_nombres(nom_fichier):
    nombres = []
    with open(nom_fichier, "r") as fichier:
        for ligne in fichier:
            try:
                nombre = float(ligne)
                nombres.append(nombre)
            except ValueError:
                print(f"Ligne ignorée : {ligne.strip()} (n'est pas un nombre)")
    return nombres

nombres = lire_nombres("nombres.txt")
print(f"Liste des nombres : {nombres}")
print(f"Somme : {sum(nombres)}")
```

---

## **5. Écriture dans un fichier**

### **5.1 Mode `"w"` (écrasement)**
Le mode `"w"` **écrase le contenu existant** du fichier.

```python
with open("sortie.txt", "w") as fichier:
    fichier.write("Première ligne\n")
    fichier.write("Deuxième ligne\n")
```

---

### **5.2 Mode `"a"` (ajout)**
Le mode `"a"` **ajoute** du contenu à la fin du fichier sans écraser le contenu existant.

```python
with open("sortie.txt", "a") as fichier:
    fichier.write("Troisième ligne\n")
    fichier.write("Quatrième ligne\n")
```

---

### **5.3 Écrire une liste de nombres dans un fichier**
```python
nombres = [1.5, 2.5, 3.5, 4.5]
with open("nombres_sortie.txt", "w") as fichier:
    for nombre in nombres:
        fichier.write(f"{nombre}\n")
```

---

## **6. Exemples avec chaînes de caractères**

### **6.1 Lire un fichier de chaînes de caractères**
```python
with open("mots.txt", "r") as fichier:
    for ligne in fichier:
        mot = ligne.strip()  # Supprime les sauts de ligne et espaces
        print(f"Mot lu : {mot}")
```

---

### **6.2 Écrire une liste de chaînes dans un fichier**
```python
mots = ["pomme", "banane", "cerise", "datte"]
with open("mots_sortie.txt", "w") as fichier:
    for mot in mots:
        fichier.write(f"{mot}\n")
```

---

### **6.3 Lire et afficher les lignes d'un fichier de chaînes**
```python
with open("mots.txt", "r") as fichier:
    lignes = fichier.readlines()  # Lit toutes les lignes dans une liste
    for ligne in lignes:
        print(ligne.strip())
```

---
