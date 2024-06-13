#crea un programa que halle el area de un trapecio
base_mayor = float(input("Ingrese la longitud de la base mayor del trapecio: "))
base_menor = float(input("Ingrese la longitud de la base menor del trapecio: "))
A = float(input("Ingrese la altura del trapecio: "))

# Calcular el área del trapecio
A = ((base_mayor + base_menor) * A )/ 2

# Mostrar el resultado
print("El área del trapecio es:", A)
