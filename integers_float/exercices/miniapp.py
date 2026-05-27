# 1 
num1 = float(input("Primul numar: "))
num2 = float(input("Al doilea numar: "))

operator = input("Operator (+, -, *, /): ")
if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Operator invalid")


# 2
nota = float(input("Nota de plata: "))
procent = float(input("Procent bacsis: "))

total = nota + nota * procent / 100

print("Total:", total)