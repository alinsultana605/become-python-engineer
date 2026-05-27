# STRINGS = IMMUTABLE

# Print message
message = 'Hello World'
print(message)

# The len() function returns the length of a string
print(len(message))

# string.index(value, start, end)
"""
value = Required. The value to search for
start = Optional. Where to start the search. Default is 0
end = Optional. Where to end the search. Default is to the end of the string
"""

txt = "Hello, welcome to my world."
x = txt.index("l")
print(x)


# String slicing in Python is a way to get specific parts of a string by using start,
# end and step values. It’s especially useful for text manipulation and data parsing.
""" substring = s[start : end : step]
s: The original string.
start (optional): Starting index (inclusive). Defaults to 0 if omitted.
end (optional): Stopping index (exclusive). Defaults to the end of the string if omitted.
step (optional): Interval between indices. A positive value slices from left to right,
 while a negative value slices from right to left. If omitted, 
 it defaults to 1 (no skipping of characters).
Return Type: The result of a slicing operation is always a string (str type) 
that contains a subset of the characters from the original string.
"""



# Return first character
print(message[0])

# Return character from possition 10
print(message[10])

# From index = to index 5(without possioton number 5, "Hello")
# 0 = H, 1 = E, 2 = L , 3 = L , 4 = O
print(message[0:5])

#From start to possition 5 (Hello)
print(message[:5])

# From index number 6 to final (World)
print(message[6:])

# string lowercase (hello world)
print(message.lower())

# string uppercase(HELLO WORLD)
print(message.upper())

"""
The count() method returns the number of times a specified value appears in the string.
string.count(value, start, end)
value:Required. A String. The string to value to search for
start:Optional. An Integer. The position to start the search. Default is 0
end: Optional. An Integer. The position to end the search. Default is the end of the string
"""
print(message.count('l'))


"""
The find() method finds the first occurrence of the specified value.
The find() method returns -1 if the value is not found.
The find() method is almost the same as the index() method, the only difference 
is that the index() method raises an exception if the value is not found.

string.find(value, start, end)
value: Required. The value to search for
start: Optional. Where to start the search. Default is 0
end: Optional. Where to end the search. Default is to the end of the string


"""
print(message.find('World'))


"""
The replace() method replaces a specified phrase with another specified phrase.
string.replace(oldvalue, newvalue, count)
oldvalue:Required. The string to search for
newvalue: Required. The string to replace the old value with
count: 	Optional. A number specifying how many occurrences of the 
old value you want to replace. Default is all occurrences

"""
new_message = message.replace('World', 'Universe')
print(new_message)

"""
Merge variable a with variable b into variable c:
"""
greeting = 'Hello'
name = 'Alin'
greeting_message = greeting + ', ' + name + '. Welcome!'
print(greeting_message)

"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.
he placeholder is defined using curly brackets: {}
The format() method returns the formatted string.

string.format(value1, value2...)
value1, value2: 
Required. One or more values that should be formatted and inserted in the string.
The values are either a list of values separated by commas, a key=value list, or a combination of both.
The values can be of any data type.

The placeholders can be identified using named indexes {price}, numbered indexes {0}, or even empty placeholders {}.
"""

messages = '{}, {}, Welcome!'.format(greeting, name)
print(messages)

messagess = f'{greeting.lower()}, {name.upper()}, Welcome!'
print(messagess)