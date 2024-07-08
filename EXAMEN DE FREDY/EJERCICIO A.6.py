"""Escribir una función que calcule el total de una factura tras aplicarle el IGV. La 
función debe recibir la cantidad sin IGV y el porcentaje de IGV a aplicar, y devolver 
el total de la factura. Si se invoca la función sin pasarle el porcentaje de IGV, 
deberá aplicar un 12%."""

def CALCULO_DE_FACTURA(costo_sin_IGV, porcentaje_igv=12):
    IGV = porcentaje_igv / 100
    total_con_igv = costo_sin_IGV * (1 + IGV)
    return total_con_igv
cantidad = float(input("Introduce el costo sin IGV: "))
porcentaje = input("Introduce el porcentaje de IGV a aplicar,o precione enter para poner el 12 por ciento de IGv: ")
if porcentaje:
    porcentaje = float(porcentaje)
    total = CALCULO_DE_FACTURA(cantidad, porcentaje)
else:
    total = CALCULO_DE_FACTURA(cantidad)
print("El total de la factura con el IGV aplicado es:", total)
