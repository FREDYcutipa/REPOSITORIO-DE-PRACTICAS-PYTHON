# Escriba un programa que permita crear una lista de palabras y que, a continuacion,
# pida una palabra, que diga cuantas veces aparece esa palabra en la lista.
def crear_lista():
    numero = int(input("¿Cuántas palabras tiene su lista?: "))
    if numero < 1:
        print("No se genera ninguna lista.")
        return
    
    lista = []
    for i in range(numero):
        palabra = input(f"Dígame la palabra {i + 1}: ")
        lista.append(palabra)
    
    print("La lista generada es:", lista)
    return lista

def buscar_palabra(lista):
    buscar = input("¿Qué palabra desea buscar?: ")
    contador = 0
    for palabra in lista:
        if palabra == buscar:
            contador += 1
    
    if contador == 0:
        print(f"La palabra '{buscar}' no aparece en la lista.")
    elif contador == 1:
        print(f"La palabra '{buscar}' aparece una vez en la lista.")
    else:
        print(f"La palabra '{buscar}' aparece {contador} veces en la lista.")

print("GENERADOR Y BUSCADOR DE LISTAS: ")
lista_final = crear_lista()
if lista_final:
    buscar_palabra(lista_final)
