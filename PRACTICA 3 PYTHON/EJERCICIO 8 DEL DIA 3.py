# EJERCICIO 8 Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla True si una 
# cadena contiene solo dígitos y False en caso contrario

frase = input("Ingrese una frase: ")

es_digito = frase.isdigit()

print(es_digito)
