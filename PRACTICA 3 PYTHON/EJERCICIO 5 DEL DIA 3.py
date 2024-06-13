#EJERCICIO 5: Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida

frase = input("Introduce una frase: ")
frase_invertida = ""
longitud = len(frase)
indice = longitud - 1
while indice >= 0:
    frase_invertida += frase[indice]
    indice -= 1
print("Frase invertida:", frase_invertida)
