# EJERCICIO 4: Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por 
# pantalla la misma frase pero con la vocal introducida en mayúscula

FRASE = input("Ingrese una frase: ")
VOCAL = input("Ingrese una vocal: ")

vocal_mayuscula = VOCAL.upper()
frase_con_vocal_mayuscula = FRASE.replace(VOCAL, vocal_mayuscula)

print("Frase con la vocal en mayúscula:", frase_con_vocal_mayuscula)
