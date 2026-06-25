""" Ce sunt Getters, Setters și Deleters?
Sunt metode speciale care controlează:

citirea unui atribut → getter

modificarea unui atribut → setter

ștergerea unui atribut → deleter

În Python, acestea se fac cu decoratorul @property.
🎯 De ce avem nevoie de ele?
Pentru că uneori:

vrei să validezi datele înainte să fie setate

vrei să protejezi un atribut

vrei să ascunzi implementarea internă

vrei să controlezi ce se întâmplă când cineva modifică o valoare

| Ce? | Decorator | Ce face? |
| --- | --- | --- |
| Getter | ``@property`` | returnează valoarea |
| Setter | ``@nume.setter`` | setează valoarea cu validare |
| Deleter | ``@nume.deleter`` | șterge atributul |

"""

class ContBancar:
    def __init__(self, sold) -> None:
        self._sold = sold

    @property
    def sold(self):
        return self._sold
    
    @sold.setter
    def sold(self, value):
        if value < 0:
            raise ValueError("value cannot be negative.")
        self._sold = value


c = ContBancar(100)
print(c.sold)      # 100
c.sold = 200
print(c.sold)      # 200
# c.sold = -50       # EROARE


class Persoana:
    def __init__(self, nume) -> None:
        self._nume = nume

    @property
    def nume(self):
        return self._nume
    
    @nume.setter
    def nume(self, value):
        if value == '' or len(value) < 2:
            raise ValueError('Value cannot be empty string or less that 2')
        self._nume = value

    @nume.deleter
    def nume(self):
        print("Deleting name...")
        del self._nume

p = Persoana("Sultana")
print(p.nume)
p.nume = "Ana"
del p.nume 

class Temperatura:
    def __init__(self, celsius) -> None:
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Value cannot be less then -273.15')
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9
        
    @celsius.deleter
    def celsius(self):
        print('Deleting temperature')
        del self._celsius

    
        

t = Temperatura(25)
print(t.celsius)        # 25
print(t.fahrenheit)     # 77.0

t.fahrenheit = 212
print(t.celsius)        # 100

del t.celsius

class Angajat:
    def __init__(self, salariu_de_baza) -> None:
        self._salariu_de_baza = salariu_de_baza
    
    @property
    def salariu_baza(self):
        return self._salariu_de_baza
    
    @property
    def salariu_total(self):
            return self._salariu_de_baza + self._salariu_de_baza * 10/100
    
    @salariu_baza.setter
    def salariu_baza(self, value):
        if value < 1000 or value > 100000:
            raise ValueError("TEST")
        self._salariu_de_baza = value

    @salariu_baza.deleter
    def salariu_baza(self):
        print("DELETING..")
        del self._salariu_de_baza


a = Angajat(5000)
print(a.salariu_total)     # 5500.0

a.salariu_baza = 8000
print(a.salariu_total)     # 8800.0

# a.salariu_baza = 500       # EROARE

del a.salariu_baza

