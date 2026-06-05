"""
Anatomia unei funcții
def salut():
    print("Salut!")
def = definește o funcție
salut = numele funcției
() = parametri (momentan goi)
: = începe blocul funcției

Funcție cu parametri

Poți trimite date către funcție.

def salut(nume):
    print("Salut", nume)

Apel:

salut("Alin")

Output:

Salut Alin

Mai mulți parametri
def aduna(a, b):
    print(a + b)

Apel:

aduna(5, 7)

Output:

12

Return

Foarte important.

Până acum afișam rezultatul.

Mai util este să-l returnăm:

def aduna(a, b):
    return a + b

Apel:

rezultat = aduna(5, 7)

print(rezultat)

Output:

12
Diferența dintre print și return
Cu print
def aduna(a, b):
    print(a + b)

Afișează rezultatul.

Cu return
def aduna(a, b):
    return a + b

Îți dă rezultatul înapoi ca să îl poți folosi.

Exemplu real
def este_major(varsta):
    return varsta >= 18

Apel:

print(este_major(20))

Output:

True
"""

"""
Primele exerciții
1.

Creează o funcție:

salut()

care afișează:

Salut Python
2.

Creează o funcție:

afiseaza_nume(nume)

care afișează numele primit.

3.

Creează o funcție:

aduna(a, b)

care afișează suma.

4.

Creează o funcție:

scade(a, b)

care returnează diferența.

5.

Creează o funcție:

este_par(numar)

care returnează:

True

sau

False
6.

Creează o funcție:

este_major(varsta)

care returnează:

True

dacă vârsta este minim 18.

7.

Creează o funcție:

maxim(a, b)

care returnează numărul mai mare.

8.

Creează o funcție:

lungime_text(text)

care returnează numărul de caractere.

9.

Creează o funcție:

media(lista)

care returnează media numerelor din listă.

10.

Creează o funcție:

este_palindrom(cuvant)

care returnează:

True

sau

False
"""

# def salut():
#     print("Salut Python")

# salut()

def afiseaza_nume(nume):
    print(nume)

afiseaza_nume("Alin")

def aduna (a,b):
    return (a + b)

print(aduna(1, 2))


def scade (a,b):
    return (a - b)

print(scade(1, 2))

def este_par(numar):
    if numar % 2 == 0:
        return True
    else:
        return False

print(este_par(2))

def este_major(varsta):
    if varsta >=18:
        return True
    else:
        return False
    
print(este_major(17))

def maxim(a,b):
    return max(a,b)

print(maxim(3,2))

def lungime_text(text):
    return len(text)

print(lungime_text("alin"))


def media (lista):
    return sum(lista) / len(lista)

print(media([10, 8, 9]))

def palindorm(cuvant):
    if cuvant == cuvant[::-1]:
        return True
    else:
        return False

print(palindorm("cojoc"))

"""
Exerciții - Functions (Nivel 2)
1. Parametru implicit

Creează funcția:

def salut(nume="Utilizator"):

Apeluri:

salut()
salut("Alin")

Output:

Salut Utilizator
Salut Alin
2. Calculator simplu

Creează funcția:

def calculator(a, b):

Afișează:

suma
diferența
produsul
împărțirea
3. Funcție care verifică dacă un număr este pozitiv
def este_pozitiv(numar):

Returnează:

True

sau

False
4. Funcție care primește o listă
def afiseaza_lista(lista):

și afișează fiecare element.

Exemplu:

afiseaza_lista(["mar", "para", "kiwi"])
5. Funcție care calculează suma unei liste

Fără sum().

def suma_lista(lista):
6. Funcție care calculează maximul unei liste

Fără max().

def maxim_lista(lista):
7. Funcție care numără vocalele
def numara_vocale(text):

Exemplu:

numara_vocale("programare")

Rezultat:

4
8. Funcție care inversează un text
def inverseaza(text):

Exemplu:

inverseaza("python")

Rezultat:

nohtyp
9. Funcție care verifică dacă un element există într-o listă
def exista(lista, element):

Exemplu:

exista([1,2,3], 2)

Rezultat:

True
10. Funcție care apelează altă funcție

Creează:

def este_par(numar):

și apoi:

def afiseaza_rezultat(numar):

care folosește este_par() și afișează:

Numarul este par

sau

Numarul este impar
Mini Challenge
11. Student Manager

Creează funcții:

adauga_nota(lista, nota)
media_note(lista)
nota_maxima(lista)

Folosește-le pe lista:

note = [10, 8, 9]
"""
def salut(nume="Utilizator"):
    return nume
print(salut("Alin"))

def calculator(a,b):
    print("Suma", a+b)
    print("Diferenta", a-b)
    print("Impartire", a/b)
    print("Inmultire", a * b)
    
calculator(1,2)

def este_pozitiv(numar):
    if numar > 0:
        return True
    
print(este_pozitiv(2))

def afiseaza_lista(lista):
    return lista

print(afiseaza_lista(["mar", "para", "kiwi"]))



def suma_lista(lista):
    suma = 0
    for numar in lista:
        suma += numar 
    return suma