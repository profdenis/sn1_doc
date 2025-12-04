# **Corrigés 3 : Importation de modules**

---

## **Corrigés pour le module `random`**

### **Exercice 1 : Lancer de dé**
```python
import random
de = random.randint(1, 6)
print(f"Résultat du lancer de dé : {de}")
```

---

### **Exercice 2 : Nombre aléatoire flottant**
```python
import random
nombre_aleatoire = random.uniform(5.0, 10.0)
print(f"Nombre aléatoire : {nombre_aleatoire:.2f}")
```

---

### **Exercice 3 : Choix aléatoire**
```python
import random
fruits = ["pomme", "banane", "orange", "kiwi", "fraise"]
fruit_aleatoire = random.choice(fruits)
print(f"Fruit choisi : {fruit_aleatoire}")
```

---

### **Exercice 4 : Mélanger une liste**
```python
import random
nombres = [1, 2, 3, 4, 5]
print(f"Liste originale : {nombres}")
random.shuffle(nombres)
print(f"Liste mélangée : {nombres}")
```

---

### **Exercice 5 : Échantillon aléatoire**
```python
import random
nombres = list(range(1, 21))
echantillon = random.sample(nombres, 5)
print(f"Échantillon aléatoire : {echantillon}")
```

---

### **Exercice 6 : Jeu de pile ou face**
```python
import random
resultat = random.choice(["pile", "face"])
print(f"Résultat du lancer : {resultat}")
```

---

---

## **Corrigés pour le module `math`**

### **Exercice 7 : Calcul de racine carrée**
```python
import math
nombre = float(input("Entrez un nombre : "))
racine = math.sqrt(nombre)
print(f"Racine carrée de {nombre} : {racine:.2f}")
```

---

### **Exercice 8 : Calcul de l’hypoténuse**
```python
import math
cote1 = float(input("Entrez la longueur du premier côté : "))
cote2 = float(input("Entrez la longueur du deuxième côté : "))
hypotenuse = math.sqrt(cote1**2 + cote2**2)
print(f"Hypoténuse : {hypotenuse:.2f}")
```

---

### **Exercice 9 : Calcul de sinus**
```python
import math
degres = float(input("Entrez un angle en degrés : "))
radians = math.radians(degres)
sinus = math.sin(radians)
print(f"sin({degres}°) = {sinus:.4f}")
```

---

### **Exercice 10 : Calcul de logarithme**
```python
import math
nombre = float(input("Entrez un nombre : "))
logarithme = math.log10(nombre)
print(f"log10({nombre}) = {logarithme:.2f}")
```

---

### **Exercice 11 : Calcul de la circonférence d’un cercle**
```python
import math
rayon = float(input("Entrez le rayon du cercle : "))
circonference = 2 * math.pi * rayon
print(f"Circonférence : {circonference:.2f}")
```

---

---

## **Corrigés pour le module `datetime`**

### **Exercice 12 : Date et heure actuelles**
```python
from datetime import datetime
maintenant = datetime.now()
print(f"Date et heure actuelles : {maintenant.strftime('%Y-%m-%d %H:%M:%S')}")
```

---

### **Exercice 13 : Date formatée**
```python
from datetime import datetime
maintenant = datetime.now()
print(f"Date formatée : {maintenant.strftime('%d/%m/%Y')}")
```

---

### **Exercice 14 : Calcul de durée**
```python
from datetime import datetime
date_future_str = input("Entrez une date future (YYYY-MM-DD) : ")
date_future = datetime.strptime(date_future_str, "%Y-%m-%d")
maintenant = datetime.now()
duree = date_future - maintenant
print(f"Jours restants : {duree.days}")
```

---

### **Exercice 15 : Âge en jours**
```python
from datetime import datetime
date_naissance_str = input("Entrez votre date de naissance (YYYY-MM-DD) : ")
date_naissance = datetime.strptime(date_naissance_str, "%Y-%m-%d")
maintenant = datetime.now()
age_jours = (maintenant - date_naissance).days
print(f"Âge en jours : {age_jours}")
```

---

### **Exercice 16 : Heure de fin d’un événement**
```python
from datetime import datetime, timedelta
heure_debut_str = input("Entrez l'heure de début (HH:MM) : ")
duree_str = input("Entrez la durée (ex. 2h45) : ")
heure, minute = map(int, heure_debut_str.split(':'))
duree_heures, duree_minutes = map(int, duree_str.replace('h', ':').split(':'))
debut = datetime.strptime(heure_debut_str, "%H:%M").time()
duree = timedelta(hours=duree_heures, minutes=duree_minutes)
fin = (datetime.combine(datetime.today(), debut) + duree).time()
print(f"Heure de fin : {fin.strftime('%H:%M')}")
```

---

---

## **Corrigés pour les exercices combinés**

### **Exercice 17 : Simulation de lancer de dés**
```python
import random
lancers = [random.randint(1, 6) for _ in range(10)]
moyenne = sum(lancers) / len(lancers)
print(f"Résultats des lancers : {lancers}")
print(f"Moyenne des lancers : {moyenne:.2f}")
```

---

### **Exercice 18 : Calcul de date aléatoire**
```python
import random
from datetime import datetime, timedelta
date_debut = datetime(2020, 1, 1)
date_fin = datetime(2025, 12, 31)
duree = date_fin - date_debut
jours_aleatoires = random.randint(0, duree.days)
date_aleatoire = date_debut + timedelta(days=jours_aleatoires)
print(f"Date aléatoire : {date_aleatoire.strftime('%d/%m/%Y')}")
```

---

### **Exercice 19 : Calcul de volume d’une sphère**
```python
import math
rayon = float(input("Entrez le rayon de la sphère : "))
volume = (4/3) * math.pi * (rayon ** 3)
print(f"Volume de la sphère : {volume:.2f}")
```

---

### **Exercice 20 : Jeu de devinette amélioré**
```python
import random
nombre_a_deviner = random.randint(1, 100)
tentatives = 0
while True:
    devine = int(input("Devinez le nombre entre 1 et 100 : "))
    tentatives += 1
    if devine < nombre_a_deviner:
        print("Trop petit !")
    elif devine > nombre_a_deviner:
        print("Trop grand !")
    else:
        print(f"Bravo ! Vous avez trouvé en {tentatives} tentatives.")
        break
```

---
