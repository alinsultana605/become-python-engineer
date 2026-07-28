"""
1. Creează o funcție care folosește o variabilă locală
Scrie o funcție show_local() care definește o variabilă x = "local" și o afișează.
"""
def show_local():
    x = 'local'
    print(x)

show_local()

"""
2. Creează două funcții nested și folosește variabila din Enclosing Scope
Scrie o funcție outer() care are x = "outer".
În interior, definește inner() care afișează x.

Apelează outer().
"""
def outer():
    x = 'outer'
    def inner():
        print(x)
    inner()


outer()

"""
3. Folosește o variabilă globală într-o funcție
Definește x = "global" în afara funcțiilor.
Scrie o funcție show() care afișează x.
"""

y = 'global'

def show():
    print(y)

show()

"""
4. Suprascrie o variabilă globală folosind global
Definește x = 10.
Scrie o funcție change() care folosește global x și setează x = 99.
Apelează funcția și afișează x.
"""

x = 10
def change():
    global x
    x = 99
    print(x)
change()

"""
Creează o funcție nested care modifică variabila din Enclosing Scope cu nonlocal
"""

def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "changed"
    inner()
    print(x)
outer()

len = 100

def show_len():
    print(len)

show_len()

"""
7. Demonstrează ordinea LEGB
Scrie codul:

x = "global"

în outer(), definește x = "outer"

în inner(), definește x = "inner" și afișează-l

apoi afișează x din outer()

apoi afișează x global
"""

x = 'global'

def outer():
    x = 'outer'
    def inner():
        x = 'inner'
        print(x)
    inner()
    print(x)
outer()
print(x)


"""
8. Creează o funcție care încearcă să folosească o variabilă nedefinită
Scrie o funcție test() care încearcă să afișeze y, fără să existe y.
"""

def test():
    print(y)

test()

"""
9. Creează un exemplu în care o variabilă locală ascunde o variabilă globală
Definește x = "global"  
Scrie o funcție care definește x = "local" și o afișează.
"""

x = 'global'

def define():
    x = 'local'   # variabilă locală, ascunde pe cea globală
    print(x)

define()
print(x)

"""
10. Creează un exemplu în care nonlocal este necesar pentru a modifica o variabilă din funcția părinte
"""

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
    increment()
    increment()
    increment()
    print(count)
counter()
