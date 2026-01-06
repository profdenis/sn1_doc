# **Corrigés 2 : Utilisation de l'entrée standard**

---

## **Exercices de base**

### **Exercice 1 : Lecture et affichage simple**

```python
prenom = input("Entrez votre prénom : ")
nom = input("Entrez votre nom : ")
print(f"Bonjour {prenom} {nom}, bienvenue !")
```

---

### **Exercice 2 : Calcul de surface**

```python
longueur = float(input("Entrez la longueur du rectangle (en mètres) : "))
largeur = float(input("Entrez la largeur du rectangle (en mètres) : "))
surface = longueur * largeur
print(f"La surface du rectangle est {surface:.2f} m².")
```

---

### **Exercice 3 : Conversion de température**

```python
celsius = float(input("Entrez la température en degrés Celsius : "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius}°C correspond à {fahrenheit:.1f}°F.")
```

---

### **Exercice 4 : Calcul de moyenne**

```python
note1 = float(input("Entrez la première note : "))
note2 = float(input("Entrez la deuxième note : "))
note3 = float(input("Entrez la troisième note : "))
moyenne = (note1 + note2 + note3) / 3
print(f"La moyenne est {round(moyenne, 2)} (arrondie) ou {moyenne:.2f} (formatée).")
```

---

### **Exercice 5 : Prix total**

```python
prix_unitaire = float(input("Entrez le prix unitaire de l'article (en dollars) : "))
quantite = int(input("Entrez la quantité achetée : "))
total = prix_unitaire * quantite
print(f"Le prix total est {total:.2f} $.")
```

---

---

## **Exercices intermédiaires**

### **Exercice 6 : Conversion de devises**

```python
montant_eur = float(input("Entrez le montant en euros : "))
taux_change = float(input("Entrez le taux de change (1 EUR = ? USD) : "))
montant_usd = montant_eur * taux_change
print(f"{montant_eur} EUR équivaut à {montant_usd:.2f} USD.")
```

---

### **Exercice 7 : Calcul d’IMC**

```python
poids = float(input("Entrez votre poids (en kg) : "))
taille = float(input("Entrez votre taille (en mètres) : "))
imc = poids / (taille ** 2)
print(f"Votre IMC est {imc:.1f}.")
```

---

### **Exercice 8 : Calcul de périmètre**

```python
rayon = float(input("Entrez le rayon du cercle (en mètres) : "))
perimetre = 2 * 3.1416 * rayon
print(f"Le périmètre du cercle est {perimetre:.2f} mètres.")
```

---

### **Exercice 9 : Gestion de temps**

```python
minutes = int(input("Entrez un nombre de minutes : "))
heures = minutes // 60
restantes = minutes % 60
print(f"{minutes} minutes équivaut à {heures}h{restantes:02d}.")
```

---

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.