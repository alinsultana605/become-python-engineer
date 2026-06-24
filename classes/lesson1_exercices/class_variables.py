class Employee:

    raise_amount = 1.05
    num_of_emps = 0
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Alin', 'Sultana', 5000)
emp_2 = Employee('Test', 'User', 6000)
emp_3 = Employee('Tests', 'Users', 6000)

# # print(emp_1.pay)
# # emp_1.apply_raise()
# # print(emp_1.pay)

# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)

# # print(emp_1.__dict__)
# # print(Employee.__dict__)
# Employee.raise_amount = 1.06
# print(Employee.raise_amount)
print(Employee.num_of_emps)

""""
A class variable is a variable that belongs to the class itself, not to individual objects.
All objects created from that class share the same value of the class variable.
🧩 Class variables vs instance variables
✔ Class variables
Shared by all instances

Defined inside the class, but outside any method

✔ Instance variables
Unique for each object

Defined inside __init__ using self

class Student:
    school = "National College"   # class variable

    def __init__(self, name):
        self.name = name          # instance variable

s1 = Student("Ana")
s2 = Student("Mihai")

print(s1.school)
print(s2.school)

National College
National College

📌 Useful example: counting objects
python
class Counter:
    total = 0   # class variable

    def __init__(self):
        Counter.total += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()

print(Counter.total)
Output:

Code
3
"""