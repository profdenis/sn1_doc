
# **Corrigés 4: Définition et utilisation des fonctions**

---

### **Exercice 1 : Calcul du volume d'un cylindre**
```python
import math

def volume_cylindre(rayon, hauteur):
    """Calcule le volume d'un cylindre à partir de son rayon et de sa hauteur."""
    return math.pi * rayon ** 2 * hauteur

# Appel de la fonction
rayon = float(input("Entrez le rayon du cylindre : "))
hauteur = float(input("Entrez la hauteur du cylindre : "))
volume = volume_cylindre(rayon, hauteur)
print(f"Le volume du cylindre est {volume:.2f}.")
```

---

### **Exercice 2 : Calcul de l'aire d'un triangle**
```python
def aire_triangle(base, hauteur):
    """Calcule l'aire d'un triangle à partir de sa base et de sa hauteur."""
    return (base * hauteur) / 2

# Appel de la fonction
base = float(input("Entrez la base du triangle : "))
hauteur = float(input("Entrez la hauteur du triangle : "))
aire = aire_triangle(base, hauteur)
print(f"L'aire du triangle est {aire:.2f}.")
```

---

### **Exercice 3 : Conversion de degrés Celsius en Fahrenheit**
```python
def celsius_vers_fahrenheit(celsius):
    """Convertit une température de degrés Celsius en degrés Fahrenheit."""
    return celsius * 9/5 + 32

# Appel de la fonction
celsius = float(input("Entrez la température en degrés Celsius : "))
fahrenheit = celsius_vers_fahrenheit(celsius)
print(f"{celsius}°C équivaut à {fahrenheit:.1f}°F.")
```

---

### **Exercice 4 : Calcul de l'hypoténuse d'un triangle rectangle**
```python
import math

def hypoténuse(cote1, cote2):
    """Calcule l'hypoténuse d'un triangle rectangle à partir des deux côtés."""
    return math.sqrt(cote1 ** 2 + cote2 ** 2)

# Appel de la fonction
cote1 = float(input("Entrez la longueur du premier côté : "))
cote2 = float(input("Entrez la longueur du deuxième côté : "))
hypotenuse_resultat = hypoténuse(cote1, cote2)
print(f"L'hypoténuse du triangle rectangle est {hypotenuse_resultat:.2f}.")
```

---

### **Exercice 5 : Calcul du périmètre d'un cercle**
```python
import math

def perimetre_cercle(rayon):
    """Calcule le périmètre d'un cercle à partir de son rayon."""
    return 2 * math.pi * rayon

# Appel de la fonction
rayon = float(input("Entrez le rayon du cercle : "))
perimetre = perimetre_cercle(rayon)
print(f"Le périmètre du cercle est {perimetre:.2f}.")
```

---

### **Exercice 6 : Calcul de la surface d'une sphère**
```python
import math

def surface_sphere(rayon):
    """Calcule la surface d'une sphère à partir de son rayon."""
    return 4 * math.pi * rayon ** 2

# Appel de la fonction
rayon = float(input("Entrez le rayon de la sphère : "))
surface = surface_sphere(rayon)
print(f"La surface de la sphère est {surface:.2f}.")
```

---

### **Exercice 7 : Calcul du volume d'une sphère**
```python
import math

def volume_sphere(rayon):
    """Calcule le volume d'une sphère à partir de son rayon."""
    return (4/3) * math.pi * rayon ** 3

# Appel de la fonction
rayon = float(input("Entrez le rayon de la sphère : "))
volume = volume_sphere(rayon)
print(f"Le volume de la sphère est {volume:.2f}.")
```

---

### **Exercice 8 : Calcul de la distance entre deux points dans un plan**
```python
import math

def distance_deux_points(x1, y1, x2, y2):
    """Calcule la distance entre deux points dans un plan cartésien."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Appel de la fonction
x1 = float(input("Entrez la coordonnée x du premier point : "))
y1 = float(input("Entrez la coordonnée y du premier point : "))
x2 = float(input("Entrez la coordonnée x du deuxième point : "))
y2 = float(input("Entrez la coordonnée y du deuxième point : "))
distance = distance_deux_points(x1, y1, x2, y2)
print(f"La distance entre les deux points est {distance:.2f}.")
```

---

-------

??? info "Utilisation de l'IA"
      Page rédigée en partie avec l'aide d'un assistant IA, principalement à l'aide de Perplexity AI. L'IA a été 
      utilisée pour générer des explications, des exemples et/ou des suggestions de structure. Toutes les informations 
      ont été vérifiées, éditées et complétées par l'auteur.
