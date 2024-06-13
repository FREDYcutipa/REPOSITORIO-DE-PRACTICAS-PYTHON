# EJERCICIO 6: Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el 
# nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra 
# solo con la primera letra del nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando 
# mayúsculas y minúsculas como quiera

nombre_completo = input("Ingrese su nombre completo: ")

print("Nombre completo en minúsculas:", nombre_completo.lower())
print("Nombre completo en mayúsculas:", nombre_completo.upper())

partes_nombre = nombre_completo.split()
nombre_capitalizado = ' '.join(nombre.capitalize() for nombre in partes_nombre)

print("Nombre completo con la primera letra de cada parte en mayúscula:", nombre_capitalizado)
