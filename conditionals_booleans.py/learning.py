"""
Comparison:
Equal: 3 == 3
Not Equal 3 != 2 
Greater Than: 3 > 2
Less Than: 3 < 2
Greater or Equal 3 >= 2
Less or Equal 3 <= 2
"""

language = "java"

if language == "python":
    print("Language is python")
elif language == "java":
    print("Language is Java")
elif language == "javaScript":
    print("Language is javaScript")
else:
    print("No Match")

"""
and
or
not

AND:
| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

OR:
| A     | B     | A and B |
| ----- | ----- | ------- |
| True  | True  | True    |
| True  | False | False   |
| False | True  | False   |
| False | False | False   |

NOT:
| A     | not A |
| ----- | ----- |
| True  | False |
| False | True  |

"""

user = "admin"
logged_in = True
if user == "admin" and logged_in:
    print("Admin Page")
else:
    print("Bad credentials")

if not logged_in:
    print("Please log in")
else:
    print("Welcome")

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))
print(a is b) #False because the id it s different, if i put b = a the condition is true because we have the same id

"""
#False Values:
    False
    None
    Zero and any numeric type
    Any empty sequence, for example , ", {}, []
    Any empyty mapping, for example {}
"""
condition = False

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")

"""
In programming you often need to know if an expression is True or False.
You can evaluate any expression in Python, and get one of two answers, True or False.
When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)

The bool() function allows you to evaluate any value, and give you True or False in return,
print(bool("Hello"))
print(bool(15))

"""