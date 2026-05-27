"""
1. Suma a două numere

Cere două numere și afișează suma lor.

2. Pentru două numere afișează:

suma
scăderea
înmulțirea
împărțirea
"""

a = 2 
b = 3
print (a + b)
print(a - b)
print (a / b)
print( a * b)


"""
3. Află tipul variabilei

Folosește:

type()

Testează:

10
10.5
"10"
"""

a = 10
b = 1.5
c = "10"
list = [a, b, c]
for element in list:
    print(type(element))

print(str(a))
print(int(b))
print(float(c))

"""
5. Număr par sau impar

Verifică dacă un număr este:

par
impar
"""

numar = int(input("inrodu numar"))
if numar % 2 == 0:
    print("este par")
else:
    print("nu este")


    """
    6. Media a 3 numere

Cere 3 numere și afișează media lor.


    """

a = 10
b = 9
c = 7

media = a + b + c
print(media / 3)

"""
7. Puterea unui număr

Cere:

un număr
o putere
"""

a = 2 ** 3
print(a)

"""8. Conversie Celsius → Fahrenheit"""
C = 34

F = C * 9 /5 + 32
print (F)
