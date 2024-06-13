#EJERCICIO 1: Escribir un programa que pregunte el nombre el un producto, su precio y un número de 
#unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de 
#unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales

nombre_producto = input("Ingrese el nombre del producto: ")
precio_unitario = input("Ingrese el precio por unidad: ")
num_unidades = input("Ingrese el número de pedidos: ")

precio_unitario = "0" * (6 - len(precio_unitario)) + precio_unitario
num_unidades = "0" * (3 - len(num_unidades)) + num_unidades

coste_total = str(int(precio_unitario) * int(num_unidades))

coste_total = "0" * (8 - len(coste_total)) + coste_total

cadena_salida = ("NOMBRE:",nombre_producto) + ("PRECIO U",precio_unitario + ".00" ) + ("UNIDAD",num_unidades) + ("COSTO UNI", coste_total + ".00")
print(cadena_salida)

