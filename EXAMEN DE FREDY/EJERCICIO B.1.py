"""Escriba un programa que permita crear dos listas de palabras y que, a continuación, 
elimine de la primera lista los nombres de la segunda lista."""

n1 = int(input("¿Cuántas palabras tiene en la primera lista? "))
LISTA_A = []
for i in range(n1):
    palabra = input("Introduce la palabra " + str(i + 1) + ": ")
    LISTA_A.append(palabra)
print("Primera lista creada:", LISTA_A)

n2 = int(input("¿Cuántas palabras tiene en la segunda lista? "))
LISTA_B = []
for i in range(n2):
    palabra = input("Introduce la palabra " + str(i + 1) + ": ")
    LISTA_B.append(palabra)
print("Segunda lista creada:", LISTA_B)
for palabra in LISTA_B:
    while palabra in LISTA_A:
        LISTA_A.remove(palabra)

print("Lo que queda de la primera lista despues de eliminar lo de la segunbda es:", LISTA_A)
print("La segunda lista era: ", LISTA_B)
