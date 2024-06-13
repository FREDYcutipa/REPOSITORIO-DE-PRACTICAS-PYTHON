# EJERCICIO 10: Escribir un programa que pida al usuario que introduzca una frase en la consola () y muestre por pantalla la cantidad de 
# caracteres en mayúsculas y cantidad de caracteres en minúsculas

FRASE = input("Ingrese cualquier frase: ")

mayusculas = 0
minusculas = 0

for caracter in FRASE:
    
    if caracter.isupper():
        mayusculas += 1
    
    elif caracter.islower():
        minusculas += 1

print("Numero de caracteres en mayúsculas:", mayusculas)
print("Numero de caracteres en minúsculas:", minusculas)
