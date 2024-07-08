# Escriba un programa que permita crear una lista de palabras y que, a continuacion,
# pida una palabra, que diga cuantas veces aparece esa palabra en la lista.

numero = int(input("cuantas palabras tiene su lista: "))
if numero < 1:
    print ("No se genera ninguna lista: ")
else:
    lista = []
    for i in range (numero):
        palabra = input (f"digame la {i + 1} palabra ")
        lista += [palabra] 
    print ("la lista greada es: ", lista)
    
    buscar = input ("que palabra decea buscar: ")
    contador = 0
    for i in lista:
        if i == buscar:
            contador +=1
    if contador == 0:
        print ("la palanra", buscar,  " no aparece en la lista:")
    elif contador ==1:
         print ("la palanra", buscar, " aparece una vez en la lista:")
    else:
         print ("la palanra", buscar, " aparece", contador,  "veces en la lista:")