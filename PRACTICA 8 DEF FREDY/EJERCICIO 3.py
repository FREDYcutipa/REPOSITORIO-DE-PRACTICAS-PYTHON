# Escribe una funsion que reciba una muestra del numero en una lista y devuelva su media.
INGRESO_DE_NUMEROS = input("Ingrese los números separados por COMAS: ")
NUMEROS = [float(x) for x in INGRESO_DE_NUMEROS.split(",")]

def calcular_media(NUMEROS):
    suma = sum(NUMEROS)
    cantidad = len(NUMEROS)
    MEDIA = suma / cantidad
    return MEDIA

MEDIA = calcular_media(NUMEROS)
print("De la lista de numeros ",NUMEROS, "su media es: ", MEDIA)
