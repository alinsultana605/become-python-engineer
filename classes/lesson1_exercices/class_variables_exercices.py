"""
1
Creează:

class Elev

cu:

an_scolar = 2026

și:
nume
varsta
în __init__.

Afișează:
e1.nume
e1.an_scolar
"""

class Elev:
    an_scolar = 2026

    def __init__(self, nume, varsta) -> None:
        self.nume = nume
        self.varsta = varsta


elev_1 = Elev('Alin', 15)
print(elev_1.nume)
print(elev_1.an_scolar)

"""
2

Creează:

class Masina

cu:

numar_roti = 4

și:

marca
model

în constructor.

Afișează:

m1.numar_roti
"""

class Masina:
    numar_roti = 4

    def __init__(self, model, marca) -> None:
        self.model = model
        self.marca = marca

m1 = Masina('ARKANA', 'Renault')
print(m1.numar_roti)

"""
3

Creează:

class Angajat

cu:

marire = 1.10

și metoda:

aplica_marire()

care mărește salariul.
"""

class Angajat:
    marire = 1.10
    
    def __init__(self, salariu) -> None:
        self.salariu = salariu

    def aplica_marire(self):
        self.salariu *= self.marire
    
a1 = Angajat(5000)
a2 = Angajat(6000)
print(a1.salariu)
a1.aplica_marire()
print(a1.salariu)

print(a2.salariu)
a2.aplica_marire()
print(a2.salariu)

"""
Exercițiu: Sistem de Bibliotecă 📚
"""
class Carte:
    categorie = "Educatie"

    def __init__(self, titlu, autor, pagini) -> None:
        self.titlu = titlu
        self.autor = autor
        self.pagini = pagini
        self.pagini_citite = 0

    def descriere(self):
        return f"{self.titlu} - {self.autor} ({self.pagini})"
        
    def este_lunga(self):
        return True if self.pagini > 300 else False
    
    def citeste(self, pagini):
        self.pagini -= pagini
        self.pagini_citite += pagini
        
carte1 = Carte('Python Basics', 'Alin', 250)
carte2 = Carte('Smecheria de facut bani', 'Romica Toader', 350)
carte = Carte("Python", "Alin", 250)

print(carte1.descriere())
print(carte2.descriere())

print(carte1.este_lunga())
print(carte2.este_lunga())

print(carte1.categorie)

carte.citeste(120)
print(carte.pagini)

"""
🏦 Exercițiu: Cont Bancar (Bank Account)
"""

class ContBancar:

    def __init__(self, nume, sold) -> None:
        self.nume = nume
        self.sold = sold

    def depunere(self, suma):
        self.sold += suma
    def retragere(self, suma):
        if suma <= self.sold:
            self.sold -= suma
        else:
            print("Fonduri insuficiente")
    def afiseaza_sold(self):
        return f"Ai in cont {self.sold}"

cont = ContBancar('Alin', 1000)

cont.depunere(500)
cont.retragere(300)
cont.retragere(1500)
print(cont.afiseaza_sold())