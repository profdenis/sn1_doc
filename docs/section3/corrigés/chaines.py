import re

# Exercices de base
def exercice_1_inverser():
    def inverser(chaine):
        return chaine[::-1]
    print(inverser("Python"))

def exercice_2_compter_mots():
    def compter_mots(chaine):
        return len(chaine.split())
    print(compter_mots("Bonjour tout le monde"))

def exercice_3_palindrome():
    def est_palindrome(chaine):
        return chaine == chaine[::-1]
    print(est_palindrome("radar"))
    print(est_palindrome("python"))

def exercice_4_majuscules_alternées():
    def majuscules_alternées(chaine):
        resultat = []
        for i, lettre in enumerate(chaine):
            if i % 2 == 0:
                resultat.append(lettre.lower())
            else:
                resultat.append(lettre.upper())
        return "".join(resultat)
    print(majuscules_alternées("python"))

def exercice_5_censurer():
    def censurer(texte, mot_interdit):
        return texte.replace(mot_interdit, "*" * len(mot_interdit))
    print(censurer("Ce mot est interdit.", "interdit"))

def exercice_6_initiales():
    def initiales(nom_complet):
        mots = nom_complet.split()
        return " ".join([f"{mot[0]}." for mot in mots])
    print(initiales("Denis Rinfret"))

def exercice_7_code_postal():
    def est_code_postal_valide(code):
        return bool(re.match(r'^[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d$', code))
    print(est_code_postal_valide("H3T 1J4"))
    print(est_code_postal_valide("H3T1J4"))

def exercice_8_extraire_nombres():
    def extraire_nombres(chaine):
        return [int(nombre) for nombre in re.findall(r'\d+', chaine)]
    print(extraire_nombres("Il a 3 pommes et 5 bananes."))

# Exercices combinant chaînes et listes
def exercice_9_chaine_en_liste():
    def chaine_en_liste(chaine):
        return chaine.split()
    print(chaine_en_liste("Bonjour tout le monde"))

def exercice_10_mots_les_plus_long():
    def mots_les_plus_long(mots):
        if not mots:
            return []
        longueur_max = max(len(mot) for mot in mots)
        return [mot for mot in mots if len(mot) == longueur_max]
    print(mots_les_plus_long(["pomme", "banane", "cerise", "ananas"]))

def exercice_11_compter_voyelles_liste():
    def compter_voyelles_liste(mots):
        voyelles = "aeiouyAEIOUY"
        compte = 0
        for mot in mots:
            for lettre in mot:
                if lettre in voyelles:
                    compte += 1
        return compte
    print(compter_voyelles_liste(["pomme", "banane", "kiwi"]))

def exercice_12_inverser_mots():
    def inverser_mots(chaine):
        mots = chaine.split()
        return " ".join(reversed(mots))
    print(inverser_mots("Bonjour tout le monde"))

def exercice_13_filtrer_mots():
    def filtrer_mots(mots, lettre):
        return [mot for mot in mots if mot.startswith(lettre)]
    print(filtrer_mots(["pomme", "banane", "poire", "cerise"], "p"))

# Exercices combinant chaînes et boucles/conditionnelles
def exercice_14_mot_de_passe_valide():
    def est_mot_de_passe_valide(mot_de_passe):
        if len(mot_de_passe) < 8:
            return False
        if not any(c.isupper() for c in mot_de_passe):
            return False
        if not any(c.isdigit() for c in mot_de_passe):
            return False
        return True
    print(est_mot_de_passe_valide("MotDePasse123"))
    print(est_mot_de_passe_valide("motdepasse"))

def exercice_15_remplacer_voyelles():
    def remplacer_voyelles(chaine, caractere):
        voyelles = "aeiouyAEIOUY"
        resultat = []
        for lettre in chaine:
            if lettre in voyelles:
                resultat.append(caractere)
            else:
                resultat.append(lettre)
        return "".join(resultat)
    print(remplacer_voyelles("Bonjour", "*"))

def exercice_16_compter_occurrences():
    def compter_occurrences(chaine):
        chaine = chaine.lower().replace(" ", "")
        occurrences = {}
        for lettre in chaine:
            if lettre in occurrences:
                occurrences[lettre] += 1
            else:
                occurrences[lettre] = 1
        return sorted(occurrences.items())
    print(compter_occurrences("Bonjour"))

def exercice_17_trouver_anagrammes():
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

# Exercices combinant chaînes et fonctions
def exercice_18_cesar():
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
    print(cesar("Bonjour", 3))

def exercice_19_capitaliser():
    def capitaliser(chaine, exclus):
        mots = chaine.split()
        resultat = []
        for mot in mots:
            if mot.lower() in [e.lower() for e in exclus]:
                resultat.append(mot.lower())
            else:
                resultat.append(mot.capitalize())
        return " ".join(resultat)
    print(capitaliser("bonjour tout le monde", ["le"]))

def exercice_20_tronquer():
    def tronquer(chaine, longueur):
        if len(chaine) <= longueur:
            return chaine
        return chaine[:longueur] + "..."
    print(tronquer("Bonjour tout le monde", 10))

def main():
    print("Exécution des corrigés sur les chaînes de caractères...\n")

    # Exercices de base
    exercice_1_inverser()
    exercice_2_compter_mots()
    exercice_3_palindrome()
    exercice_4_majuscules_alternées()
    exercice_5_censurer()
    exercice_6_initiales()
    exercice_7_code_postal()
    exercice_8_extraire_nombres()

    # Exercices combinant chaînes et listes
    exercice_9_chaine_en_liste()
    exercice_10_mots_les_plus_long()
    exercice_11_compter_voyelles_liste()
    exercice_12_inverser_mots()
    exercice_13_filtrer_mots()

    # Exercices combinant chaînes et boucles/conditionnelles
    exercice_14_mot_de_passe_valide()
    exercice_15_remplacer_voyelles()
    exercice_16_compter_occurrences()
    exercice_17_trouver_anagrammes()

    # Exercices combinant chaînes et fonctions
    exercice_18_cesar()
    exercice_19_capitaliser()
    exercice_20_tronquer()

    print("\nTous les corrigés ont été exécutés.")

if __name__ == "__main__":
    main()