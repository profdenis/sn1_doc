---
icon: material/checkbox-outline
---

# 4. **Exécution de code Python**

---

## **1. La console Python (REPL)**

### **1.1 Qu'est-ce que la console Python (REPL) ?**

- **REPL** signifie **Read-Eval-Print Loop** (Boucle de lecture-évaluation-affichage).
- C'est un environnement interactif où vous pouvez entrer des commandes Python une par une et voir immédiatement le
  résultat.
- Idéal pour **tester rapidement** des expressions, des fonctions, ou des morceaux de code.

---

### **1.2 Démarrer la console Python**

#### :material-checkbox-blank-outline: **Sur Windows :**

1. Ouvrez le menu **Démarrer**.
2. Tapez `cmd` pour ouvrir l'**Invite de commandes**.
3. Tapez `python` ou `python3` et appuyez sur **Entrée**.
    - Si Python est correctement installé, la console Python s'ouvre avec un message comme :
      ```commandline
      Python 3.11.4 (tags/v3.11.4:d234, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
      Type "help", "copyright", "credits" or "license" for more information.
      >>>
      ```

#### :material-checkbox-blank-outline: **Sur macOS :**

1. Ouvrez le **Terminal** (via Spotlight : `Cmd + Espace`, puis tapez `Terminal`).
2. Tapez `python3` et appuyez sur **Entrée**.
    - La console Python s'ouvre avec un message similaire à celui de Windows.

#### **Dans PyCharm :**

1. Ouvrez PyCharm.
2. Allez dans **Tools > Python Console** (ou utilisez le raccourci `Alt + F12`).
    - Une console Python s'ouvre en bas de l'écran.

---

### **1.3 Utilisation de la console Python (REPL)**

- **Entrer des commandes** : Tapez directement du code Python après le symbole `>>>`, puis appuyez sur **Entrée** pour
  l'exécuter.
  ```commandline
  >>> print("Bonjour, monde !")
  Bonjour, monde !
  ```
- **Quitter la console** : Tapez `exit()` ou `quit()` et appuyez sur **Entrée**, ou utilisez `Ctrl + D` (macOS/Linux) ou
  `Ctrl + Z` (Windows).

---

### **1.4 Exemples d'utilisation du REPL**

- **Calculs simples** :
  ```commandline
  >>> 5 + 3
  8
  ```
- **Définir une variable** :
  ```commandline
  >>> x = 10
  >>> x * 2
  20
  ```
- **Tester une fonction** :
  ```commandline
  >>> def carre(n):
  ...     return n ** 2
  ...
  >>> carre(4)
  16
  ```

---

## **2. Fichiers Python (.py)**

### **2.1 Qu'est-ce qu'un fichier Python ?**

- Un fichier Python est un fichier texte contenant du code Python.
- Il a l'**extension `.py`** (ex. : `mon_programme.py`).
- Permet d'écrire des programmes plus longs et de les réutiliser.

---

### **2.2 Créer un fichier Python**

- **Avec un éditeur de texte** (ex. : Notepad++, VS Code, Sublime Text) :
    1. Créez un nouveau fichier.
    2. Enregistrez-le avec l'extension `.py` (ex. : `mon_programme.py`).
- **Dans PyCharm** :
    1. Créez un nouveau projet (`File > New Project`).
    2. Ajoutez un fichier Python (`File > New > Python File`).

---

###  :material-checkbox-blank-outline: **2.3 Exécuter un fichier Python dans le terminal**

#### **Sur Windows :**

1. Ouvrez l'**Invite de commandes**.
2. Naviguez jusqu'au dossier contenant votre fichier avec `cd` (ex. : `cd C:\mon_dossier`).
3. Exécutez le fichier avec la commande :
   ```bash
   python mon_programme.py
   ```
   ou
   ```bash
   python3 mon_programme.py
   ```

#### **Sur macOS :**

1. Ouvrez le **Terminal**.
2. Naviguez jusqu'au dossier contenant votre fichier avec `cd` (ex. : `cd ~/mon_dossier`).
3. Exécutez le fichier avec la commande :
   ```bash
   python3 mon_programme.py
   ```

---

### **2.4 Exécuter un fichier Python dans PyCharm**

1. Ouvrez votre fichier `.py` dans PyCharm.
2. Cliquez sur le bouton **▶️ (Run)** en haut à droite, ou utilisez le raccourci `Shift + F10`.
3. Le résultat s'affiche dans la **console d'exécution** en bas de l'écran.

---

### **2.5 Exemple de fichier Python**

Créez un fichier `bonjour.py` avec le contenu suivant :

```python
print("Bonjour, monde !")
nom = input("Quel est votre nom ? ")
print(f"Bonjour, {nom} !")
```

#### **Exécution dans le terminal :**

```bash
python3 bonjour.py
```

**Sortie possible :**

```
Bonjour, monde !
Quel est votre nom ? Alice
Bonjour, Alice !
```

#### **Exécution dans PyCharm :**

1. Ouvrez `bonjour.py` dans PyCharm.
2. Cliquez sur **▶️ (Run)** ou appuyez sur `Shift + F10`.
3. Le programme s'exécute dans la console intégrée.

---

## **3. Résumé des commandes utiles**

| **Action**                 | **Terminal (Windows/macOS)**      | **PyCharm**                          |
|----------------------------|-----------------------------------|--------------------------------------|
| Démarrer la console Python | `python` ou `python3`             | `Tools > Python Console`             |
| Quitter la console Python  | `exit()` ou `Ctrl + D`/`Ctrl + Z` | Fermer l'onglet de la console        |
| Exécuter un fichier `.py`  | `python3 mon_programme.py`        | Bouton **▶️ (Run)** ou `Shift + F10` |

---

## **4. Bonnes pratiques**

- **Utilisez la console Python (REPL)** pour tester rapidement des idées ou des morceaux de code.
- **Utilisez des fichiers `.py`** pour écrire des programmes complets ou des scripts réutilisables.
- **PyCharm** offre une interface conviviale pour écrire, exécuter et déboguer du code Python.

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
