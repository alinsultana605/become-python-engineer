from my_module import find_index, test
# from my_module import * ## import all
# from my_module import find_index as test ## create alias
import sys
# sys.path.append("/users.....") import a module from another place
import random
import math
import datetime
import calendar
import os

courses = ['Histroy', 'Math', 'Physiscs', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)
# print(sys.path)

random_course = random.choices(courses)
print(random_course)

rads = math.radians(90)
print(rads)

today = datetime.date.today()
print(today)

print(calendar.isleap(2020))

print(os.getcwd())
print(os.__file__)
