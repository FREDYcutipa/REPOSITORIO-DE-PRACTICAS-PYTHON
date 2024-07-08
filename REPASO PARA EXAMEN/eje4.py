#Escribir un programa que cree un dicionario vacio y lo vaya llamando con informacion sobre un estudiante
#luego imprima el contenido del diccionario.
estudiante = {}
continuar = True
while continuar:
    clave = input ("Que datos quieres ingresar del estudiante?: ")
    valor = input (clave + ":")
    estudiante[clave] = valor
    print(estudiante)
    continuar = input("¿quieres ingresar mas datos SI/NO?") == "si"