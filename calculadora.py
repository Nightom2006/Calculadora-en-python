def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

print("Calculadora")

a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero:"))

operador = input("Ingrese la opracion a realizar: ")

if operador == "+":
    print("el resultado de la suma es: " + str(suma(a, b)))
elif operador == "-":
    print("El resultado de la resta es: " + str(resta(a, b)))
elif operador == "*":
    print("El resultado de la multiplicacion es: " + str(multiplicacion(a, b)))
elif operador == "/":
    print("El resultado de la division es: " + str(division(a, b)))