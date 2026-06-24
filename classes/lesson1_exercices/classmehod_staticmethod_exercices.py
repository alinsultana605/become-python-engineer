"""
🧠 Ideea generală (pe scurt)

Într-o clasă ai 3 tipuri de metode:

| Tip           | Ce primește   | La ce folosește                |
| ------------- | ------------- | ------------------------------ |
| normal method | `self`        | lucrează cu un obiect          |
| classmethod   | `cls`         | lucrează cu clasa              |
| staticmethod  | nimic special | funcție “în interiorul clasei” |

class Elev:
    an_scolar = 2026

    def __init__(self, nume):
        self.nume = nume

    @classmethod
    def schimba_an(cls, noul_an):
        cls.an_scolar = noul_an

        
        Staticmethod
👉 NU are acces la self sau cls

Este doar o funcție pusă în clasă.

@staticmethod
class Matematica:

    @staticmethod
    def aduna(a, b):
        return a + b
"""
"""
🧪 Exerciții – nivel 1 (basic)
1. Staticmethod simplu

Creează o clasă Calculator cu:

o metodă statică aduna(a, b) care returnează suma

Testează:

Calculator.aduna(2, 3)
"""
class Calculator:
    @staticmethod
    def aduna(a, b):
        return a + b
    
print(Calculator.aduna(2, 3))

"""
2. Staticmethod – verificare număr

Creează clasa Numar cu:

staticmethod este_par(n) → returnează True / False

Testează cu mai multe numere.
"""
class Numar:
    @staticmethod
    def este_par(n):
        if n % 2 == 0:
            return True
        else:
            return False
        
print(Numar.este_par(20))

#3.
class Student:
    scoala = "IT School"

    def __init__(self, nume) -> None:
        self.nume = nume

    @classmethod
    def schimba_scoala(cls, nume_scoala):
        cls.scoala = nume_scoala

Student.schimba_scoala('English School')
print(Student.scoala)

#4.
class Masina:
    def __init__(self, marca, model, an):
        self.marca = marca
        self.model = model
        self.an = an

    @classmethod
    def from_string(cls, txt):
        marca, model, an = txt.split("-")   
        return cls(marca, model, int(an))
    
c1 = Masina.from_string("Dacia-Logan-2024")

print(c1.marca)
print(c1.model)
print(c1.an)


class Utilizator:
    def __init__(self, nume, varsta) -> None:
        self.nume = nume
        self.varsta = varsta
    
    @staticmethod
    def este_major(varsta):
        if varsta >= 18:
            return "Este major"
        else:
            return "Este minor"
        
    @classmethod
    def din_an_nastere(cls, nume, an_nastere):
        from datetime import datetime
        anul_curent = datetime.now().year
        varsta = anul_curent - an_nastere

        return cls (nume,varsta)
    

u1 = Utilizator("Ana", 20)
u2 = Utilizator.din_an_nastere("Matei", 2005)

print(u1.varsta)  
print(u2.varsta)  

class Produs:
    def __init__(self, produs, pret) -> None:
        self.produs = produs
        self.pret = pret

    @classmethod
    def pret_redus(cls, produs, pret, reducere):
        pretul_redus = pret - (pret * reducere / 100)

        return cls (produs, pretul_redus)
    

u2 = Produs.pret_redus("Paine", 150, 10)
print(u2.pret)


class Masina_2:
    numar_masini = 0

    def __init__(self, model) -> None:
        self.model = model

    @classmethod
    def masini_create(cls):
        cls.numar_masini +=1
        return cls.numar_masini
    
c1 = Masina_2("Arkana")
c2 = Masina_2("Megane")

Masina_2.masini_create()
print(c1.model)

    

class Users:
    def __init__(self, nume, prenume) -> None:
        self.nume = nume
        self.prenume = prenume
    
    @classmethod
    def imparte_stringul(cls, txt):
        nume, prenume = txt.split("-")
        return cls (nume, prenume)

c1 = Users("Alin", "Stefan")
c2 = Users.imparte_stringul("Alin-Stefan")
print(c2.nume)
print(c2.prenume)


class User_2:
    def __init__(self, email) -> None:
        self.email = email

    @staticmethod
    def verify_email(email):
        if "@" in email and "." in email:
            return True
        else:
            return False
c1 = User_2("sultanastefan@gmail.com")
print(User_2.verify_email("sultanastefangmail.com"))


class Factura:
    def __init__(self, pret) -> None:
        self.pret = pret

    def afiseaza(self):
        return self.pret

    @staticmethod
    def tva(pret):
        pret_tva = pret + (pret * 19) / 100
        return pret_tva
    
c1 = Factura(250)
print(c1.afiseaza())   
print(Factura.tva(200))


class Number:
    def __init__(self, numar) -> None:
        self.numar = numar

    @staticmethod
    def este_par(numar):
        if numar % 2 == 0:
            return "Este par"
        else:
            return "Este impar"
        
c1 = Number(2)
print(c1.este_par(3))

class User:
    def __init__(self, name, varsta) -> None:
        self.name = name
        self.varsta = varsta

    @classmethod
    def to_str(cls, txt):
        nume, varsta = txt.split(",")
        return cls (nume, varsta)
    
c1 = User("Ana", 25)
c2 = User.to_str("Ana,25")

print(c2.name)
print(c2.varsta)
    

class Person:
    def __init__(self, nume, prenume) -> None:
        self.nume = nume
        self.prenume = prenume

    def afiseaza_persoana(self):
        print(self.nume ,self.prenume)

c1 = Person("Alin", "Sultana")
c1.afiseaza_persoana()

        