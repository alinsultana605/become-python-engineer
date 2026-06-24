class Employee:
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

# emp_1 = Employee()
# emp_2= Employee()
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)
print(Employee.fullname(emp_1))
"""
Print both of these are employee objects and they re both unique
<__main__.Employee object at 0x00000210E71986E0>
<__main__.Employee object at 0x00000210E719C550>
different locations in memory
"""
# print(emp_1)
# print(emp_2)

# emp_1.first = 'Corey'
# emp_1.first = 'Schafer'
# emp_1.email = 'Corey.schafer@company.com'
# emp_1.pay = 5000


# emp_2.first = 'Test'
# emp_2.first = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 5000

# print(emp_1.email) # Corey.schafer@company.com
# print(emp_2.email) # Test.User@company.com

# print('{} {}'.format(emp_1.first, emp_2.last))
# print(emp_2.fullname())

"""
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.

Create a Class
To create a class, use the keyword class:

ExampleGet your own Python Server
Create a class named MyClass, with a property named x:

class MyClass:
  x = 5

  Create Object
Now we can use the class named MyClass to create objects:

Example
Create an object named p1, and print the value of x:

p1 = MyClass()
print(p1.x)

Delete Objects
You can delete objects by using the del keyword:

Example
Delete the p1 object:

del p1
"""

# Create a class
class Person:
   def __init__(self, name, age):
       self.name = name
       self.age = age
   def greet(self):
       return 'Hello my name is' , self.name




# Create an object
p1 = Person('John', 36)
# Call the greet method
p1.greet()

