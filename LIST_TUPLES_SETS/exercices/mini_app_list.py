"""
13. Mini list manager

Creează un program unde utilizatorul poate:

adăuga elemente
șterge elemente
afișa lista
"""
elemente = []
adauga = input("Adauga elementele urmatoar:")
elemente.append(adauga)
print(elemente)
sterge = input("Sterge elementele urmatoar:")
if sterge in elemente:
    elemente.remove(sterge)

print(elemente)