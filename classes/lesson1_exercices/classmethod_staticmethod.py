class Employee:

    raise_amount = 1.04
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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Alin', 'Sultana', 5000)
emp_2 = Employee('Test', 'User', 6000)

Employee.set_raise_amt(1.05)
emp_1.set_raise_amt(1.05)

emp_str_1 = 'Alin-Sultana-12345'
emp_str_2 = 'Madalina-Sultana-77777'
emp_str_3 = 'Sultana-Bianca-1772'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.first)
print(new_emp_1.pay)

import datetime
my_date = datetime.date(2016,7, 10)
print(Employee.is_workday(my_date))


"""
A classmethod is a method that receives the class as its first argument instead of the instance.
It is used when you want to access or modify class-level data or create alternative constructors.

First parameter is always cls

Works on the class, not on individual objects

Example use: updating class variables, creating objects in a special way.

4. @staticmethod — Definition
A staticmethod is a method that does not receive self or cls.
It behaves like a normal function but is placed inside the class because it is logically related to the class.

Does not access instance data

Does not access class data

Pure utility/helper function

Example use: calculations, validations, formatting functions.
"""