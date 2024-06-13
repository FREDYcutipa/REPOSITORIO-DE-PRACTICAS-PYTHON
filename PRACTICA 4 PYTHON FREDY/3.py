EDAD_DE_JOVEN = input("¿CUAL ES SU EDAD ACTUAL? ")
INGRESOS = input("¿CUANTO GANA AL MES? ")
  
edad = int(EDAD_DE_JOVEN)
ingresos = float(INGRESOS)
    
if edad >= 18 and ingresos >= 2000:
    print("Usted debe pagar impuestos.")
else:
    print("Usted no tiene que pagar impuestos.")
