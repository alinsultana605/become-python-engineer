class Animal:
    def __init__(self, nume) -> None:
        self.nume = nume

    def vorbeste(self):
        return f'{self.nume} scoate un sunet'
    
class Caine(Animal):
    def vorbeste(self):
        return f"{self.nume} spune: Ham Ham"
    
c1 = Caine('Rext')
print(c1.vorbeste())


class Vehicul:
    def __init__(self, marca) -> None:
        self.marca = marca
    
    def info(self):
        return f"{self.marca}"
    
class Masina(Vehicul):
    def __init__(self, marca, model) -> None:
        super().__init__(marca)
        self.model = model

    def info(self):
        return f"Masina marca: {self.marca}, model {self.model}"

c1 = Masina("Dacia", "Logan")
print(c1.info())


class Persoana:
    def __init__(self, nume, prenume) -> None:
        self.nume = nume
        self.prenume = prenume
    
class Student(Persoana):
    def __init__(self, nume, prenume, nota) -> None:
        super().__init__(nume, prenume)
        self.nota = nota

    def afiseaza_student(self):
        return f"Studentul {self.nume}, {self.prenume}, a luat nota: {self.nota}"
    
c1 = Student('Alin', 'Stefan', 10)
print(c1.afiseaza_student())


class Angajat:
    def __init__(self, nume, salariu) -> None:
        self.nume = nume
        self.salariu = salariu

    def info(self):
        return f"{self.nume} are salariu : {self.salariu}"
    
class Manager(Angajat):
    def __init__(self, nume, salariu, departament) -> None:
        super().__init__(nume, salariu)
        self.departament = departament
    def info(self):
        baza = super().info()
        return f"{baza} și este manager la departamentul {self.departament}"    

c1 = Manager("Sultana", 5000, "IT")
print(c1.info())


class Carte:
    def __init__(self, titlu, autor) -> None:
        self.titlu = titlu
        self.autor = autor

class Ebook(Carte):
    def __init__(self, titlu, autor, marime_fisier) -> None:
        super().__init__(titlu, autor)
        self.marime_fisier = marime_fisier

    def info(self):
        return f"Ebook: {self.titlu} de {self.autor}, {self.marime_fisier} MB"
    

c1 = Ebook("Python OOP", "Sultana", 5)
print(c1.info())

class Produs:
    tva = 0.19
    def __init__(self, produs, pret) -> None:
        self.produs = produs
        self.pret = float(pret)
    
    @staticmethod
    def adauga_tva(pret):
        tva = 0.19
        valoare_tva = pret * tva
        pret_final = valoare_tva + pret
        return f"Pret final: {pret_final}"
    

class ProdusAlimentar(Produs):
    def __init__(self, produs, pret, expire) -> None:
        super().__init__(produs, pret)
        self.expire = expire

    @classmethod
    def din_string(cls, txt):
        produs, pret, expire = txt.split("-")
        return cls(produs, float(pret), expire)

c1 = Produs("Lapte", 15)
print(c1.adauga_tva(15))

c2 = ProdusAlimentar.din_string("Lapte-200-25.05")
print(c2.produs)
print(c2.pret)
print(c2.expire)
        

class Animals():
    def __init__(self, nume) -> None:
        self.nume = nume

    def vorbeste(self):
         return f"{self.nume} scoate un sunet."
    
class Dog(Animal):
    def __init__(self, nume) -> None:
        super().__init__(nume)

    def vorbeste(self):
        return "Ham , Ham"
    
class Cat(Animal):
    def __init__(self, nume) -> None:
        super().__init__(nume)
    
    def vorbeste(self):
        return "Miau Miau"
    
animale = [
    Cat("Rex"),
    Cat("Miti"),
    Dog("Azor"),
    Cat("Luna")
]

for animal in animale:
    print(animal.vorbeste())


class A:
    def m1(self):
        return "Metoda m1 din A"


class B:
    def m2(self):
        return "Metoda m2 din B"


class C(A, B):
    pass


c = C()
print(c.m1())   # vine din A
print(c.m2())   # vine din B


class Telefon:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
    
    def descriere(self):
        return f"{self.brand}, {self.model}"
    
c1 = Telefon("Iphone", "6s")
print(c1.descriere())


class Cerc:
    pi = 3.14
    def __init__(self, raza) -> None:
        self.raza = raza
    
    def arie(self):
         return self.pi * (self.raza ** 2)
    
    def diametru(self):
        return 2 * self.raza
    
c1 = Cerc(4)
print(c1.arie())
print(c1.diametru())

class Agenda:
    def __init__(self):
        self.contacte = []

    def adauga_contact(self, nume):
        self.contacte.append(nume)

    def afiseaza(self):
        return self.contacte


a = Agenda()
a.adauga_contact("Alin")
a.adauga_contact("Sultana")
print(a.afiseaza())

class Masina_2:
    numar_masini = 0
    def __init__(self,marca) -> None:
        self.marca = marca
        Masina_2.numar_masini += 1
        
    
    def info(self):
        return f" Masina {self.marca} are {self.numar_masini} masini"
    
m1 = Masina_2("Dacia")
m2 = Masina_2("BMW")

print(Masina_2.numar_masini)
print(m1.marca)
print(m2.marca)

class ListaTest:
    elemente = []

    def adauga(self, x):
        self.elemente.append(x)
    
    def afiseaza(self):
        return f"{self.elemente}"
    
