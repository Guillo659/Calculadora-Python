#Author: Guillermo Salgado (El Maligno)

# Variables
num1 = int
num2 = int
res = int
operacion = str

# Entrada de datos
print("Hola humano, bienvenido a la calculadora\n")
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

# Menu de operaciones
print("\nHumano, las operaciones disponibles son: ")
print("\t[*] Suma")
print("\t[*] Resta")
print("\t[*] Multiplicacion")
print("\t[*] Division")

# stdint operacion
operacion = input("Humano, ¿Que operacion deseas realizar?: ")

# Validando proceso
if operacion == "Suma":
  res = num1 + num2
elif operacion == "Resta":
  res = num1 - num2
elif operacion == "Multiplicacion":
  res = num1 * num2
elif operacion == "Division":
  # Validando division
  if num2 != 0:
    res = num1 / num2
  else:
    res = 0
    print("Humano, no se puede dividir por 0")

# Salida de datos (stdout)
print("El resultado es: ", res)