class Employee:

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
       
    @property
    def email(self):
        return '{} {}@email.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    

    @fullname.deleter
    def fullname(self):
        print ('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('John', 'Smith')
emp_1.fullname = 'Alin Stefan'



print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)
del emp_1.fullname

"""
In Python, getters, setters, and deleters manage access to class attributes without
 changing how they are accessed. Handled via the @property decorator, they allow you
to enforce validation or perform computations while maintaining a clean syntax 
(e.g., object.value)

Instead of creating traditional Java-style methods like get_name() or set_name(), 
Python uses built-in decorators.Getter (@property): Retrieves the value of an 
attribute.Setter (@property.setter): Validates or modifies data before saving it
 to a hidden, private variable.Deleter (@property.deleter): Cleans up resources or 
 prevents deletion when the del keyword is used.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # This calls the setter below automatically

    # Getter
    @property
    def age(self):
        return self._age

    # Setter
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    # Deleter
    @age.deleter
    def age(self):
        print("Deleting age...")
        del self._age

# Usage
person = Person("Alice", 30)

# Calls the getter
print(person.age)  # Output: 30

# Calls the setter
person.age = 35 

# Calls the deleter
del person.age


