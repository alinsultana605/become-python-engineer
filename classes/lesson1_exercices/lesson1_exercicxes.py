"""
Dacă ai ajuns la "Python OOP Tutorial 1: Classes and Instances" de Corey Schaffer, intri într-o zonă foarte importantă din Python.

Până acum ai lucrat cu:

nume = "Alin"
varsta = 26
oras = "Gaesti"

sau:

persoana = {
    "nume": "Alin",
    "varsta": 26,
    "oras": "Gaesti"
}

Problema este că dacă ai 100 de persoane, trebuie să faci 100 de dicționare.

OOP rezolvă asta.

Ce este o clasă?

O clasă este un șablon (blueprint).

Exemplu:

class Persoana:
    pass

Momentan clasa există, dar nu face nimic.

Ce este o instanță?

Dacă clasa este planul unei mașini:

class Masina:
    pass

atunci:

dacia = Masina()

este o mașină construită după acel plan.
"""

"""
1.

Creează clasa:

class Persoana

cu:

nume
varsta

și afișează valorile.
"""
class Persoana:
    def __init__(self, nume, varsta) -> None:
      self.nume = nume
      self.varsta = varsta

    def salut(self):
       return f"Salut eu sunt, {self.nume}"
p1 = Persoana('Alin', 25)
print(p1.nume)
print(p1.varsta)

"""
2.

Adaugă metoda:

salut()

care afișează:

Salut, eu sunt Alin
"""
print(p1.salut())


"""
3.

Creează clasa:

Masina

cu:

marca
model
an

și afișează informațiile
"""

class Masina:
    def __init__(self, marca, model, an) -> None:
      self.marca = marca
      self.model = model
      self.an = an

    def descriere(self):
        return f"{self.marca} {self.model} {self.an}"

info = Masina('Dacia', 'Logan', 2024)
info_2 = Masina('Dacia', 'Duster', 2024)
print(info.marca)
print(info.model)
print(info.an)

print(info_2.descriere())