"""
Perfect. Tuple-urile sunt foarte asemănătoare cu listele, dar au o diferență foarte importantă:

💡 Diferența principală
Listă
lista = [1, 2, 3]

✔️ se poate modifica

Tuple
tuplu = (1, 2, 3)

❌ NU se poate modifica

Tuple = date fixe/constante.
"""

"""
1. Creează un tuple

Creează un tuple cu:

nume
vârstă
oraș

și afișează:

tuple-ul complet
primul element
ultimul element
"""
elemente = ("nume", "varsta", "oras")
print(elemente)
print(elemente[0])
print(elemente[-1])

"""
2. Află lungimea tuple-ului

Folosește:

len()
"""
print(len(elemente))

"""
3. Verifică dacă un element există

Exemplu:

"mere" in fructe
"""

print("mere" in elemente)

"""
4. Parcurge tuple-ul

Având:

numere = (1, 2, 3, 4, 5)

afișează fiecare element cu:

for
"""
for element in elemente:
    print(element)

"""
5. Numără de câte ori apare un element

Folosește:

count()

Exemplu:

(1,1,2,3,1)
"""

print(elemente.count("varsta"))

"""
6. Găsește poziția unui element

Folosește:
"""

print(elemente.index("varsta"))

"""
7. Încearcă să modifici un tuple

Exemplu:

numere = (1, 2, 3)

numere[0] = 10

👉 vezi ce eroare primești și încearcă să înțelegi de ce.
"""
# numere = (1, 2, 3)

# numere[0] = 10
# print(numere) ## 'tuple' object does not support item assignment, because tuples is immutable

"""
8. Transformă tuple în listă

Având:

numere = (1, 2, 3)

transformă-l în listă folosind:

list()

apoi adaugă un element nou.
"""

numere = (1, 2, 3)
transform = list(numere)
transform.append(4)
print(transform)