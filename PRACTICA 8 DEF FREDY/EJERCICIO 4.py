# Escribir una funcion que reciba una muestra de numeros en una lista y devuelva otra lista con sus cuadrados.
INGRESO_DE_NUMEROS = input("Ingrese los números separados por COMAS: ")
numeros = [float(x) for x in INGRESO_DE_NUMEROS.split(",")]

def calcular_cuadrados(numeros):
    cuadrados = [num ** 2 for num in numeros]
    return cuadrados

cuadrados = calcular_cuadrados(numeros)
print("LOS NUMEROS QUE USTED INGRESÓ SON: ", numeros )
print("NUMEROS CON SUS CUADRADOS SON: ",cuadrados )
