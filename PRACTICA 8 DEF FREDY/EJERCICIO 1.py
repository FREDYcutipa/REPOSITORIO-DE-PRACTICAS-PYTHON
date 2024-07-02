# Escribir una función que calcule el total de una factura tras aplicarle el IGV. 
# La funsion debe recibir la cantidad sin IGV y el porcentaje de IGv a aplicar, 
# y devolver el total de la factura. si se invoca la funcion sin pasarle el porcentaje de IGB, deberá aplicar un 18%.
Costo_sin_IGV = float(input("INGRESE EL COSTO SIN IGV: "))
Porcentaje_IGV = input(" INGRESE EL PORCENTANJE DE IGV: O (presione Enter para usar IGV de 18%): ")

def FACTURA_TOTAL(Costo_sin_IGV, Porcentaje_IGV = 18 ):
    IGV = Costo_sin_IGV * (Porcentaje_IGV / 100)
    TOTAL = Costo_sin_IGV + IGV
    return TOTAL

if Porcentaje_IGV:
    Porcentaje_IGV = float(Porcentaje_IGV)
    COST_TOTAL_FACTURA = FACTURA_TOTAL(Costo_sin_IGV, Porcentaje_IGV)
else:
    COST_TOTAL_FACTURA = FACTURA_TOTAL(Costo_sin_IGV)

print("EL COSTO TOTAL INCLUIDO IGV ES: ", COST_TOTAL_FACTURA)
print("GRACIAS POR SU COMPRA")
