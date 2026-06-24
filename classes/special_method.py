class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay + self.raise_amt)
    
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.pay)
    
    def __add__(self, other):
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())
        
emp_1 = Employee("Alin", "Stefan", 500)
emp_2 = Employee("Madalina", "Luiza", 400)

print(len("test"))
# print(1 + 2)
# print("a" + "b")

print(repr(emp_1))
print(str(emp_1))

# print(int.__add__(1,2))
# print(str.__add__('a', 'b'))

print(emp_1 + emp_2)
print(len(emp_1))


"""
Ce sunt Special / Magic / Dunder Methods?
Sunt metode speciale din Python care încep și se termină cu două liniuțe jos:
__nume__
De aceea se numesc:

dunder methods (double underscore)

magic methods

special methods

Python le folosește automat în anumite situații, fără să le apelezi tu direct.

🎯 De ce există?
Ca să poți controla:

cum se afișează un obiect

cum se compară două obiecte

cum se adună două obiecte

cum se comportă obiectul în len(), print(), str()

cum se iterează peste el

cum se transformă în string

cum se inițializează

Cu alte cuvinte:
👉 îți permit să faci obiectele tale să se comporte ca obiectele built in din Python.
"""