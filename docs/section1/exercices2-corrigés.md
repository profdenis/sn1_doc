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

### **Exercice 8 : Lecture de plusieurs valeurs en une ligne**

```python
nombres = input("Entrez trois nombres séparés par des espaces : ")
a, b, c = map(int, nombres.split())
somme = a + b + c
print(f"La somme est {somme}.")
```

---

### **Exercice 9 : Calcul de périmètre**

```python
import math

rayon = float(input("Entrez le rayon du cercle (en mètres) : "))
perimetre = 2 * math.pi * rayon
print(f"Le périmètre du cercle est {perimetre:.2f} mètres.")
```

---

### **Exercice 10 : Gestion de temps**

```python
minutes = int(input("Entrez un nombre de minutes : "))
heures = minutes // 60
restantes = minutes % 60
print(f"{minutes} minutes équivaut à {heures}h{restantes:02d}.")
```

---

---

## **Exercices avancés**

### **Exercice 11 : Calcul de factorielle**

```python
n = int(input("Entrez un nombre entier positif : "))
factorielle = 1
for i in range(1, n + 1):
    factorielle *= i
print(f"La factorielle de {n} est {factorielle}.")
```

---

### **Exercice 12 : Lecture et traitement de liste**

```python
nombres_str = input("Entrez 5 nombres séparés par des virgules : ")
nombres = [int(n) for n in nombres_str.split(",")]
somme = sum(nombres)
moyenne = somme / len(nombres)
print(f"Somme : {somme}, Moyenne : {moyenne:.2f}.")
```

---

### **Exercice 13 : Conversion de temps en secondes**

```python
temps = input("Entrez une durée sous la forme HH:MM:SS : ")
heures, minutes, secondes = map(int, temps.split(":"))
total_secondes = heures * 3600 + minutes * 60 + secondes
print(f"{temps} équivaut à {total_secondes} secondes.")
```

---

### **Exercice 14 : Calcul de distance**

```python
vitesse = float(input("Entrez la vitesse (en km/h) : "))
temps = float(input("Entrez le temps (en heures) : "))
distance = vitesse * temps
print(f"La distance parcourue est {distance:.2f} km.")
```

---

### **Exercice 15 : Jeu de devinette**

```python
import random

nombre_a_deviner = random.randint(1, 100)
while True:
    devine = int(input("Devinez le nombre entre 1 et 100 : "))
    if devine < nombre_a_deviner:
        print("Trop petit !")
    elif devine > nombre_a_deviner:
        print("Trop grand !")
    else:
        print(f"Bravo ! Vous avez trouvé {nombre_a_deviner}.")
        break
```

---

---

## **Exercices bonus**

### **Exercice 16 : Calcul de pourcentage**

```python
total = float(input("Entrez le nombre total : "))
partiel = float(input("Entrez le nombre partiel : "))
pourcentage = (partiel / total) * 100
print(f"{partiel} représente {pourcentage:.2f}% de {total}.")
```

---

### **Exercice 17 : Lecture et validation**

```python
while True:
    nombre = int(input("Entrez un nombre entre 1 et 100 : "))
    if 1 <= nombre <= 100:
        print(f"Nombre valide : {nombre}.")
        break
    else:
        print("Nombre invalide. Réessayez.")
```

---

### **Exercice 18 : Calcul de volume**

```python
import math

rayon = float(input("Entrez le rayon de la sphère (en mètres) : "))
volume = (4 / 3) * math.pi * (rayon ** 3)
print(f"Le volume de la sphère est {volume:.2f} m³.")
```

---
