# nume = input("Numele:")
# anul_nasterii = input("An nastere:")

# username = nume + anul_nasterii

# print(username)


parola = input("Introdu parola:")

are_lungime = len(parola) >= 8
are_cifra = any(text.isdigit() for text in parola)
litera_mare = any(text.isupper() for text in parola)

if are_lungime and are_cifra and litera_mare:
    print("Parola este ok")

else:
    print("Try again")


    ##Snake case

    text = "Salut Lume Python"
    new_text = text.lower().replace(' ', "_")
    print(new_text)


    propozitie = "Python este greu"
    new_prop = propozitie.replace("greu", "****")
    print(new_prop)


    """
    Creează un mini program care:
cere utilizatorului un text
afișează:
numărul de caractere
numărul de cuvinte
textul cu majuscule
textul inversat
dacă textul începe cu vocală
    """

    text = input("Introdu textul: ")

print("Caractere:", len(text))
print("Cuvinte:", len(text.split()))
print("Majuscule:", text.upper())
print("Invers:", text[::-1])

vocale = "aeiouAEIOU"
print("Incepe cu vocala:", text[0] in vocale)