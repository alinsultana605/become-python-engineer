"""
🎯 1. Ce înseamnă sortarea în Python (conceptual)?
Sortarea este procesul prin care Python rearanjează elementele unei colecții (listă, tuplu, obiecte) într-o anumită ordine:

ordine alfabetică

ordine numerică

ordine inversă

ordine bazată pe o anumită proprietate (de ex. user.age)

ordine custom, definită de tine

Python oferă două mecanisme principale:

✔ list.sort()
modifică lista în loc

funcționează doar pe liste

nu returnează nimic (None)

✔ sorted(iterable)
funcționează pe orice iterabil (listă, tuplu, set, dict keys)

returnează o nouă listă sortată

nu modifică originalul

🎯 2. Parametrii importanți: key și reverse
✔ reverse=True
Inversează ordinea sortării.

✔ key=function
Aici e magia.
key spune lui Python după ce criteriu să sorteze.

Exemple de funcții folosite ca key:

len → sortează după lungime

str.lower → sortează ignorând majusculele

lambda x: x.age → sortează obiecte după atributul age

lambda x: x['name'] → sortează dicționare după cheie

🎯 3. Cum sortează Python intern?
Python folosește algoritmul Timsort, un hibrid între merge sort și insertion sort.

Avantaje:

foarte rapid pe date reale

stabil (nu schimbă ordinea elementelor egale)

eficient pentru liste deja parțial sortate
"""

li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li, reverse=True)

print('Sorted Variables:\t', s_li)

li.sort(reverse=True)

print('Original Variables:\t', li)

tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)

# tup.sort() error
s_tup = sorted(tup)

print('Tuple\t', s_tup)

di = {'name': 'Alin', 'job':'programming', 'age':None, 'os': 'Windows'}
s_di = sorted(di)
print('Dict\t', s_di)

negative_list = [-6, -5, -4, 1, 2, 3]
n_list = sorted(negative_list, key=abs)
print(n_list)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self) -> str:
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

e1 = Employee('Alin', 13, 10000 )
e2 = Employee('Madalina', 22, 5500)
e3 = Employee('Popescu', 25, 7600)

employees = [e1, e2, e3]

# def e_sort(emp):
#     return emp.salary
s_employee = sorted(employees, key = lambda e: e.name, reverse=True)
print(s_employee)

