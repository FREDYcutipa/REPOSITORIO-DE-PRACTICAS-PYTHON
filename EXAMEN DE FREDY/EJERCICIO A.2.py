"""Escriba un programa que pida un año y que escriba si es bisiesto o no. Se recuerda 
que los años bisiestos son múltiplos de 4, pero los múltiplos de 100 no lo son, aunque 
los múltiplos de 400 sí. Estos son algunos ejemplos de posibles respuestas: 
2012 es bisiesto.
2010 no es bisiesto.
2000 es bisiesto.
1900 no es bisiesto. """

def AÑO_BISIESTO(AÑO):
    if AÑO % 400 == 0:
        return True
    elif AÑO % 100 == 0:
        return False
    elif AÑO % 4 == 0:
        return True
    else:
        return False

AÑO = int(input("Introdusca cualquier año: "))

if AÑO_BISIESTO(AÑO):
    print("EL ", AÑO, "ES UN AÑO BISIESTO.")
else:
    print("El ", AÑO, "NO ES UN AÑO BISIESTO.")
