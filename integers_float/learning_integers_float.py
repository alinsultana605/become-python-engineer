
"""
Python Numbers
There are three numeric types in Python:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
"""

# To verify the type of any object in Python, use the type() function:
#Integer
num = 3 
print(type(num))

# Float
num = 3.14 
print(type(num))

# Complex
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

"""
Arihmetic Operators:
1. Addition: 3 + 2
2. Substraction: 3 - 2
3. Multiplication: 3 * 2
4. Division: 3 / 2
5. Floor Division: 3 // 2
6. Exponent: 3 ** 2
7. Modulus: 3 % 2
"""
print (3 + 2) # 5
print (3 - 2) # 1
print (3 * 2) # 6
print (3 / 2) # 1.5
print (3 // 2 )# 1
print (3 ** 2)# 9
print(3 % 2) # 1

print(3 * 2 + 1) # 7 
print(3 * (2 + 1)) # 9

num = 1
num = num + 1
print (num)


print(abs(-3))
print(round(3.75))
print(round(3.75, 1))

"""
Comparison:
Equal: 3 == 3
Not Equal 3 != 2 
Greater Than: 3 > 2
Less Than: 3 < 2
Greater or Equal 3 >= 2
Less or Equal 3 <= 2
"""

num_1 = 3
num_2 = 2
print(num_1 == num_2) #False
print(num_1 != num_2) #True
print(num_1 > num_2) #True
print(num_1 < num_2) #False
print(num_1 >= num_2) #True
print(num_1 <= num_2) #False

num_1 = "100"
num_2 = "200"

print(int(num_1) + int(num_2)) # 300, else without int() concat string and return "100200"


"""
Python does not have a random() function to make a random number, 
but Python has a built-in module called random that can be used to make random numbe
"""
import random

print(random.randrange(1, 10))