"""
Exercițiul 1
Scrie un program care cere un număr de la utilizator și tratează eroarea dacă acesta introduce text.
"""
try:
    age = int(input("Introdu varsta: "))

except ValueError:
    print("Trebuie introdus un numar valid")

"""
Exercițiul 2
Deschide un fișier. Dacă nu există, afișează un mesaj prietenos.
"""
try:
    f = open("test.txt")
except FileNotFoundError:
    print('Fisierul nu exista')

"""
Exercițiul 3
Fă o funcție care împarte două numere și tratează eroarea de împărțire la zero.
"""
def division():
    a = int(input("Introdu numarul a:"))
    b = int(input("Introdu numarul b:"))
    return a/b

try:
    division()
except ZeroDivisionError:
    print("Impartire la 0")

"""
Exercițiul 4
Folosește else și finally într-un exemplu cu fișiere.
"""
try:
    f = open("corrupt_file.txt")
except FileNotFoundError:
    print('Fisierul nu exista')
else:
    print("Fisierul a fost gasit")
finally:
    print("Operatiune terminata")

"""
Exercițiul 5
Folosește două except-uri diferite: ValueError și ZeroDivisionError.
"""


try:
    division()
except ZeroDivisionError:
    print("Impartire la 0")
except ValueError:
    print("Trebuie introdus un numar valid")

"""
Exercițiul 6
Scrie un program care încearcă să acceseze o cheie dintr-un dicționar și tratează KeyError.
"""
person = {'Name': 'Alin',}
try:
    print(person['Test'])
except KeyError:
    print("Cheia nu a fost gasita")