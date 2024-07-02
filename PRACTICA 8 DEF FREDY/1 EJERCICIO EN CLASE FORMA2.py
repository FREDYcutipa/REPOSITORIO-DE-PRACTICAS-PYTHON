# crear un programa que resuelva los ejercicios vasicos matematicos.
def OPERADORES(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    division = num1 / num2 
    potencia = num1 ** num2
    return suma, resta, multiplicacion, division, potencia
 
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
        
suma, resta, multiplicacion, division, potencia = OPERADORES(num1, num2)
        
print("Resultados:")
print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicación es: ", multiplicacion)
print("La división es: ", division)
print("La potencia es: ", potencia)