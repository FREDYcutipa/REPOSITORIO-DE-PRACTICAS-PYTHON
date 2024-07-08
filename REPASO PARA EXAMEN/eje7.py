# escriba un programa que permita crear una lista de palabras, 
# el programa tiene que pedir un numeroy luego solicitar ese numero de palabras para crear la lista.por ultimo imprimir la lista. 
def crea_lista():
    numero = int(input("digame cuantas palabras tiene la lista: "))
    lista = []
    for i in range(numero):
        palabra = input (f"digame la palabra {i+1}:")
        lista += [palabra]
    return lista
print (f"la lista creada es: {crea_lista()}")    