
"""
Cerințe:
Sortează lista alfabetic.

Sortează lista ignorând majusculele.

Sortează lista după lungimea fiecărui nume.

"""
from operator import attrgetter

names = ["Sultana", "ana", "Maria", "george", "Alex"]

li_alpha = sorted(names)
print(li_alpha)

li_names = sorted(names, key = str.lower)

print(li_names)

li_len = sorted(names, key = len)
print(li_len)

"""
Cerințe:
Creează o listă sortată crescător.

Creează o listă sortată descrescător.
"""
nums = (10, 3, 55, 2, 100, 7)

li_nums = sorted(nums, reverse=True)
print(li_nums)
li_nums_false = sorted(nums, reverse=False)
print(li_nums_false)

"""
Cerințe:
Sortează lista după nume.

Sortează lista după vârstă.

Sortează lista mai întâi după vârstă, apoi după nume.
"""

students = [
    ("Sultana", 22),
    ("Ana", 19),
    ("Maria", 25),
    ("George", 22),
]
li_students = sorted(students, key= lambda e: e[0])
print(li_students)

li_students_age = sorted(students, key= lambda e: e[1])
print(li_students_age)

li_students_alpha = sorted(students, key=lambda x: (x[1], x[0]))
print(li_students_alpha)

"""
Cerințe:
Sortează angajații după nume.

Sortează angajații după salariu.

Sortează angajații descrescător după salariu.

Sortează angajații după vârstă, apoi după salariu.

Rezolvă exercițiul 2 folosind attrgetter, nu lambda.
"""
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f"{self.name} - {self.age} - {self.salary}"

employees = [
    Employee("Sultana", 22, 5000),
    Employee("Ana", 19, 3000),
    Employee("Maria", 25, 7000),
    Employee("George", 30, 4500),
]

sort_name = sorted(employees, key = lambda x: x.name)
print(sort_name)
sort_salary = sorted(employees, key = lambda x: x.salary)
print(sort_salary)
sort_salary_reversed = sorted(employees, key=lambda x: x.salary, reverse=True)
print(sort_salary_reversed)
sort_salary_age = sorted(employees, key= lambda x : (x.age, x.salary))
print(sort_salary_age)
sort_second = sorted(employees, key = attrgetter('salary'))
print(sort_second)

"""
Cerințe:
Sortează lista ignorând majusculele.

Sortează lista după ultimul caracter din fiecare cuvânt.

Sortează lista după numărul de vocale din fiecare cuvânt.
"""
words = ["python", "Sorting", "corey", "SCHAFER", "tutorial"]


li_words = sorted(words, key=str.lower)
print(li_words)

li_last_char = sorted(words, key=lambda w: w[-1].lower())
print(li_last_char)

def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for c in word if c in vowels)

li_vowels = sorted(words, key=count_vowels)
print(li_vowels)