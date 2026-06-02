student = {"name": "John", "age":25, "courses":["Math", "CompSci"]}
print(student)
print(student['courses'])

student = {1: "John", "age":25, "courses":["Math", "CompSci"]}
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student[1])
print(student.get('phone'))#Traceback error , use get to return None instead error
print(student.get('phone', 'Not Found')) # Print Not found
print(student) #1: 'John', 'age': 25, 'courses': ['Math', 'CompSci'], 'phone': '555-5555', 'name': 'Jane'}
# Name updated to Jane
student.update({'name': 'Jane', 'age': 26, 'phone': '555-555'})
print(student)
del student ['age']
print(student)
name = student.pop('name')
print(name) # Pop value

student = {"name": "John", "age":25, "courses":["Math", "CompSci"]}
print(student.keys()) # dict_keys(['name', 'age', 'courses'])
print(student.values()) #dict_values(['John', 25, ['Math', 'CompSci']])
print(student.items()) # dict_items([('name', 'John'), ('age', 25), ('courses', ['Math', 'CompSci'])])

for key in student:
    print(key) #looped through and print keys



for key, value in student.items():
    print(key, value) 
    #name John
    #age 25
    #courses ['Math', 'CompSci']


"""
Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
Dictionaries cannot have two items with the same key:
Duplicate values will overwrite existing values:

"""

"""
Dictionary Items - Data Types
The values in dictionary items can be of any data type:
String, int, boolean, and list data types:

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

"""

"""
It is also possible to use the dict() constructor to make a dictionary.
Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

"""
"""
In dict key must be immutable:
"nume"      # string
25          # int
3.14        # float
True        # bool
(1, 2, 3)   # tuple

List != key beacause list is muttable
Set != key because set is muttable

| Tipe    | Key | value |
| ------ | ----- | ------- |
| string | ✅     | ✅       |
| int    | ✅     | ✅       |
| float  | ✅     | ✅       |
| bool   | ✅     | ✅       |
| tuple  | ✅*    | ✅       |
| list   | ❌     | ✅       |
| set    | ❌     | ✅       |
| dict   | ❌     | ✅       |

"""

"""
Difference pop and del
pop:
Delete the key and return the value
ex:
person = {
    "name": "Alin",
    "age": 25
}

value = person.pop("age")
print(value)
print person
25
{'nume': 'Alin'}
pop() delete the key (age) and return the value 25
del:
Delete the element and that s it return nothing
person = {
    "name": "Alin",
    "age": 25
}
del person["age"]
print (person)

{'name': 'Alin'}

Use pop also needs deleted values
nota = elev.pop("matematica")
print(f"Deleted note is {nota}")
Use del when you just want to delete
del nota["matematica"] 
"""