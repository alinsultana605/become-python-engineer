class Carte:
    def __init__(self, titlu, pagini):
        self.titlu = titlu
        self.pagini = pagini

    def __str__(self):
        return f"Carte: {self.titlu}"

    def __len__(self):
        return self.pagini

    def __add__(self, other):
        return self.pagini + other.pagini


c1 = Carte("Python", 300)
c2 = Carte("OOP", 200)

print(c1)          # __str__
print(len(c1))     # __len__
print(c1 + c2)     # __add__

class Carte_2:
    def __init__(self, titlu, autor) -> None:
        self.titlu = titlu
        self.autor = autor

    def __str__(self) -> str:
        return f"Carte: {self.titlu} scrisa de {self.autor}"
    
    def __repr__(self) -> str:
         return f"Carte_2(titlu='{self.titlu}', autor='{self.autor}')"
    
c = Carte_2("Ion", "Liviu Rebreanu")
print(c)          # __str__
print(repr(c))    # __repr__

class Playlist:

    def __init__(self) -> None:
        self.playlist = []

    def adauga_melodie(self, nume):
        self.playlist.append(nume)
    
    def __len__(self):
        return len(self.playlist)
    
p = Playlist()
p.adauga_melodie("Song 1")
p.adauga_melodie("Song 2")
print(len(p))     # 2

class Student:
    def __init__(self, nume, nota) -> None:
        self.nume = nume
        self.nota = nota

    def __eq__(self, other) -> bool:
        return self.nota == other.nota
    
    def __lt__(self, other):
        return self.nota < other.nota

s1 = Student("Ana", 9)
s2 = Student("Ion", 10)
print(s1 < s2)    # True
print(s1 == s2)   # False

class Produs:
    def __init__(self, nume, pret) -> None:
        self.nume = nume
        self.pret = pret

    def __add__(self, other):
        return self.pret + other.pret
    
p1 = Produs("Paine", 5)
p2 = Produs("Lapte", 7)
print(p1 + p2)    # 12

class Catalog:
    def __init__(self) -> None:
        self.catalog = []
    def adauga_elev(self, nume):
        self.catalog.append(nume)

    def __getitem__(self, key):
        return self.catalog[key]
    
c = Catalog()
c.adauga_elev("Ana")
c.adauga_elev("Ion")
print(c[0])       # Ana


class Colectie:
    def __init__(self, elemente) -> None:
        self.elemente = elemente
    
    def __iter__(self):
        return iter(self.elemente)
    
col = Colectie([1, 2, 3])

for x in col:
    print(x)

class CosCumparaturi:
    def __init__(self, elemente) -> None:
        self.elemente = elemente

    def __len__(self):
        return len(self.elemente)
    
    def __getitem__(self, key):
        return self.elemente[key]
    
    def __add__(self, other):
        return CosCumparaturi(self.elemente + other.elemente)
    
    def __str__(self) -> str:
        return f"Am urmatoarele {self.elemente}"
c1 = CosCumparaturi(["Paine", "Lapte"])
c2 = CosCumparaturi(["Oua"])
c3 = c1 + c2
print(len(c3))     # 3
print(c3[1])       # Lapte
print(c3)          # afișare frumoasă
