# **Corrigés : Structures conditionnelles**

---

### **Exercice 1 : Vérification de pair ou impair**

```python
nombre = int(input("Entrez un nombre : "))
if nombre % 2 == 0:
    print(f"{nombre} est pair.")
else:
    print(f"{nombre} est impair.")
```

---

### **Exercice 2 : Comparaison de trois nombres**

```python
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))
c = float(input("Entrez le troisième nombre : "))

if a >= b and a >= c:
    print(f"Le plus grand nombre est {a}.")
elif b >= a and b >= c:
    print(f"Le plus grand nombre est {b}.")
else:
    print(f"Le plus grand nombre est {c}.")
```

---

### **Exercice 3 : Catégorisation d'âge**

```python
age = int(input("Entrez votre âge : "))
if age < 12:
    print("Enfant")
elif 12 <= age <= 17:
    print("Adolescent")
elif 18 <= age <= 64:
    print("Adulte")
else:
    print("Senior")
```

---

### **Exercice 4 : Vérification de conditions logiques**

```python
a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

if a == b:
    print("Les deux nombres sont égaux.")
elif a > b:
    print("Le premier nombre est plus grand.")
else:
    print("Le deuxième nombre est plus grand.")
```

---

### **Exercice 5 : Vérification de multiples de 3 et 5**

```python
nombre = int(input("Entrez un nombre : "))
if nombre % 3 == 0 and nombre % 5 == 0:
    print("FizzBuzz")
elif nombre % 3 == 0:
    print("Fizz")
elif nombre % 5 == 0:
    print("Buzz")
else:
    print(nombre)
```

---

### **Exercice 6 : Calcul de réduction**

```python
montant = float(input("Entrez le montant total des achats : "))
if montant > 100:
    montant_final = montant * 0.9
    print(f"Montant final après une réduction de 10 % : {montant_final:.2f} $")
elif montant > 50:
    montant_final = montant * 0.95
    print(f"Montant final après une réduction de 5 % : {montant_final:.2f} $")
else:
    print(f"Aucune réduction appliquée. Montant final : {montant:.2f} $")
```

---

### **Exercice 7 : Vérification de conditions météorologiques**

```python
temperature = float(input("Entrez la température actuelle (en °C) : "))
if temperature > 30:
    print("Il fait très chaud.")
elif 20 <= temperature <= 30:
    print("Il fait chaud.")
elif 10 <= temperature < 20:
    print("Il fait doux.")
else:
    print("Il fait froid.")
```

---

### **Exercice 8 : Calcul de l'IMC et catégorisation**

```python
poids = float(input("Entrez votre poids (en kg) : "))
taille = float(input("Entrez votre taille (en mètres) : "))
imc = poids / (taille ** 2)

print(f"Votre IMC est {imc:.2f}.")
if imc < 18.5:
    print("Maigreur")
elif 18.5 <= imc < 25:
    print("Poids normal")
elif 25 <= imc < 30:
    print("Surpoids")
else:
    print("Obésité")
```

---
