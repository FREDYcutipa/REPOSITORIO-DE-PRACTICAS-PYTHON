# escriba un programa que pida cuantas listas se quiere crear y la solicite a continuacion:
def crea_lista(contador):
    numero = int(input(f"Digame cuantas palabras tiene la lista {contador}: "))
    lista = []
    for i in range(numero):
        palabra = input(f"Digame la palabra {i + 1}: ")
        lista += [palabra]
    return lista

print("GENERADOR DE LISTAS: ")
numero = int(input("¿Cuántas listas quiere escribir? "))
for i in range (1, numero + 1 ):
    print(f"la lista {i} es: {crea_lista(i)}")