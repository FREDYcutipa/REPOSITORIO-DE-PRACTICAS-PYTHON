# EscriYir una funsion que calcule el maximo como un divisor de dos numeros y otra que calcule el minimo comun multiplo.
A = int(input("INGRESE SU NUMERO: "))
B = int(input("INGRESE SU OTRO NUMERO: "))

def MAXIMO_COMO_UN_DIVISOR(X, Y):
    while Y:
        X, Y = Y, X % Y
    return X

def MAXIMO_COMO_UN_MULTIPLO(X, Y):
    return abs(X * Y) // MAXIMO_COMO_UN_DIVISOR(X, Y) 

R_MCD = MAXIMO_COMO_UN_DIVISOR(A, B)
print("El máximo común Divisor es: ", R_MCD )

R_MCM = MAXIMO_COMO_UN_MULTIPLO(A, B)
print("El máximo común Multiplo es: ",R_MCM)

