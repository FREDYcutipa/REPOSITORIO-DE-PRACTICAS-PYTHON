# escriba un programa que permita crear una lista de palabras, 
# el programa tiene que pedir un numeroy luego solicitar ese numero de palabras para crear la lista.por ultimo imprimir la lista. 

numero = int(input("cuantas palabras tiene su lista: "))
if numero < 1:
    print ("No se genera ninguna lista: ")
else:
    lista = []
    for i in range (numero):
        palabra = input (f"digame la {i + 1} palabra ")
        lista += [palabra] 
    print ("la lista greada es: ", lista)

                   