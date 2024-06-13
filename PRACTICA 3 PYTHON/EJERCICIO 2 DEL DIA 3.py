# EJERCICIO 2: Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y 
# muestre por pantalla cada uno de los productos en una línea distinta
productos = input("Ingrese tus productos de la cesta, separados por comas: ")

lista_productos = productos.split(',')

for producto in lista_productos:
    print(producto.strip())