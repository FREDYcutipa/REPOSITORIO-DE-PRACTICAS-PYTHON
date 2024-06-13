# EJERCICIO 3: Escribir un programa que pregunte por consola el precio de un producto en soles con dos decimales y muestre por 
# pantalla el número de soles y el número de céntimos del precio introducido

precio = float(input("Ingrese el precio del producto: "))

SOLES = int(precio)
CENTIMOS = int((precio - SOLES) * 100)

print("Número de soles:", SOLES)
print("Número de céntimos:", CENTIMOS)
