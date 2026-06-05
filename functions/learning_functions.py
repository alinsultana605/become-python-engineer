def hello_func():
    pass

print(hello_func) # location in memory <function hello_func at 0x000001B28DAEBE20>
print(hello_func())# None

def hello_function(greeting, name = 'You'):
    return '{}, {} Function'.format(greeting, name)

hello_function('Hi')

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}
print(hello_function('Hi', name = 'Alin'))


"""
*args and **kwargs
By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.
*args and **kwargs allow functions to accept a unknown number of arguments.

Arbitrary Arguments - *args
If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly:

ExampleGet your own Python Server
Using *args to accept any number of arguments:

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

What is *args?
The *args parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments:

Accessing individual arguments from *args:

def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")

Using *args with Regular Arguments
You can combine regular parameters with *args.

Regular parameters must come before *args:

Example
def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")
In this example, "Hello" is assigned to greeting, and the rest are collected in names.



Arbitrary Keyword Arguments - **kwargs
If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly:
Example
Using **kwargs to accept any number of keyword arguments:

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")
What is **kwargs?
The **kwargs parameter allows a function to accept any number of keyword arguments.

Inside the function, kwargs becomes a dictionary containing all the keyword arguments:

Example
Accessing values from **kwargs:

def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")
Using **kwargs with Regular Arguments
You can combine regular parameters with **kwargs.

Regular parameters must come before **kwargs:

Example
def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


Combining *args and **kwargs
You can use both *args and **kwargs in the same function.

The order must be:

regular parameters
*args
**kwargs
Example
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

Unpacking Arguments
The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.

Unpacking Lists with *
If you have values stored in a list, you can use * to unpack them into individual arguments:

Example
Using * to unpack a list into arguments:

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)
Unpacking Dictionaries with **
If you have keyword arguments stored in a dictionary, you can use ** to unpack them:

Example
Using ** to unpack a dictionary into keyword arguments:

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")
"""
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

student_info(courses, info)
"""
(['Math', 'Art'], {'name': 'John', 'age': 22})
{}
"""
student_info(*courses, **info)
"""
('Math', 'Art')
{'name': 'John', 'age': 22}
"""

month_days = [0, 31, 28, 31, 30, 31, 30 ,31, 31 ,30, 31, 30, 31]
def is_leap(year):
    #Return True for oeap years , False for non-leap years.

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    """Return number of days in that mont in that year"""

    #Year 2017
    #month 2
    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]

print(is_leap(2020))
print(days_in_month(2017,2))
