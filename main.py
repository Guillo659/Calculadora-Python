#Author: Guillermo Salgado (El Maligno)
print("EEEEEEEEEEEEEEEEEEEEEElllllll      MMMMMMMM               MMMMMMMM                  lllllll   iiii                                                         ")
print("E::::::::::::::::::::El:::::l      M:::::::M             M:::::::M                  l:::::l  i::::i                                                        ")
print("E::::::::::::::::::::El:::::l      M::::::::M           M::::::::M                  l:::::l   iiii                                                         ")
print("EE::::::EEEEEEEEE::::El:::::l      M:::::::::M         M:::::::::M                  l:::::l                                                                ")
print("  E:::::E       EEEEEE l::::l      M::::::::::M       M::::::::::M  aaaaaaaaaaaaa    l::::l iiiiiii    ggggggggg   gggggnnnn  nnnnnnnn       ooooooooooo   ")
print("  E:::::E              l::::l      M:::::::::::M     M:::::::::::M  a::::::::::::a   l::::l i:::::i   g:::::::::ggg::::gn:::nn::::::::nn   oo:::::::::::oo ")
print("  E::::::EEEEEEEEEE    l::::l      M:::::::M::::M   M::::M:::::::M  aaaaaaaaa:::::a  l::::l  i::::i  g:::::::::::::::::gn::::::::::::::nn o:::::::::::::::o")
print("  E:::::::::::::::E    l::::l      M::::::M M::::M M::::M M::::::M           a::::a  l::::l  i::::i g::::::ggggg::::::ggnn:::::::::::::::no:::::ooooo:::::o")
print("  E:::::::::::::::E    l::::l      M::::::M  M::::M::::M  M::::::M    aaaaaaa:::::a  l::::l  i::::i g:::::g     g:::::g   n:::::nnnn:::::no::::o     o::::o")
print("  E::::::EEEEEEEEEE    l::::l      M::::::M   M:::::::M   M::::::M  aa::::::::::::a  l::::l  i::::i g:::::g     g:::::g   n::::n    n::::no::::o     o::::o")
print("  E:::::E              l::::l      M::::::M    M:::::M    M::::::M a::::aaaa::::::a  l::::l  i::::i g:::::g     g:::::g   n::::n    n::::no::::o     o::::o")
print("  E:::::E       EEEEEE l::::l      M::::::M     MMMMM     M::::::Ma::::a    a:::::a  l::::l  i::::i g::::::g    g:::::g   n::::n    n::::no::::o     o::::o")
print("EE::::::EEEEEEEE:::::El::::::l     M::::::M               M::::::Ma::::a    a:::::a l::::::li::::::ig:::::::ggggg:::::g   n::::n    n::::no:::::ooooo:::::o")
print("E::::::::::::::::::::El::::::l     M::::::M               M::::::Ma:::::aaaa::::::a l::::::li::::::i g::::::::::::::::g   n::::n    n::::no:::::::::::::::o")
print("E::::::::::::::::::::El::::::l     M::::::M               M::::::M a::::::::::aa:::al::::::li::::::i  gg::::::::::::::g   n::::n    n::::n oo:::::::::::oo ")
print("EEEEEEEEEEEEEEEEEEEEEEllllllll     MMMMMMMM               MMMMMMMM  aaaaaaaaaa  aaaalllllllliiiiiiii    gggggggg::::::g   nnnnnn    nnnnnn   ooooooooooo   ")
print("                                                                                                                g:::::g                                    ")
print("                                                                                                    gggggg      g:::::g                                    ")
print("                                                                                                    g:::::gg   gg:::::g                                    ")
print("                                                                                                     g::::::ggg:::::::g                                    ")
print("                                                                                                      gg:::::::::::::g                                     ")
print("                                                                                                        ggg::::::ggg                                       ")
print("                                                                                                           gggggg                                          ")

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
