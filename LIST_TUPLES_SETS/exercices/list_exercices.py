"""
1. Creează o listă

Creează o listă cu 5 fructe și afișează:

lista completă
primul element
ultimul element
"""

fructe = ["mar", "para", "banana", "kiwi"]
print(fructe)
print(fructe[0])
print(fructe[-1])


"""
2. Modifică un element

Având:

numere = [1, 2, 3, 4]

schimbă 3 în 10.
"""
numere = [1, 2, 3, 4]
numere[2] = 10
print(numere)


"""
3. Adaugă elemente

Folosește:

append()

Adaugă:

un nume
un număr
un oraș

într-o listă goală.
"""

list_element = []
list_element.append("Alin")
list_element.append(2)
list_element.append("Barcelona")

"""
4. Șterge un element

Având:

culori = ["rosu", "verde", "albastru"]

șterge:

"verde"
"""
culori = ["rosu", "verde", "albastru"]
culori.remove("verde")
print(culori)

"""
5. Lungimea listei

Afișează câte elemente are lista.

Folosește:

len()
"""
print(len(culori))

"""
6. Parcurge lista

Având:

numere = [1, 2, 3, 4, 5]

afișează fiecare element folosind:

for
"""
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

"""
7. Suma numerelor din listă

Având:

numere = [10, 20, 30]

afișează suma totală.

Hint:

sum()
"""
numbers_sum = [10, 20, 30]
print(sum(numbers_sum))

"""
8. Găsește maximul și minimul

Pentru o listă de numere afișează:

cel mai mare număr
cel mai mic număr

Hints:

max()
min()
"""
print(max(numbers_sum))
print(min(numbers_sum))

"""
9. Verifică dacă un element există în listă

Exemplu:

"mere" in fructe
"""
fructe = ["mere", "pere", "nuci", "kiwi"]
print("mere" in fructe)

"""
10. Elimină duplicatele

Exemplu:

[1,1,2,2,3]

→

[1,2,3]
"""
duplicates = [1,1,2,2,3]
print(list(set(duplicates)))

"""
11. Sortează lista

Folosește:

sort()

și apoi:

reverse()
"""
duplicates.sort()
print(duplicates)
duplicates.reverse()
print(duplicates)

"""
12. Inversează lista

Fără reverse() dacă poți 😄

Hint:

[::-1]
"""
print(duplicates[::-1])