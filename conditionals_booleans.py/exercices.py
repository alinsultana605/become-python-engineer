"""
1. Major sau minor

Cere vârsta utilizatorului.

Afișează:

Major

sau

Minor
"""

varsta = int(input("Introdu varsta:"))

if varsta >= 18:
    print("Major")
else:
    print("Minor")


"""
Cere un număr.
Afișează:
Pozitiv
sau
Negativ
sau
Zero
"""

numar = int(input("Introdu numarul:"))
if numar > 0:
    print("Pozitiv")
elif numar < 0:
    print("Negativ")
else:
    print("0")

"""
3. Par sau impar
Cere un număr și afișează:
Par
sau
Impar
"""

numar = int(input("Introdu numarul:"))
if numar % 2 == 0:
    print("Par")
else:
    print("Impar")

"""
4. Cel mai mare dintre două numere

Cere două numere.

Afișează numărul mai mare.
"""

nr1 = int(input("Introdu numarul:"))
nr2 = int(input("Introdu numarul:"))

cel_mai_mare = nr1 if nr1>nr2 else nr2
print(cel_mai_mare)


"""
5. Verificare parolă

Cere o parolă.

Dacă are minim 8 caractere:

Parola valida

altfel:

Parola prea scurta
"""

parola = input("Introdu parola:")
verificare_parola = "Parola valida" if len(parola) >=8 else ("Parola prea scurta")
print(verificare_parola)

"""
6. Notă școlară

Cere o notă între 1 și 10.

Afișează:

10 -> Excelent
8-9 -> Foarte bine
5-7 -> Promovat
1-4 -> Respins
"""
nota = int(input("Nota obtinuta: "))

if 1 <= nota <= 10:
    print("Nota valida")
else:
    print("Nota invalida")
    exit()  

if nota == 10:
    print("Excelent")
elif nota in (8, 9):
    print("Foarte Bine!")
elif nota in (5, 6, 7):
    print("Promovat")
else:
    print("Respins")

"""
7. Login simplu

Datele corecte sunt:

username = "admin"
password = "1234"

Cere datele utilizatorului și verifică dacă sunt corecte.
 """
utilizator = input("Introdu usename")
parola = input("Introdu parola")

if utilizator == "admin" and parola == "1234":
    print("Utilizator corect")
else:
    print("Mai incearca")
    
"""
8. Reducere

Cere valoarea cumpărăturilor.

Dacă este peste 100:

Ai reducere 10%

altfel:

Nu ai reducere
"""
valoare_cumparaturi = float(input("Valoare cumparatoru"))
if valoare_cumparaturi > 10:
    print("Ai reducere de 10%")
else:
    print("Nu ai reducere")

"""
9. Acces la eveniment

Poate intra dacă:

are minim 18 ani
are bilet

Afișează:

Acces permis

sau

Acces interzis
"""
varsta = int(input("Introdu varsta: "))
are_bilet = input("Ai bilet? (Da/Nu): ")

if are_bilet == "Da" and varsta >= 18:
    print("Acces permis")
else:
    print("Acces interzis")


"""
10. Mini ATM

Utilizatorul are:

sold = 1000

Cere suma pe care vrea să o retragă.

Dacă are suficienți bani:

Retragere efectuata
Sold ramas: ...

altfel:

Fonduri insuficiente
"""
sold = 1000
suma_retrasa = float(input("Ce suma vrei sa retragi?"))
if suma_retrasa <= sold:
    print("Retragere efectuata")
    print("Sold ramas:", sold - suma_retrasa)
else:
   print("Fonduri insuficiente")