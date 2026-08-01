"""
🔥 Esența lecției: de ce folosim try / except?
Pentru că erorile sunt inevitabile.
Dar nu vrei ca programul tău să se oprească brusc.

Vrei să spui:

„Dacă apare o eroare, nu te opri. Rezolv-o sau trateaz-o.”
🧩 Structura de bază
try:
    # cod care poate produce o eroare
except:
    # cod care rulează dacă apare eroarea

try:
    x = int("abc")
except:
    print("Nu pot converti în număr")

🧩 Try / Except cu tipuri de erori
Corey insistă pe asta: nu folosi except generic.
Folosește tipuri specifice:
try:
    x = int("abc")
except ValueError:
    print("Ai introdus un text, nu un număr")
🧩 Try / Except / Else / Finally
try:
    # cod care poate produce eroare
except:
    # dacă apare eroare
else:
    # dacă NU apare eroare
finally:
    # rulează ORICUM
try:
    f = open("test.txt")
except FileNotFoundError:
    print("Fișierul nu există")
else:
    print("Fișier deschis cu succes")
finally:
    print("Operațiune încheiată")
🧩 Capturarea erorii în variabilă

try:
    1 / 0
except ZeroDivisionError as e:
    print("Eroare:", e)

Eroare: division by zero

🧩 Try / Except cu mai multe except-uri
try:
    x = int("abc")
    y = 1 / 0
except ValueError:
    print("Conversie invalidă")
except ZeroDivisionError:
    print("Împărțire la zero")

🧩 Try / Except în operații cu fișiere
try:
    with open("data.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("Fișierul nu a fost găsit")

🧩 Try / Except în conversii de input
try:
    age = int(input("Introdu vârsta: "))
except ValueError:
    print("Te rog introdu un număr valid")

🧩 Try / Except în lucrul cu dicționare
person = {"name": "Sultana"}

try:
    print(person["age"])
except KeyError:
    print("Cheia 'age' nu există")

"""
try:
    f = open('corrupt_file.txt')
    # if f.name == 'corrupt_file.txt':
    #     raise Exception
    # var = bad_var
except FileNotFoundError as e:
    print(e)

except Exception as e:
    print("Error!")
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")