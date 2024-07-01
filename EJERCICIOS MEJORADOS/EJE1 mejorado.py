# Escribir un programa que guarde en un diccionario los precios de las frutas:
# FRESA cuesta 12.50, MANZANA cuesta 8.40, PERA cuesta 5.60, NARANJA cuesta 3.50, 
# pregunte al usuario por una fruta, un numero de kilos y muestre por pantalla el precio de este numero de kilos de fruta,
# # si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# MODIFICAR PARA UNA SEGUNDA OPCION DE COMPRAS.

FRUTAS = {"Fresa": 12.50, "Manzana": 8.40, "Pera": 5.60, "Naranja": 3.50}
SI_CONTINUAMOS = "si"
NO_CONTINUAMOS = "no"
COMPRA_TOTAL = 0  
while SI_CONTINUAMOS.lower() == "si":
    FRUTA = input("Ingrese nombre de la fruta: ").title() 
    kg = float(input("Ingrese la cantidad de kilos: "))
    if FRUTA in FRUTAS:
        precio_fruta = FRUTAS[FRUTA] * kg
        print(kg, "kilos de", FRUTA, "valen", precio_fruta, "soles")
        COMPRA_TOTAL += precio_fruta
    else:
        print("Lo siento mucho, la fruta", FRUTA, "no está disponible.")
    SI_CONTINUAMOS = input("¿Tine otras compras? (si/no): ")
NO_CONTINUAMOS = print("El total de su compra es:", COMPRA_TOTAL, "soles GRACIAS POR SU COMPRA")
