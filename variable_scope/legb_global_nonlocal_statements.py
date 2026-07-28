"""
LEGB
Local, Enclosing, Global, Built-in
"""
# import builtins

# print(dir(builtins))

# def my_min():
#     pass
#
# m = min([5,1,4,2,3])
# print(m)
#
# # x = "global x"
# def test(z):
#     # global x
#     x = "local x"
#     # print(y)
#     print(z)
#
# test('local z')
# # print(z)

def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()

"""
1. Ce este “scope” în Python?
Scope = zona în care o variabilă există și poate fi folosită.

Python are 4 niveluri de scope, iar ordinea în care caută variabilele este:

LEGB
L → Local

E → Enclosing

G → Global

B → Built‑in

Python caută variabilele în această ordine, de sus în jos.
🔹 2. L — Local Scope
Variabilele definite în interiorul unei funcții.

def func():
    x = 10   # local
    print(x)
x există doar în func().

🔹 3. E — Enclosing Scope
Variabilele din funcția părinte (în funcții nested).

def outer():
    x = "outer"
    def inner():
        print(x)   # îl caută în enclosing
    inner()
inner() nu are x, deci îl caută în outer().

🔹 4. G — Global Scope
Variabile definite în fișier, în afara funcțiilor.
x = "global"

def func():
    print(x)
🔹 5. B — Built‑in Scope
Funcțiile Python deja existente:

len

print

sum

range

etc.

Dacă nu găsește variabila în L, E, G, o caută în Built‑ins.

🔥 6. Cum caută Python variabilele?
Exact în această ordine:

Local → Enclosing → Global → Built‑in

Dacă nu o găsește → NameError.

x = 10

def func():
    x = 20   # local, nu modifică globalul

func()
print(x)
Output:

Code
10
🔥 8. global — modifică variabila globală
python
x = 10

def func():
    global x
    x = 20

func()
print(x)
Output:

Code
20
🔥 9. nonlocal — modifică variabila din Enclosing Scope
Folosit doar în funcții nested.

python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner changed"
    inner()
    print(x)

outer()
Output:

Code
inner changed

| Nivel | Unde caută? |
| --- | --- |
| **L — Local** | în funcția curentă |
| **E — Enclosing** | în funcția părinte |
| **G — Global** | în fișier |
| **B — Built‑in** | funcții Python |
"""