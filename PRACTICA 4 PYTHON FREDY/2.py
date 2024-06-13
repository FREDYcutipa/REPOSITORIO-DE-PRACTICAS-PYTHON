NUM_DIVIDENDO = input("INGRESE EL NUMERO DIVIDENDO: ")
dividendo = float(NUM_DIVIDENDO)

NUM_DIVISOR = input("INGRESE EL NUMERO DIVISOR: ")
divisor = float(NUM_DIVISOR)
    
if divisor == 0: 
     print("Error: no se puede dividir por 0.")
else:    
    resultado = dividendo / divisor
    print("El cociente de la división es: ",resultado)
