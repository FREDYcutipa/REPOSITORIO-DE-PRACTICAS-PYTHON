# Escribir un programa que cree un diccionario de traducción español-inglés.
# El usuario introducirá las palabras en español e inglés separadas por dos puntos,
# y cada par <palabra>:<traducción> separados por comas. 
# El programa debe crear un diccionario con las palabras y sus traducciones. 
# Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. 
# Si una palabra no está en el diccionario debe dejarla sin traducir. 
# AGREGAR AL DICCIONARIO LOS NUEVOS ELEMENTOS PARA QUE GUARDEN AUTOMATICAMENTE.

DICCIONARIO = {}
PALABRAS = input("ingrese su palabra de esta forma: <palabra>:<traducción> <ESPAÑOL>:<INGLES>: ")
for i in PALABRAS.split(","):
    clave, valor = i.split(":")
    DICCIONARIO[clave.strip()] = valor.strip()
print("\nDiccionario de traducción creado:")
for esp, ing in DICCIONARIO.items():
    print(f"{esp}: {ing}")
while True:
    AGREGAR_PALABRA = input("¿Desea agregar una nueva palabra al diccionario? (si/no): ").strip().lower()  
    if AGREGAR_PALABRA == "si":
        NUEVA_PALABRA = input("Escribe la palabra en español: ").strip()
        NUEVA_P_INGLES = input("Escribe la palabra en inglés: ").strip()
        DICCIONARIO[NUEVA_PALABRA] = NUEVA_P_INGLES
        print("\nDiccionario actualizado:")
        for esp, ing in DICCIONARIO.items():
            print(f"{esp}: {ing}")
    elif AGREGAR_PALABRA == "no":
        break
    else:
        print("Por favor, responda 'si' o 'no'.")
FRASE = input("\nIntroduce una frase en español con las palabras que ingresó: ")
print("\nTraducción de la frase:")
for palabra in FRASE.split():
    if palabra in DICCIONARIO:
        print(DICCIONARIO[palabra], end=" ")
    else:
        print(palabra, end=" ")

