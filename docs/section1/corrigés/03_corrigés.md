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




---

## **Corrigés pour le module `math`**

### **Exercice 3 : Calcul de racine carrée**

```python
import math

nombre = float(input("Entrez un nombre : "))
racine = math.sqrt(nombre)
print(f"Racine carrée de {nombre} : {racine:.2f}")
```

---

### **Exercice 4 : Calcul de l’hypoténuse**

```python
import math

cote1 = float(input("Entrez la longueur du premier côté : "))
cote2 = float(input("Entrez la longueur du deuxième côté : "))
hypotenuse = math.sqrt(cote1 ** 2 + cote2 ** 2)
print(f"Hypoténuse : {hypotenuse:.2f}")
```

---

### **Exercice 5 : Calcul de sinus**

```python
import math

degres = float(input("Entrez un angle en degrés : "))
radians = math.radians(degres)
sinus = math.sin(radians)
print(f"sin({degres}°) = {sinus:.4f}")
```

---

### **Exercice 6 : Calcul de logarithme**

```python
import math

nombre = float(input("Entrez un nombre : "))
logarithme = math.log10(nombre)
print(f"log10({nombre}) = {logarithme:.2f}")
```

---

### **Exercice 7 : Calcul de la circonférence d’un cercle**

```python
import math

rayon = float(input("Entrez le rayon du cercle : "))
circonference = 2 * math.pi * rayon
print(f"Circonférence : {circonference:.2f}")
```

---

---

## **Corrigés pour le module `datetime`**

### **Exercice 8 : Date et heure actuelles**

```python
from datetime import datetime

maintenant = datetime.now()
print(f"Date et heure actuelles : {maintenant.strftime('%Y-%m-%d %H:%M:%S')}")
```

---

### **Exercice 9 : Date formatée**

```python
from datetime import datetime

maintenant = datetime.now()
print(f"Date formatée : {maintenant.strftime('%d/%m/%Y')}")
```

---

### **Exercice 10 : Calcul de durée**

```python
from datetime import datetime

date_future_str = input("Entrez une date future (YYYY-MM-DD) : ")
date_future = datetime.strptime(date_future_str, "%Y-%m-%d")
maintenant = datetime.now()
duree = date_future - maintenant
print(f"Jours restants : {duree.days}")
```

---

### **Exercice 11 : Âge en jours**

```python
from datetime import datetime

date_naissance_str = input("Entrez votre date de naissance (YYYY-MM-DD) : ")
date_naissance = datetime.strptime(date_naissance_str, "%Y-%m-%d")
maintenant = datetime.now()
age_jours = (maintenant - date_naissance).days
print(f"Âge en jours : {age_jours}")
```

---

### **Exercice 12 : Heure de fin d’un événement**

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

----------

??? info "Utilisation de l'IA"
    Page rédigée en partie avec l'aide d'un assistant IA. L'IA a été utilisée pour générer des 
    explications, des exemples et/ou des suggestions de structure. Toutes les informations ont 
    été vérifiées, éditées et complétées par l'auteur.
