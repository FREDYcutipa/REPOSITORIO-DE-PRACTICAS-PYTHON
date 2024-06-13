#EJERCICIO 7 Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en 
#líneas distintas el nombre del usuario tantas veces como el número introducido

nombre_usuario = input("Ingrese su nombre: ")
numero_entero = int(input("Ingrese un número entero: "))

cadena_repetida = (nombre_usuario + "\n") * numero_entero

print(cadena_repetida, end="")
