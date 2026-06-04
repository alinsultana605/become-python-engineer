"""
1.

Afișează numerele de la 1 la 10.

2.

Afișează numerele de la 10 la 1.

3.

Afișează toate numerele pare între 1 și 20.

4.

Afișează toate numerele impare între 1 și 20.
"""

for x in range(0,11):
    print(x)

for i in range (11, 0, -1):
    print(i)

for i in range(1, 20):
    if i % 2 == 0:
        print(i)
    else:
        continue

for i in range(1, 20):
    if i % 2 == 0:
        continue
    else:
        print(i)

"""
5.

Parcurge lista:

fructe = ["mar", "para", "banana", "kiwi"]

și afișează fiecare element pe linie separată.

6.

Calculează suma numerelor din lista:

numere = [10, 20, 30, 40, 50]

fără să folosești sum().

7.

Calculează media numerelor din lista:

numere = [5, 7, 9, 10]
8.

Afișează doar elementele care conțin litera "a":

fructe = ["mar", "kiwi", "banana", "para"]
9.

Numără câte elemente sunt într-o listă fără să folosești len().

10.

Găsește cel mai mare număr din:

numere = [4, 7, 2, 10, 5]

fără max().
"""

# fructe = ["mar", "para", "banana", "kiwi"]

# for fruct in fructe:
#     print(fruct)

numere = [10, 20, 30, 40, 50]

suma = 0

for numar in numere:
    suma += numar

print(suma)
suma = 0
media = 0
numere = [5, 7, 9, 10]
for numar in numere:
    suma += numar
media = suma / len(numere)
print(media)

fructe = ["mar", "kiwi", "banana", "para"]

for fruct in fructe:
    if "a" in fruct:
        print(fruct)

fructe = ["mar", "kiwi", "banana", "para"]
count = 0
for _ in fructe:
    count +=1
    print("Numar elemente:", count)

numere = [4, 7, 2, 9, 5]
mare = numere[0]
for numar in numere:
    if numar > mare:
        mare = numar
print("Cel mai mare element", mare)

"""
11.

Afișează numerele de la 1 la 5 folosind while.

12.

Afișează numerele de la 5 la 1 folosind while.

13.

Cere utilizatorului un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).

14.

Cere utilizatorului să introducă parola.

Programul continuă să ceară parola până când utilizatorul introduce:

python123
15.

Cere utilizatorului numere și calculează suma lor.

Programul se oprește când utilizatorul introduce:
"""
x = 0
while x < 5:
    x += 1
    print(x) 

numar = 5
while numar >= 1:
    print(numar)
    numar -= 1
    

numar = int(input("Introdu un număr: "))

i = 1
while i <= 10:
    print(numar, "x", i, "=", numar * i)
    i += 1

parola = (input("Introdu parola"))

while parola != "python123":
    print("Parola Gresita")
    parola = input("Introdu parola")
print("Parola corecta")


while True:
    nr1 = int(input("Introdu primul număr: "))
    nr2 = int(input("Introdu al doilea număr: "))

    if nr1 == 0 or nr2 == 0:
        print("Ați introdus valoarea 0. Programul se oprește.")
        break

    print(nr1, "+", nr2, "=", nr1 + nr2)


"""
Exerciții cu Break și Continue
16.

Afișează numerele de la 1 la 20.

Oprește bucla când ajungi la 12.

17.

Afișează numerele de la 1 la 20.

Sari peste numărul 7.

18.

Afișează toate numerele între 1 și 30 care NU sunt divizibile cu 3.

19.

Parcurge lista:

nume = ["Ana", "Maria", "Alin", "George"]

Oprește-te când găsești "Alin".

20.

Parcurge lista:

nume = ["Ana", "", "Maria", "", "George"]

Afișează doar numele ne-goale.
"""

for x in range(1, 20):
    if x==12:
        break
    print(x)

    
for i in range(1, 20):
    if i==7:
        continue
    print(i)

for i in range (1, 30):
    if i % 3 == 0:
        print(i)

nume = ["Ana", "Maria", "Alin", "George"]
for num in nume:
    if num == "Ana":
        break
    print(num)

nume = ["Ana", "", "Maria", "", "George"]
for num in nume:
    if num != "":
        print(num)

while True:
    nr1 = int(input("Introdu primul număr: "))

    if nr1 == 8:
        print("Ați ghicit numarul.")
        break

    print("Mai incearca")


sold = 1000

while True:
    print("\n--- MINI ATM ---")
    print("1. Vezi sold")
    print("2. Retrage bani")
    print("3. Iesire")

    optiune = input("Alege o opțiune: ")

    if optiune == "1":
        print("Soldul tău este:", sold)

    elif optiune == "2":
        suma = int(input("Introdu suma de retras: "))
        if suma <= sold:
            sold -= suma
            print("Ai retras", suma, "lei. Sold rămas:", sold)
        else:
            print("Fonduri insuficiente!")

    elif optiune == "3":
        print("La revedere!")
        break

    else:
        print("Opțiune invalidă!")

produse = []

while True:
    print("\n--- Shopping List ---")
    print("1. Adauga produse")
    print("2. Stop")

    optiune = input("Alege o optiune:")
    
    if optiune == "1":
        produsul_adaugat = input("Adauga produsul")
        produse.append(produsul_adaugat)
        print("Ai adaugat", produsul_adaugat)
    elif optiune == "2":
        print("Aceasta este lista finala de cumparaturi:", produse)
        break
    else:
        print("Opțiune invalidă!")