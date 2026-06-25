import math
import random
from datetime import datetime

print(math.sqrt(144))
print(math.pi)
print(math.sin(1))

print(random.randint(1, 10))

lista = ["Ana", "Ion", "Maria"]
print(random.choice(lista))

print(datetime.now())
print(datetime.now().date())
print(datetime.now().strftime('%d/%m/%Y, %H:%M:%S'))

import os

print(os.getcwd())
print(os.listdir())
# os.mkdir('Test_folder')