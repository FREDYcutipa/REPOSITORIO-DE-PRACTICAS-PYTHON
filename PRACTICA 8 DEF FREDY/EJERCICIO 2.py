# Escribir una funsion que calcule el area del circulo y 
# otra que calcule el volumen de un cilindro usando la primera funsion.
RADIO_DEL_CIRCULO = float(input("INGRESE EL RADIO DEL CIRCULO: "))
ALTURA_DEL_CILINDRO = float(input("INGRESE LA ALTURA DEL CILINDRO: "))
PI = 3.1416

def AREA_DEL_CIRCULO (RADIO_DEL_CIRCULO):
    return PI * RADIO_DEL_CIRCULO ** 2      # FORMULA AC=pi*radio**2

def VOLUMEN_DEL_CILINDRO (RADIO_DEL_CIRCULO, ALTURA_DEL_CILINDRO):
    AREA_BASE = AREA_DEL_CIRCULO (RADIO_DEL_CIRCULO)
    return AREA_BASE * ALTURA_DEL_CILINDRO

AREA = AREA_DEL_CIRCULO (RADIO_DEL_CIRCULO)
VOLUMEN = VOLUMEN_DEL_CILINDRO (RADIO_DEL_CIRCULO, ALTURA_DEL_CILINDRO)
print("El AREA del circulo con el RADIO ingresado ", RADIO_DEL_CIRCULO, "es: ", AREA )
print("El VOLUMEN del cilindro con RADIO ingresado ", RADIO_DEL_CIRCULO, "y ALTURA DEL CILINDRO ", ALTURA_DEL_CILINDRO, "es: ", VOLUMEN )
        