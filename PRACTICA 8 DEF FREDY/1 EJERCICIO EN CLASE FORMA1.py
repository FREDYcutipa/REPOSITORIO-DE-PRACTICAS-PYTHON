# crear un programa que resuelva los ejercicios vasicos matematicos.

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
    
print("\nSeleccione la operación que desea realizar:")
OPERACION = input("Ingrese la operación (+, -, *, /, ** ): ")

if OPERACION == "+":
    resultado = a + b
    print("Resultado de ", a, "+", b,  "=", resultado)
elif OPERACION == "-":
    resultado = a - b
    print("Resultado de ", a, "-", b , "=", resultado)
elif OPERACION == "*":
    resultado = a * b
    print("Resultado de ", a, "*", b , "=", resultado)
elif OPERACION == "/":
    if b == 0:
        resultado = "Error: División por cero no permitida"
    else:
        resultado = a / b
    print("Resultado de ", a, "/", b , "=", resultado)
elif OPERACION == "**":
    resultado = a ** b
    print("Resultado de ", a, "**", b , "=", resultado)
else:
    print("\nOperación no válida. Por favor, ingrese una operación válida (+, -, *, /, **).")

