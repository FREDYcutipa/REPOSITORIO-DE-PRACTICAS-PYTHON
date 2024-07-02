# Escribir un programa que escriba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia, 
# escribir otra funsion que reciba el diccionario generado con la funsion anterior 
# y devuelva una tupla con la palabra mas repetida y su frecuencia.
FRASE_INTRO = input("Introduce una frase: ")

def PALABRAS(FRASE_INTRO):
    palabras = FRASE_INTRO.lower().split()  
    
    frecuencia_palabras = {}  
    
    for palabra in palabras:
        palabra = palabra.strip('.,!?"\'') 
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    return frecuencia_palabras

def PALABRAS_FRECUENTES(diccionario):
    palabra, frecuencia = max(diccionario.items(), key=lambda x: x[1])
    return (palabra, frecuencia)

FRECUENCIA = PALABRAS(FRASE_INTRO)
print("Diccionario de frecuencia:",  FRECUENCIA)

PALABRAS_MAS_FRECUENTES = PALABRAS_FRECUENTES(FRECUENCIA)
print("La palabra más frecuente es", PALABRAS_MAS_FRECUENTES, " con una frecuencia de " , PALABRAS_MAS_FRECUENTES)
