#IMMUTABLE

tuple_1 = ('Histroy', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)
# tuple_1[0] = 'Art'
print(tuple_1) #TypeError: 'tuple' object does not support item assignment
print(tuple_1[3]) #CompSci

"""
On tuple, doesn t have nearly as many methods as a list
we can t append, remove but it s possible to loop, to access value, etc
"""