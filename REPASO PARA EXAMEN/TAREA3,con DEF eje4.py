#Escribir un programa que cree un dicionario vacio y lo vaya llamando con informacion sobre un estudiante
#luego imprima el contenido del diccionario.
def datos_del_estudiante():
    estudiante = {}
    continuar = True
    while continuar:
        clave = input("¿Qué dato quieres ingresar del estudiante?: ")
        valor = input(clave + ": ")
        estudiante[clave] = valor
        print(estudiante)
        respuesta = input("¿Quieres ingresar más datos? (SI/NO): ").lower()
        if respuesta != "si":
            continuar = False
    return estudiante
datos_estudiante = datos_del_estudiante()
print("Datos del estudiante ingresados:")
for clave, valor in datos_estudiante.items():
    print(clave + ":", valor)
