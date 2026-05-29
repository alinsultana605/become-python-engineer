"""
Set-urile sunt foarte utile în Python și au câteva caracteristici importante.

💡 Ce este un set?

Un set:

NU păstrează duplicate
NU are ordine fixă
este folosit pentru elemente unice
numere = {1, 2, 3, 3, 2}

print(numere)
{1, 2, 3} 👉 duplicatele dispar automat.
"""

"""
1. Creează un set

Creează un set cu:

5 numere

Afișează set-ul.
"""

numere = {1,2,3, 4, 5}
print(numere)

"""
2. Adaugă un element

Folosește:

add()
"""
numere.add(6)
print(numere)

"""
3. Șterge un element

Folosește:

remove()
"""
numere.remove(2)
print(numere)

"""
4. Verifică dacă un element există

Exemplu:

3 in numere
"""
print(3 in numere)

"""
5. Elimină duplicatele dintr-o listă

Exemplu:

[1,1,2,2,3,4]

→ transformă în:

{1,2,3,4}
"""

duplicates = [1,1,2,2,3,4]
print(set(duplicates))

"""
6. Află lungimea set-ului

Folosește:

len()
"""

print(len(numere))

"""
 Parcurge set-ul

Folosește:

for
"""
for numar in numere:
    print(numar)


"""
8. Diferența dintre listă și set

Creează:

lista = [1,1,2,2,3]
setul = {1,1,2,2,3}

Afișează-le și observă diferența.
"""

lista = [1,1,2,2,3]
setul = {1,1,2,2,3}
print(lista)
print(setul)
## List contains duplicates and it s ordered, and set not contain duplicates and it s use for fix element

"""
9. Union

Având:

a = {1, 2, 3}
b = {3, 4, 5}

unește set-urile folosind:
"""
a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print(c)
print(a.intersection(b))

"""
11. Verifică dacă două liste au elemente comune

Exemplu:

[1,2,3]
[3,4,5]
"""
lista_1=[1,2,3]
lista_2=[3,4,5]

print(len(set(lista_1).intersection(set(lista_2))))
print(bool(set(lista_1).intersection(set(lista_2))))
print(set(lista_1).intersection(set(lista_2)))