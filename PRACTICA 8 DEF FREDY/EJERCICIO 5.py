# Escribir una funcion que reciba una muestra de numeros en una lista y devuelva un diccionario con su media, 
# varianza y desviacion tipica.
NUMEROS_INGRESADOS = input("Ingrese los números separados por comas: ")
NUMEROS = [float(x) for x in NUMEROS_INGRESADOS.split(",")]
def ESTADISTICAS(numeros):
    media = sum(numeros) / len(numeros)
    varianza = sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    desv_tipica = (varianza) ** 0.5  
    
    RESULTADOS = { "media": media, "varianza": varianza, "desviacion tipica": desv_tipica}
    return RESULTADOS

RESULTADOS = ESTADISTICAS(NUMEROS)
print("RESULTADOS:")
print("Los resultados son: ", RESULTADOS)

