# modifique el programa anterior de manera que las listas se escriban al final del programa:
def crea_lista(contador):
    numero = int(input(f"Digame cuantas palabras tiene la lista{contador}: "))
    lista = []
    for i in range(numero):
        palabra = input(f"Digame la palabra {i+1}: ")
        lista += [palabra]
    return lista

print("GENERADOR DE LISTAS: ")
numero_listas = int(input("¿Cuántas listas quiere escribir? "))

listas =[]
for i in range (1, numero_listas + 1):
    listas += [crea_lista(i)]
    
for i in range (numero_listas):
    print(f"la lista {i + 1} es: {listas[i]}")
