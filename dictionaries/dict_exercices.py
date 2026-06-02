"""
1. Creează un dicționar

Creează un dicționar cu:

nume
vârstă
oraș

Afișează:

dicționarul complet
numele
orașul
"""
zone = {
    "name": "Alin",
    "age": 26,
    "city": "Visina"
}

print(zone)
print(zone["name"])
print(zone["city"])

"""
2. Adaugă o cheie nouă

Pornind de la:

persoana = {
    "nume": "Alin",
    "varsta": 25
}

Adaugă:

"oras": "Targoviste"
3. Modifică o valoare

Schimbă:

"varsta": 25

în:

"varsta": 26
"""
person = {
    "name": "Madalina",
    "age": 25
}
person["city"] = "Gaesti"
print(person)
person["age"] = 26
print(person)
"""
4. Verifică dacă o cheie există

Folosește:

in

Exemplu:

"nume" in persoana
"""
print("name" in person)

"""
5. Afișează toate cheile
6. Afișează toate valorile
7. Afișează toate perechile cheie-valoare
8. Sterge o cheie
"""
print(person.keys())
print(person.values())
for key, value in person.items():
    print(person)

person.pop('name')
print(person)
del person["age"]
print(person)

"""
9. Catalog elev

Creează:

elev = {
    "nume": "Maria",
    "matematica": 10,
    "romana": 9,
    "engleza": 8
}

Afișează:

numele
nota la matematică
media notelor

"""
elev = {
    "nume": "Maria",
    "matematica": 10,
    "romana": 9,
    "engleza": 8
}
print(elev["nume"])
print(elev["matematica"])
print((elev["engleza"] + elev["matematica"] + elev["romana"])/3)

"""
10. Numără câte chei are dicționarul
"""
print(len(elev))

"""
11. Dicționar cu liste

Creează:

persoana = {
    "nume": "Alin",
    "hobbyuri": ["fotbal", "gaming", "programare"]
}

Afișează:

toate hobby-urile
primul hobby
"""

persoana = {
    "nume": "Alin",
    "hobbyuri": ["fotbal", "gaming", "programare"]
}
print(persoana["hobbyuri"])
print(persoana["hobbyuri"][0])

carte_identiate ={
    "nume": "Sultana",
    "prenume": "Alin",
    "varsta": 26,
    "oras": "Gaesti"
}
for k,v in carte_identiate.items():
    print(k, ":", v)