a = ListaTest()
b = ListaTest()

a.adauga("Ana")
b.adauga("Ion")

print(a.afiseaza())
print(b.afiseaza())

class ListaTest2:

    def adauga(self, x):
        self.elemente = []
        self.elemente.append(x)
    
    def afiseaza(self):
        return f"{self.elemente}"
    
a = ListaTest2()
b = ListaTest2()

a.adauga("Ana")
b.adauga("Ion")

print(a.afiseaza())
print(b.afiseaza())

class Student_2:
    total_studenti = 0

    def __init__(self, nume) -> None:
        self.nume = nume
        Student_2.total_studenti +=1
    
    def info(self):
        return self.total_studenti

s1 = Student_2("Alin")
s2 = Student_2("Sultana")

print(Student_2.total_studenti)
print(s1.nume)
print(s2.nume)

class Setari:
    tema = 'light'

    def schimba_tema(self, noua_tema):
        Setari.tema = noua_tema

    @classmethod
    def schimba_tema_globala(cls, noua_tema):
        cls.tema = noua_tema
        
s1 = Setari()
s2 = Setari()
s1.schimba_tema("blue")
Setari.schimba_tema_globala("dark")
print(s1.tema)
print(s2.tema)

class Email:
    def __init__(self, adresa) -> None:
        self.adresa = adresa

    @staticmethod
    def este_valid(email):
        if "@" in email and "." in email:
            return  "Email este valid"
        else:
            return "Email nu este Valid"
        
c1 = Email("alinstefan@gmail.com")
c2 = Email("alinstefan")

print(c1.este_valid("alinstefan@gmail.com"))
print(c2.este_valid("alinstefa"))

class Film:
    def __init__(self, titlu, an) -> None:
        self.titlu = titlu
        self.an = an

    @classmethod
    def din_string(cls, txt):
        titlu, an = txt.split("-")
        return cls (titlu,an)
    
c1 = Film("Titanic", 1997)
c2 = Film.din_string("Romania-1997")
print(c2.titlu)
print(c2.an)


class Contor:
    numar = 0

    def __init__(self) -> None:
        Contor.numar += 1
    
    def cate(self):
        return Contor.numar
    
c1 = Contor()
c2 = Contor()
print(c1.cate())

class Vehicul_2:
    def __init__(self,marca) -> None:
        self.marca = marca
    def info(self):
        return f"Marca Vehicul este: {self.marca}"

class Motocicleta(Vehicul_2):
    def __init__(self, marca, tip_motor) -> None:
        super().__init__(marca)
        self.tip_motor = tip_motor

    def info(self):
        return f"{self.marca} are motorul {self.tip_motor}"
c1 = Vehicul_2("Renault")
c2 = Motocicleta("BMW", "Disel")

print(c1.info())
print(c2.info())

class Persoana_3:
    def __init__(self, nume, prenume) -> None:
        self.nume = nume
        self.prenume = prenume
    
    def descriere(self):
        return f"{self.nume}, {self.prenume}"

class Profesor(Persoana_3):
    def __init__(self, nume, prenume, materie) -> None:
        super().__init__(nume, prenume)
        self.materie = materie

    def descriere(self):
        baza = super().descriere()
        return f"{baza}, profesor de {self.materie}"
c1 = Persoana_3("Alin", "Stefan")
print(c1.descriere())
c2 = Profesor("Madalina", "Luiza", "Matematica")
print(c2.descriere())

class Animal_2:
    def __init__(self, nume) -> None:
        self.nume = nume
    
    def sunet(self):
         return f"{self.nume} scoate un sunet."

class Vaca(Animal_2):
    def __init__(self, nume) -> None:
        super().__init__(nume)

    def sunet(self):
        baza = super().sunet()
        return f"{baza}, Muuu"
    
class Oaie(Animal_2):
    def __init__(self, nume) -> None:
        super().__init__(nume)

    def sunet(self):
        baza = super().sunet()
        return f"{baza}, Beeee"
    

class Porc(Animal_2):
    def __init__(self, nume) -> None:
        super().__init__(nume)
    def sunet(self):
        baza = super().sunet()
        return f"{baza}, Oink"
    
animale = [
    Vaca("Luna"),
    Oaie("Marcela"),
    Porc("Ghita"),
    Porc("Costica")
]

for animal in animale:
    print(animal.sunet())


class Radio:
    def porneste(self):
        return "Radio Pornit"

class GPS:
    def porneste(self):
        return 'GPS Pornit'
    
class MasinaSmart(Radio, GPS):
    pass

m = MasinaSmart()
print(m.porneste())

class Angajat_2:
    def __init__(self, nume, salariu) -> None:
        self.nume = nume
        self.salariu = salariu
    
    def info(self):
        return f"Angajatul {self.nume} are {self.salariu} salariu"
    
class Programator(Angajat_2):
    def __init__(self, nume, salariu, limbaj_de_programare) -> None:
        super().__init__(nume, salariu)
        self.limbaj_de_programare = limbaj_de_programare
    
    def info(self):
        baza = super().info()
        return f"{baza} si este {self.limbaj_de_programare} engineer"
    
c1 = Angajat_2("Alin", 9000)
print(c1.info())

c2 = Programator("Marian", 10000, "Python")
print(c2.info())