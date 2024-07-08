"""Escribir un programa que reciba una cadena de caracteres y devuelva un 
diccionario con cada palabra que contiene y su frecuencia. Escribir otra función 
que reciba el diccionario generado con la función anterior y devuelva una tupla 
con la palabra más repetida y su frecuencia."""

def CONTEO_DE_PALABRA(cadena):
    palabras = cadena.lower().split()  
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

def PALABRA_MAS_FRECUENTE(palabra_frecuente):
    palabra_de_mayor_cant = max(palabra_frecuente, key=palabra_frecuente.get)
    frecuencia_max = palabra_frecuente[palabra_de_mayor_cant]
    return (palabra_de_mayor_cant, frecuencia_max)

cadena = input("Introduce una frase: ")
frecuencia_palabras = CONTEO_DE_PALABRA(cadena)

print("Se muestra cada palabra de la frase con su frecuencia:")
for palabra, frecuencia in frecuencia_palabras.items():
    print("la palabra", palabra, ":", frecuencia, "veces")

palabra_frecuente, frecuencia = PALABRA_MAS_FRECUENTE(frecuencia_palabras)
print("La palabra más frecuente es", palabra_frecuente,"con una frecuencia de", frecuencia, "veces.")
