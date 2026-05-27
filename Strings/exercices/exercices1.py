"""
1.
Creează o variabilă nume și afișează:

lungimea stringului
prima literă
ultima literă
stringul cu litere mari
"""

nume = 'Salut lume'

print(len(nume))
print(nume[0])
print(nume[-1])
print(nume.upper())

"""
2.
Având:
mesaj = "Salut lume"
afișează:
Salut
lume
folosind slicing.
"""

mesaj = 'Salut lume'

print(mesaj[:5])
print(mesaj[6:])

"""
3.
Transformă:
text = "python"

în:

"Python"
"""
text = 'python'
new_text = text.replace('python', 'Python')
print(new_text)
"""
Verifică dacă un string introdus de utilizator începe cu "https".
"""

text = "https://google.com"
print(text.startswith("https"))

"""
Cere utilizatorului nume și prenume și afișează:
Prenume: X
Nume: Y
Initiale: X.Y
"""
# prenume = input ("Prenume:")
# nume = input("Nume:")
# print(f"Prenume: {prenume}")
# print(f"Nume: {nume}")
# print(f"Initiale: {prenume[0]}.{nume[0]}")

"""
Având:
email = "test@gmail.com"

extrage:

username-ul
domeniul
"""
email = "test@gmail.com"
print(email[0:4])
print(email[5:])

"""
Inversează un string folosind slicing.

Exemplu:

"python" -> "nohtyp"
"""
test = 'python'
print(test[::-1])


"""
Verifică dacă un cuvânt este palindrom.

Exemple:

ana → True
radar → True
python → False
"""
cuvant_1 = "ana"
cuvant_2 = "radar"
cuvant_3 = 'python'
cuvant = cuvant_1[::-1]
print(cuvant == cuvant_1)
cuvant_22 = cuvant_2[::-1]
print(cuvant_22 == cuvant_2)
cuvant_33 = cuvant_3[::-1]
print(cuvant_33 == cuvant_3)

cuvinte = [cuvant_1, cuvant_3, cuvant_2]
for cuvant in cuvinte:
    print(cuvant == cuvant[::-1])


